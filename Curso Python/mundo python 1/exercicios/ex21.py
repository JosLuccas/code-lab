# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# Na atual versão que uso do python, não tem suporte para pygame

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("musica.mp3")
pygame.mixer.music.play()

input("Pressione ENTER para encerrar...")
