#    Word Car automotive narration system
#    Copyright (C) 2017, Ross Goodwin
#    Full license at: https://github.com/rossgoodwin/wordcar

import pika
import sys
import os
import time
from datetime import datetime
import subprocess
import random
from random import sample as rs, choice as rc, randint as ri
import threading
from collections import defaultdict
from hashids import Hashids
import shutil
import webbrowser
import requests
import json
from noise import pnoise1
from pattern.en import numerals
# import razer_rgb
# import serial
import thermal

# GPS STUFF

from gps3 import gps3
import json

import foursquare
import fs_api_keys

# AUDIO STUFF

from record_audio import record


def time_parse():
    dt = datetime.now()

    h = dt.hour
    m = dt.minute

    time_str_list = list()

    time_str_list.append(rc(['The time was', 'It was']))
    
    def midnight_noon():
        if h == 0:
            time_str_list.append('midnight')
        elif h == 12:
            time_str_list.append('noon')

    def x_oclock_in_the():
        if not h in [0,12]:
            if h < 12:
                time_str_list.append(numerals(h))
            else:
                time_str_list.append(numerals(h-12))
            time_str_list.append("o'clock")
            if h < 12:
                time_str_list.append('in the morning')
            elif h > 17:
                time_str_list.append('in the evening')
            else:
                time_str_list.append('in the afternoon')

    def normal_time():
        if h == 0:
            time_str_list.append('twelve')
        elif 0 < h < 13:
            time_str_list.append(numerals(h))
        else:
            time_str_list.append(numerals(h-12))

        time_str_list.append(numerals(m))

        if h in [0,12]:
            if h == 0:
                time_str_list.append('ante meridiem')
            else:
                time_str_list.append('post meridiem')
        else:
            if 0 < h < 12:
                time_str_list.append('in the morning')
            elif h > 17:
                time_str_list.append('in the evening')
            else:
                time_str_list.append('in the afternoon')        


    if m == 0:
        if h in [0,12]:
            midnight_noon()
        x_oclock_in_the()

    elif 0 < m < 15:
        time_str_list.append(numerals(m))

        if m == 1:
            time_str_list.append('minute')
        else:
            time_str_list.append('minutes')

        time_str_list.append(rc(['past', 'after']))

        if h in [0,12]:
            midnight_noon()
        else:
            x_oclock_in_the()

    elif m == 15:
        time_str_list.append('quarter')
        time_str_list.append(rc(['past', 'after']))
        if h in [0,12]:
            midnight_noon()
        else:
            x_oclock_in_the()

    elif 15 < m < 30:
        normal_time()

    elif m == 30:
        time_str_list.append('half past')
        if h in [0,12]:
            midnight_noon()
        else:
            x_oclock_in_the()

    elif 30 < m < 45:
        normal_time()

    elif m == 45:
        time_str_list.append('quarter')
        time_str_list.append(rc(['to', 'until']))
        if h == 11:
            time_str_list.append('noon')
        elif h == 23:
            time_str_list.append('midnight')
        else:
            h += 1
            x_oclock_in_the()

    elif 45 < m < 50:
        normal_time()

    elif 50 <= m <= 59:
        time_str_list.append(numerals(60-m))

        if m == 59:
            time_str_list.append('minute')
        else:
            time_str_list.append('minutes')

        time_str_list.append(rc(['to', 'until']))

        if h == 11:
            time_str_list.append('noon')
        elif h == 23:
            time_str_list.append('midnight')
        else:
            h += 1
            x_oclock_in_the()

    return ' '.join(time_str_list)


