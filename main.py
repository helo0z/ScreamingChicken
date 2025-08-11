import pygame
from pygame.locals import *
from sys import exit
import os

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

# --------- Configurações ---------
largura = 1280         # largura da janela do jogo
altura = 720           # altura da janela do jogo
FPS = 60               # frames por segundo (velocidade do loop)

# Caminho da música (está uma pasta acima, dentro da pasta 'audio')
base_path = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(base_path, "..", "audio", "FaseUm.mp3")

# Cores usadas no jogo
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 0)  # amarelo para destacar os botões

# Inicializa todos os módulos do pygame (exceto mixer que será inicializado no menu)
pygame.init()

# Caminho do ícone (volta uma pasta e acessa teste.png)
icon_path = os.path.join(os.path.dirname(__file__), "imagens", "chickenjanela.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
pygame.display.set_caption("Screaming Chicken")

# Fonte usada nos botões: Comic Sans MS, tamanho 48, itálico e negrito
FONT_BUTTON = pygame.font.SysFont("comicsansms", 48, italic=True, bold=True)

# Cria a janela do jogo com o tamanho definido
tela = pygame.display.set_mode((largura, altura))

# Carrega a imagem de fundo do menu e ajusta para o tamanho da janela
caminho_fundo = os.path.join(os.path.dirname(__file__), "imagens", "FundoUm.jpeg")
fundo_original = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo_original, (largura, altura))

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "chicken.png")).convert_alpha()


class Galinha(pygame.sprite.Sprite): #sprite da galinha
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_galinha = []
        for i in range(4):
            img = sprite_sheet.subsurface((i * 64, 0), (64, 64))
            img = pygame.transform.scale(img, (64*3, 64*3)) #aumentando o tamanho da galinha
            self.imagens_galinha.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_galinha[self.index_lista]
        self.rect = self.image.get_rect() 
        self.rect.center = (100, 100)

    def update(self): #loop das sprites da galinha
        if self.index_lista > 3: #3 é o indece do ultimo elemento da lista imagens_galinha
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_galinha[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite)
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



todas_as_sprites = pygame.sprite.Group()
galinha = Galinha()
todas_as_sprites.add(galinha)

relogio = pygame.time.Clock() #relogio que controla a taxa de frems por segundo
while True: #loop principal do jogo, todo o script do jogo devera está aqui dentro
    relogio.tick(30)
    tela.fill(WHITE)
    for event in pygame.event.get(): #detectar se algum evento ocorreu
        if event.type == QUIT: #se o evento for fechar jogo
            pygame.quit()
            exit()

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()