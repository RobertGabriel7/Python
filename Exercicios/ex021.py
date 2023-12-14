import pygame

#para iniciar o pygame

pygame.init()
pygame.mixer.init()

#Para carregar o arquivo da musica

pygame.mixer.music.load('C:\\xampp\\htdocs\\Aulas\\Python\\Exercicios\\louvor1.mp3')


pygame.mixer.music.play()

