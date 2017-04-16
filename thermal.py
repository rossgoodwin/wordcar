import subprocess
import serial
import string
import os
import time

ser = serial.Serial('/dev/ttyUSB1')
ser.write(b'{LP}')


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def split_to_lines(text, ll=80):
    if not text:
        return ""
    text_list = filter(
        lambda x: x in string.printable,
        list(text.strip())
    )
    char_count = 0
    ws_indexes = list()
    cur_line = list()
    all_lines = list()
    i = 0
    start_ix = 0
    while i < len(text_list):
        c = text_list[i]
#         print c
        if c in [' ', '\t']:
            ws_indexes.append(i)
        
        cur_line.append(c)        
        char_count += 1
            
        if c == '\n':
            cur_line = text_list[start_ix:i]
            start_ix = i
            all_lines.append(''.join(cur_line))
            
            cur_line = list()
            char_count = 0
            
        elif char_count >= ll:
            tgt_ix = ws_indexes.pop()
            cur_line = text_list[start_ix:tgt_ix]
            i = tgt_ix
            start_ix = i
            all_lines.append(''.join(cur_line))
            
            cur_line = list()
            char_count = 0
            
        i += 1
    
    all_lines.append(''.join(cur_line))
    return map(lambda x: x.strip(), all_lines)

def line_print_mode():
    ser.write(b'{LP}')

def feed_paper():
    ser.write(b'\n'*4)

def line_break():
    ser.write(b'\n')

def basic_print(text):
    ser.write(b'\n')
    ser.write(bytes(text))
    time.sleep(0.5)

def thermal_print(text):
    font_switch = chr(27) + b'!4'
    for l in split_to_lines(text, ll=38):
        ser.write(font_switch)
        ser.write(b'  '+bytes(l))
        ser.write(b'\n')
        time.sleep(0.5)