class WordCamera(object):

    VALID_IMG = set(['jpg', 'jpeg', 'png'])

    def __init__(self, do_upload=False, img_orig_fp="", sentence_count=7, seed_ix=0, ebook_title="", ascii_img_path="", manual=False, looper=False, folderpath=""):
        self.first_pass = True

        # GPS STUFF

        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

        # END OF GPS STUFF

        # FOURSQUARE STUFF

        # Construct the client object
        # TODO: MOVE TO ENV VARIABLES
        self.client = foursquare.Foursquare(
            client_id=fs_api_keys.client_id,
            client_secret=fs_api_keys.client_secret,
            redirect_uri=fs_api_keys.redirect_uri
        )

        # Build the authorization url for your app
        self.auth_uri = self.client.oauth.auth_url()

        # END OF FOURSQUARE


        self.do_upload = do_upload
        self.img_orig_fp = img_orig_fp
        self.manual = manual
        # ebook of results?
        # self.ebook = ebook
        self.ebook_title = ebook_title

        self.folderpath = folderpath

        # ascii img path
        self.ascii_img_path = ascii_img_path

        # Connect to RabbitMQ
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()

        self.camera_ip = '10.0.0.2'
        self.camera_nums = [5,6,7,8]

        self.cur_cam = -1
        self.cur_hash = ""

        self.cur_exp = None



        possible_pre_seeds = [
            "The dreams of men who would regard the scene,\nThe sorrows of the morn, whose waters wave,\n",
            "~~~The arm of a person or thing and a frequency of a similar process within a postulated printed contest with the weapons of the post office.\n~|~",
            "The door opened and the old man turned in his armchair to see whether he had been to the river bank.\n"
        ]

        self.pre_seed = possible_pre_seeds[seed_ix]

        # Serial to Arduino button
        # self.ser = serial.Serial('/dev/ttyACM0')

        # Queue names
        queue_names = [
            'ImgPaths',
            'Captions',
            'CaptionToExpand',
            'Expansions'
        ]

        # Declare and Purge Queues
        for qn in queue_names:
            self.channel.queue_declare(queue=qn)
            self.channel.queue_purge(queue=qn)

        # HashIds
        self.hashids = Hashids()

        # Unused captions (changes every image)
        self.unused_captions = list()
        self.unused_captions_per_graf = 0

        # Class Variables
        self.sentence_count = sentence_count
        self.sentences = defaultdict(list)
        self.img_dest = '/home/rg/projects/wc3/img'
        self.template_path = '/home/rg/projects/wc3/template.html'
        self.ebook_template_path = '/home/rg/projects/wc3/ebook_template.html'

        self.thr1 = threading.Thread(target=self.consume)
        self.thr1.start()

        self.looper = looper
        self.gogogo = True

        if self.looper:
            if self.img_orig_fp:
                self.process_fp()
            else:
                self.thr2 = threading.Thread(target=self.loop)
                self.thr2.start()

        for i in range(len(self.camera_nums)):
            thr = threading.Thread(target=self.loop_generator(i))
            thr.start()

    def get_location_str(self):
        i = 0
        key_set = ['lat', 'lon', 'alt', 'speed']

        fancy_str = None


        for new_data in self.gps_socket:
            if new_data:
                i += 1
                try:
                    json_data = json.loads(new_data)
                except:
                    json_data = {}
                if not set(key_set) - set(json_data.keys()):
                    lat, lng, alt_meters, speed_kph = map(lambda x: json_data[x], key_set)
                    speed_mph = 0.621371 * speed_kph
                    alt_feet = 3.28084 * alt_meters
                    # return "", lat, lng, speed_mph, alt_feet
                    # break
                    
                    try:
                        response = self.client.venues.search(params={'ll': ','.join(map(str, [lat, lng]))})
                    except:
                        response = {}
                        
                    fancy_str = None
                        
                    if 'venues' in response:
                        venues = response['venues']
                        if venues:
                            v = rc(venues)
                            
                            loc_obj = v['location']
                            cats = v['categories']
                            if cats and 'city' in loc_obj:
                                c = cats[0]
                                fancy_str = v['name'] + ': ' 'a ' + c['name'].lower() + ' in ' + loc_obj['city']
                                return fancy_str, lat, lng, speed_mph, alt_feet
                    
            # if fancy_str:
            #     return fancy_str, lat, lng, alt_feet, speed_mph

            elif i > 9:
                try:
                    return "", lat, lng, alt_feet, speed_mph
                except:
                    return "(?)", 0, 0, 0, 0

        

    def process_fp(self):
        if self.img_orig_fp.rsplit('.').pop().strip().lower() in self.VALID_IMG:
            self.pre_narrate_individual(self.img_orig_fp)
        else:
            self.pre_narrate_folder()

    def pre_narrate_folder(self):
        for subdir, dirs, files in os.walk(self.img_orig_fp):
            for f in files:
                if f.rsplit('.', 1).pop().lower().strip() in self.VALID_IMG:
                    self.pre_narrate_individual(os.path.join(subdir, f))
    
    def pre_narrate_individual(self, fp):
        img_hash = self.hashids.encode(int(time.time()*1000))
        fn = "%s.jpg" % img_hash
        filepath = os.path.join(self.img_dest, fn)
        shutil.copy2(fp, filepath)
        self.narrate(filepath)  

    def loop_generator(self, cameraNo):
        def output_func():
            t = 0.0
            while 1:
                if cameraNo != self.cur_cam:
                    panVal = self.custom_pnoise(t,0+32*cameraNo)*180.0
                    tiltVal = abs(self.custom_pnoise(t,64+32*cameraNo)*90.0)
                    zoomVal = int(self.custom_pnoise(t,128+32*cameraNo)*5000+5000)
                    # print panVal, tiltVal, zoomVal
                    # print tiltVal
                    self.ptz(
                        camera=self.camera_nums[cameraNo],
                        pan=panVal,
                        tilt=tiltVal,
                        zoom=zoomVal
                    )
                time.sleep(0.01)
                t += 0.01
        return output_func

    def ptz(self, **kwargs):
        controlEndPt = 'http://%s/axis-cgi/com/ptz.cgi' % self.camera_ip
        requests.get(controlEndPt, params=kwargs)

    def custom_pnoise(self, tt, bb):
        return pnoise1(tt, base=bb, octaves=6, persistence=0.25, lacunarity=2.0)

    def loop(self):
        while 1:
            if self.gogogo:
                source_choice = ri(0,2)

                if self.cur_cam >= len(self.camera_nums)-1:
                    self.cur_cam = 0
                else:
                    self.cur_cam += 1
                # trigger = raw_input('Capture? ')
                # if trigger:
                if not self.first_pass:
                    time.sleep(ri(11,21))
                self.first_pass = False

                # camera
                if source_choice == 0:
                    self.cur_exp = 'camera'
                    self.capture(self.cur_cam)

                # clock
                else:
                    img_hash = self.hashids.encode
                    img_hash = self.hashids.encode(int(time.time()*1000))

                    simple_choice = ri(0,2)
                    if simple_choice == 0:
                        self.cur_exp = 'time'
                        print "EXPANDING TIME"

                        time_str = time_parse()

                    # elif simple_choice == 1:
                    #     self.cur_exp = 'audio'
                    #     print "EXPANDING AUDIO"

                    #     time_str = record(img_hash)

                    else:
                        self.cur_exp = 'location'
                        print "EXPANDING LOCATION"

                        time_str, lat, lng, alt, speed = self.get_location_str()
                    
                    if not time_str:
                        self.cur_exp = 'alt_speed'
                        print "EXPANDING ALT_SEED"

                        # _, lat, lng, alt, speed = self.get_location_str()

                        try:
                            components = tuple(map(str, [lat, lng, alt, speed]))
                            time_str = "%s N, %s W, at %s feet above sea level, at %s miles per hour" % components
                        except:
                            time_str = ""

                    thermal.line_print_mode()
                    thermal.feed_paper()

                    self.channel.basic_publish(
                        exchange = '',
                        routing_key = 'CaptionToExpand',
                        body = img_hash + '#' + self.pre_seed + time_str
                    )


                self.gogogo = False


            # curline = self.ser.readline().strip()
            # if curline == 'b':
            #     self.capture()
            # elif curline == 's':
            #     os.system('shutdown -h now')

    def process_folder(self, fp):
        self.folderpath = fp
        for subdir, dirs, files in os.walk(fp):
            for f in files:
                if f.endswith('.jpg'):
                    filepath = os.path.join(subdir, f)
                    img_hash = self.hashids.encode(int(time.time()*1000))
                    new_fp = os.path.join(self.img_dest, img_hash+'.jpg')
                    shutil.copy2(filepath, new_fp)
                    self.narrate(new_fp)
                    time.sleep(0.1)


    def capture(self, cameraNo):
        print "CAPTURING WITH CAMERA %i" % cameraNo
        img_hash = self.hashids.encode(int(time.time()*1000))
        fn = "%s.jpg" % img_hash
        filepath = os.path.join(self.img_dest, fn)
        # cmd_list = [
        #     'fswebcam', '-r', '640x480', '--jpeg', '100',
        #     '--no-banner', filepath
        # ]
        # proc = subprocess.Popen(cmd_list)
        # proc.communicate()

        endPt = "http://%s/axis-cgi/jpg/image.cgi" % self.camera_ip
        payload = {'camera': self.camera_nums[cameraNo]}
        res = requests.get(endPt, params=payload, stream=True)

        if res.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)

            # self.cur_cam = cameraNo

        #time.sleep(1)

        # Narrate
        return self.narrate(filepath)

    def img2txt(self, img_path):
        cmd_list = [
            '/usr/local/bin/img2txt.py', img_path, '--maxLen=80',
            '--targetAspect=0.4', '--bgcolor=#FFFFFF'
        ]
        proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE)
        result = proc.stdout.read()
        thermal.basic_print(result)

    def narrate(self, img_path):
        # Put printer in line print mode + feed paper
        thermal.line_print_mode()
        thermal.feed_paper()

        # Print ascii image
        if self.ascii_img_path:
            self.img2txt(self.ascii_img_path)
        else:
            self.img2txt(img_path)
        # self.img2txt()

        # Paper feed
        thermal.feed_paper()

        # Establish unique hash id for image
        img_hash = img_path.rsplit('/', 1).pop().rsplit('.', 1)[0]

        # Send img_path to densecap
        self.channel.basic_publish(
            exchange = '',
            routing_key = 'ImgPaths',
            body = img_hash + '#' + img_path
        )

        print img_hash
        return img_hash


    def approve(self, text):
        print('CANDIDATE: %s' % text)
        isApproved = raw_input('Approve? (y/n)\n')
        return isApproved and isApproved.strip().lower() != 'n'

    def consume(self):
        # Bind methods to consumption queues
        self.channel.basic_consume(self.process_captions, queue='Captions')
        self.channel.basic_consume(self.process_expansions, queue='Expansions')

        # Go
        self.channel.start_consuming()


    def process_captions(self, ch, method, properties, body):
        def int_to_enc(i):
            return "{0:b}".format(i).replace('0', '~').replace('1', '|')

        img_hash, csv = body.split('#', 1)

        print img_hash, "CAPTIONED"

        captions_raw = list(set(csv.split(',')))

        if self.manual or len(captions_raw) <= self.sentence_count:
            captions_cut = captions_raw
        else:
            captions_cut = rs(captions_raw, self.sentence_count)

        self.unused_captions = list(set(captions_raw) - set(captions_cut))
        self.unused_captions_per_graf = len(self.unused_captions) / self.sentence_count
        
        captions = map(
            # lambda (i, x): int_to_enc(i%8) + x[0].upper() + x[1:],
            lambda (i, x): x[0].upper() + x[1:],
            enumerate(captions_cut)
        )
        approved_captions = list()

        for c in captions:
            approved = True
            if self.manual:
                if len(approved_captions) > self.sentence_count:
                    approved = False
                else:
                    approved = self.approve(c)
            if approved:
                approved_captions.append(c)

        for c in approved_captions:
            self.channel.basic_publish(
                exchange = '',
                routing_key = 'CaptionToExpand',
                body = img_hash + '#' + self.pre_seed + c
            )

        # time.sleep(5)
        # self.channel.basic_publish(
        #     exchange = '',
        #     routing_key = 'Expansions',
        #     body = 'END#END'
        # )

    def process_expansions(self, ch, method, properties, body):
        img_hash, expansion = body.decode('utf8').split('#', 1)
        # print(expansion)

        expansion = expansion[len(self.pre_seed):]
        
        grafs = expansion.rsplit('\n', 1)

        if len(grafs) > 1:
            first_graf = '\n'.join(grafs[:-1])
        else:
            first_graf = grafs[0]

        first_graf = first_graf.replace('|', '').replace('~', '').replace('<UNK>', '(?)')

        def split_on_punc(punc, graf):
            complete_sents_no_punc, remainder = first_graf.rsplit(punc, 1)
            complete_sents = complete_sents_no_punc + punc.strip()
            return complete_sents[0].upper() + complete_sents[1:]

        result = None

        if len(grafs) > 1:
            result = first_graf[0].upper() + first_graf[1:]
            result = result.strip()
            if not result[-1] in set(['.', '!', '?', ',', ';', ':']):
                result += '.'
        elif '? ' in first_graf:
            result = split_on_punc('? ', first_graf)
        elif '! ' in first_graf:
            result = split_on_punc('! ', first_graf)
        elif '. ' in first_graf:
            result = split_on_punc('. ', first_graf)
        elif first_graf and first_graf[-1] in set(['.', '!', '?', ',', ';', ':']):
            result = first_graf[0].upper() + first_graf[1:]
        elif self.cur_exp != 'camera' or (self.looper and self.manual):
            result = first_graf[0].upper() + first_graf[1:] + '...'
        # else:
        #     result = first_graf[0].upper() + first_graf[1:].rstrip() + '...'

        # if self.unused_captions and rc([True, False, False, False, False]):
        #     graf_captions = list()
        #     for _ in range(self.unused_captions_per_graf):
        #         graf_captions.append( self.unused_captions.pop() )
        #     graf = ', '.join(graf_captions)
        #     self.sentences[img_hash].append( graf[0].upper() + graf[1:] + '.' )



        if self.looper:
            print "MAIN BLOCK RUNNING"

            approved = True

            if self.manual:
                approved = self.approve(result)

            if approved:
                print "APPEND RESULT TO SENTENCES"
                print result
                self.sentences[img_hash].append(result)
                print self.sentences[img_hash]
                thermal.thermal_print(result)
                thermal.line_break()
            else:
                self.sentences[img_hash].append("")

            if self.looper and (self.cur_exp != 'camera' or len(self.sentences[img_hash]) == self.sentence_count):
                self.publish(img_hash)


        print(img_hash, len(self.sentences[img_hash]))

    def get_text(self, img_hash):
        return ' '.join(self.sentences[img_hash])

    def change_sentence_count(self, new_count):
        self.sentence_count = new_count

    def publish(self, img_hash):
        if self.looper:
            self.gogogo = True

        approved_sents = filter(lambda x: x, self.sentences[img_hash])

        # now = str(datetime.now())
        # signature = 'wordcar by Ross Goodwin | %s' % now
        # thermal.line_break()
        # thermal.basic_print( '_'*len(signature) )
        # thermal.basic_print( signature )
        # thermal.line_break()
        # thermal.line_break()

        if self.do_upload:
            from upload_to_s3 import upload
        from string import Template
        # from datetime import datetime

        def chunks(l, n):
            """Yield successive n-sized chunks from l."""
            for i in range(0, len(l), n):
                yield l[i:i + n]

        with open(self.template_path, 'r') as infile:
            html_temp = Template(infile.read())

        img_fp = os.path.join(self.img_dest, img_hash+'.jpg')

        if self.do_upload:
            img_web_url = upload(img_fp)
        else:
            img_web_url = 'file://'+img_fp

        if approved_sents:
            last_line = approved_sents[-1].strip()

            if last_line:
                if last_line[-1] in set([',', ';', ':']):
                    approved_sents[-1] = last_line[:-1] + '.'
                elif not last_line[-1] in set(['.', '!', '?', ',', ';', ':']):
                    approved_sents[-1] = last_line + '.'



        body_text = '<p>%s</p>' % '</p><p>'.join(
            map(lambda x: '<br>'.join(x).replace('\n', '<br>'), list(chunks(approved_sents, 5)))
            # self.sentences[img_hash]
        )

        title = str(datetime.now()).split(' ', 1)[0] + '_' + img_hash

        html_str = html_temp.substitute(title=title, img_url=img_web_url, body=body_text)

        if self.folderpath:
            html_fn = os.path.join(self.folderpath, title+'.html')
        else:
            html_fn = os.path.join('/home/rg/projects/wc3/pages', title+'.html')

        with open(html_fn, 'w') as outfile:
            outfile.write(html_str.encode('utf8'))

        if self.do_upload:
            result_url = upload(html_fn)
            os.remove(html_fn)
        else:
            result_url = 'file://'+html_fn

        if not self.ebook_title:
            # webbrowser.open(result_url)
            # razer_rgb.scrolling_text(body_text.split(',', 1)[0], bg_color=(0,0,0), text_color=(255,255,255), speed=20, variety=64)
            return result_url
        else:
            return html_fn

    def publish_all(self):
        urls = map(self.publish, self.sentences.keys())
        if not self.ebook_title:
            for u in urls:
                print u
            return urls
        else:
            self.create_ebook(self.ebook_title, urls)

    def create_ebook(self, ebook_title, page_paths):
        from bs4 import BeautifulSoup
        from string import Template

        def get_file_text(fp):
            with open(fp) as f:
                soup = BeautifulSoup(f.read().strip())
            return str(soup.select('div.col-md-8')[0])

        ebook_html = '\n\n'.join(map(get_file_text, page_paths))

        with open(self.ebook_template_path, 'r') as infile:
            html_temp = Template(infile.read())

        ebook_html_text = html_temp.substitute(title=ebook_title, body=ebook_html)

        ebook_html_path = '/home/rg/projects/wc3/pages/ebook.html'
        ebook_output_path = '/home/rg/projects/wc3/pages/'+ebook_title+'.epub'

        with open(ebook_html_path, 'w') as outfile:
            outfile.write(ebook_html_text)

        proc = subprocess.Popen(['ebook-convert', ebook_html_path, ebook_output_path])
        proc.communicate()

        print ebook_output_path

        return ebook_output_path

        # os.remove(ebook_html_path)



    # def process_folder(self, folderpath):
    #     for root, dirs, files in os.walk(folderpath):
    #         for f in files:
    #             if f.endswith('.jpg'):
    #                 img_path = os.path.join(root, f)
    #                 print img_path
    #                 self.narrate(img_path)
    #                 time.sleep(0.1)


