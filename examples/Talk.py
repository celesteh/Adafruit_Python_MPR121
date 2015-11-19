#!/usr/bin/python

import sys
import time, math, random, threading, glob

#import pygame
import subprocess as sp
from os import environ


import Adafruit_MPR121.MPR121 as MPR121


cap = MPR121.MPR121()


if not cap.begin():
    print ('Error: Did you forget to sudo? If no, Must Reboot')
    sys.exit(1)

env =environ.copy()
env['AUDIODEV'] = 'front:CARD=Device,DEV=0'

#pygame.init()
#pygame.mixer.init()
#pygame.mixer.set_num_channels(1)
#sfx = pygame.mixer.Channel(0)

sfxFiles = glob.glob("audio/*.wav") #Sorry, not including the audio on github
nSFX = len(sfxFiles)
last = random.randrange(0, (nSFX-1))
text = sfxFiles[last]
#while (pygame.mixer.get_init() == None):
#    print('waiting')
#    time.sleep(0.2)
#text = pygame.mixer.music.load(sfxFiles[nextt])
#print(nSFX, text, sfxFiles)


last_touched = cap.is_touched(1) or cap.is_touched(2)
while True:
    current_touched = cap.is_touched(1) or cap.is_touched(2)
    #pygame.event.pump()
    #pin_bit = 1 << 1
    # First check if transitioned from not touched to touched.
    if current_touched and (not last_touched):
        #print '{0} touched!'.format(i)
        #if( not sfx.get_busy()):
        #    time.sleep(0.4)
            #sfx.play(text)
            #text.play()
        #    print(sfxFiles[nextt])
        #    pygame.mixer.music.load(sfxFiles[nextt])
        #    pygame.mixer.music.play()
            #print(text.get_volume())
        #    nextt = last
        #    while ((nSFX > 1) and (nextt != last)):
        #        nextt = random.randrange(0, (nSFX-1))
            #text = pygame.mixer.Sound(sfxFiles[nextt])
        #    last = nextt
        print("playing")
        sp.call(['play', text], env=env)
        nextt=last
        while ((nSFX > 1) and (nextt == last)):
            nextt = random.randrange(0, (nSFX-1))
            
        text = sfxFiles[nextt]
        last=nextt
    # Next check if transitioned from touched to not touched.
    #if not current_touched & pin_bit and last_touched & pin_bit:
        #print '{0} released!'.format(i)
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.1)