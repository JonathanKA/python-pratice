#ex021 play a mp3 file
import pygame
# pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021_Luna Haruna - Overfly.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#algum bug, unico codigo que funcionou.
# from pygame import mixer, event
# mixer.init()
# mixer.music.load('ex021_Luna Haruna - Overfly.mp3')
# mixer.music.play()
# event.wait()
# input()