num_sents, seed_id = map(int, sys.argv[1:3])

allowed_ext = set(['tif', 'tiff', 'png', 'jpg', 'jpeg'])

if len(sys.argv) > 3:
    fp = sys.argv[3]
    # fp_ext = fp.rsplit('.', 1).pop().lower()
    # if fp_ext in allowed_ext:
        # if image file
    wc = WordCamera(img_orig_fp=fp, sentence_count=num_sents, seed_ix=seed_id, manual=True, looper=True)
    # else:

        # if folder
        # cameras = list()
    #     wc = False
    #     for subdir, dirs, files in os.walk(fp):
    #         for f in files:
    #             f_ext = f.rsplit('.', 1).pop().lower()
    #             if f_ext in allowed_ext:
    #                 img_fp = os.path.join(subdir, f)
    #                 if not wc:
    #                     wc = WordCamera(img_orig_fp=img_fp, sentence_count=num_sents, seed_ix=seed_id, manual=False, looper=True, folderpath=subdir)
    #                 else:

    #                 time.sleep(1.5)
    # # with open('big_picture_2016/page_paths.txt') as infile:
    #     filepaths = filter(lambda y: y, map(lambda x: x.strip(), infile.read().strip().split('\n')))
    # wc.create_ebook(sys.argv[4], filepaths)
else:
    wc = WordCamera(sentence_count=num_sents, seed_ix=seed_id, manual=False, looper=True)

# if len(sys.argv) > 3:
#     folderpath = sys.argv[3]
#     wc.process_folder(folderpath)

#     trigger = raw_input('Publish? ')
#     if trigger:
#         wc.publish_all()
# else:
#     wc = WordCamera(sentence_count=num_sents, seed_ix=seed_id, manual=True, looper=True)
        

        # time.sleep(num_sents*3)

        # razer_rgb.write_to_file('brightness', '255')
        # razer_rgb.perlin_noise(secs=num_sents*3)

        # wc.publish(imghash)

