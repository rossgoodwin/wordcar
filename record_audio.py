import pyaudio
import wave
import subprocess
import os
# from hashids import Hashids

ROOT_AUDIO_FOLDER = '/home/rg/projects/wc3/audio'

def record(hashid):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 16
    WAVE_OUTPUT_FILENAME = os.path.join(ROOT_AUDIO_FOLDER, "output.wav")

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    mp3_output_fp = os.path.join(ROOT_AUDIO_FOLDER, hashid+'.mp3')

    proc = subprocess.Popen(['ffmpeg', '-i', WAVE_OUTPUT_FILENAME, mp3_output_fp])
    proc.communicate()

    proc2 = subprocess.Popen(['audiogrep', '--input', mp3_output_fp, '--transcribe'])
    proc2.communicate()

    with open(mp3_output_fp+'.transcription.txt') as infile:
        transcript = infile.read().strip().split('\n')[0]

    return transcript[0].upper() + transcript[1:]
