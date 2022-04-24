import pygame

pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
print("Escuta ai esse som")
input("Ta gostando?")
pygame.event.wait()
