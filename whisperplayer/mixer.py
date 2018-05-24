'''
Created on May 12, 2018

@author: spark
'''
import pygame
from pygame.mixer import *
import random


class mixer(object):
    '''
    classdocs
    '''

    def __init__(self):
        #
        #---PYGAME SOUNDS---------
        #
        self._buf = 307200
        pygame.mixer.quit()
        #init pygame mixer if needed--------------
        if pygame.mixer.get_init() == None:
            pygame.mixer.pre_init(44100, -16, 2, self._buf)
            pygame.mixer.init()
        # audio params, time in ms
        self.fadeTime = 4000
        self.fx_vol = 1.0

    def play_sound(self, sounds):
        self.soundpath = str(random.choice(sounds))
        try:
            self.this_sound = pygame.mixer.Sound(self.soundpath)
            self.this_sound.play(0, 0, 12)

            msg = ('Playing for {} seconds:\n{}')
            print(msg.format(
                         round(self.this_sound.get_length(), 2),
                         self.this_sound))

        except:
            print('Failed to play sound file')

    def stop_sound(self, fade=1000):
        try:
            pygame.mixer.fadeout(fade)
            while pygame.mixer.get_busy():
                pygame.time.wait(10)
            return 0
        except Exception:
            return 1
    
    def load_music(self, path):
        try:
            pygame.mixer.music.load(path)
            return 0
        except Exception:
            print(('Failed to load music file\n{}').format(path))
            return 1
    
    def play_music(self):
        pygame.mixer.music.play(loops=-1, start=0_0)
        
    def pause_music(self):
        pygame.mixer.music.pause()
        
    def unpause_music(self):
        pygame.mixer.music.unpause()
        
    def stop_music(self):
        pygame.mixer.music.stop()    
    
    def get_music_busy(self):
        return pygame.mixer.music.get_busy()

    def pywait(self, mils):
        pygame.time.wait(mils)
        return 0
