#Faça um programa em python que reproduza o audio em um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load('ex1.mp3')
pygame.mixer.music.play()
pygame.event.wait()