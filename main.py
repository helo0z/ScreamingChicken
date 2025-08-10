import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

icon = pygame.image.load("chicken.jpeg")
pygame.display.set_icon(icon)
pygame.display.set_caption("Screaming Chicken")

while True: #loop principal do jogo, todo o script do jogo devera está aqui dentro
    for event in pygame.event.get(): #detectar se algum evento ocorreu
        if event.type == QUIT: #se o evento for fechar jogo
            pygame.quit()
            exit()

    pygame.display.update() #a cada interacao do loop principal do jogo, essa linha atualiza o jogo (loop infinito)