import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, randint
import math
#comentario

pygame.init()
pygame.mixer.init()

# ===== Diretórios =====
diretorio_principal = os.path.dirname(__file__)  # Diretório do arquivo atual
diretorio_imagens = os.path.join(diretorio_principal, "imagens")  # Pasta das imagens
diretorio_sons = os.path.join(diretorio_principal, "audio")        # Pasta dos sons

# ===== Configurações =====
largura = 1280   # largura da janela do jogo
altura = 720     # altura da janela do jogo

# Caminho da música (uma pasta acima, dentro da pasta 'audio')
base_path = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(base_path, "audio", "FaseUm.mp3")

# ===== Cores =====
WHITE = (255, 255, 255)           # branco
BLACK = (0, 0, 0)                 # preto
HIGHLIGHT = (255, 255, 0)         # amarelo para destaque (exemplo de cor extra)

# ===== Inicialização do Pygame =====
pygame.init()  # inicializa todos os módulos do pygame (exceto mixer que será inicializado separadamente)

# ===== Ícone e título da janela =====
icon_path = os.path.join(diretorio_imagens, "chickenjanela.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
pygame.display.set_caption("Screaming Chicken")

# ===== Fonte =====
FONT_BUTTON = pygame.font.SysFont("comicsansms", 48, italic=True, bold=True)

# ===== Janela do jogo (fixa com tamanho definido) =====
tela = pygame.display.set_mode((largura, altura))  

# ===== Fundo (Carrega a imagem de fundo e ajusta para o tamanho da janela) =====
caminho_fundo = os.path.join(diretorio_imagens, "FundoUm.jpeg")
fundo_original = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo_original, (largura, altura))  # escala a imagem do fundo uma única vez

# ===== Carregar e tocar música de fundo em loop =====
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.set_volume(0.024)  # volume entre 0 e 1
pygame.mixer.music.play(-1)  # loop infinito

# ===== Sprite da Galinha =====
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "chicken.png")).convert_alpha()

class Galinha(pygame.sprite.Sprite):
    """Classe que representa a galinha animada."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "pulo.mp3"))
        self.som_pulo.set_volume(1)
        self.imagens_galinha = []
        for i in range(4): # Recorta os frames do sprite e aumenta o tamanho da galinha
            img = sprite_sheet.subsurface((i * 64, 0), (64, 64))
            img = pygame.transform.scale(img, (64*3, 64*3))
            self.imagens_galinha.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_galinha[self.index_lista]
        self.rect = self.image.get_rect() #retangulo ao redor do objeto (galinha)
        self.pos_y_inicial = altura - 129 - 192//2
        self.rect.center = (200, altura - 129)  # posição inicial da galinha (já acima do piso)
        self.pulo = False  # controle de pulo

    def pular(self):
        """Faz a galinha pular."""
        self.pulo = True
        self.som_pulo.play()
        
    def update(self):
        """Atualiza o frame da animação da galinha."""
        if self.pulo == True:
            if self.rect.y <= 300:
                self.pulo = False # galinha parou de subir
            self.rect.y -= 20  # move a galinha para cima ao pular
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        if self.index_lista > 3: # 3 é o último índice da lista de imagens_galinha
            self.index_lista = 0
        self.index_lista += 0.25  # controla a velocidade da animação
        self.image = self.imagens_galinha[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        imagem_original = pygame.image.load(os.path.join(diretorio_imagens, "nuvem.png")).convert_alpha()
        self.image = pygame.transform.scale(imagem_original, (150, 90))  
        self.rect = self.image.get_rect()
        self.rect.y = randint(10, 150) # sorteio de posição aleatória (na vertical) no intervalo descrito
        self.rect.x = randrange(largura, largura + 600) 

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura + randrange(150, 500, 50)
            self.rect.y = randrange(10, 140, 10)
        self.rect.x -= 7


class Piso(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        imagem_original = pygame.image.load(os.path.join(diretorio_imagens, "piso.jpg")).convert_alpha()
        self.image = pygame.transform.scale(imagem_original, (150, 90))
        self.rect = self.image.get_rect()  
        self.rect.y = altura - 64
        self.rect.x = pos_x * 150

    def update(self):
        if self.rect.topright[0] < 0: 
            self.rect.x = largura
        self.rect.x -= 10


sprite_sheet_arbusto = pygame.image.load(os.path.join(diretorio_imagens, "arbusto.png")).convert_alpha()

class Arbusto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_arbusto = []
        for i in range(9):
            img = sprite_sheet_arbusto.subsurface((i * 16, 0), (16, 16))
            img = pygame.transform.scale(img, (64, 64))  # aumenta o tamanho
            self.imagens_arbusto.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_arbusto[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (largura - 100, altura - 129)  # já começa visível

    def update(self):
        if self.index_lista > 8:  # já que temos 9 frames
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_arbusto[int(self.index_lista)]

        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 10

        
# ===== Grupo de sprites =====
todas_as_sprites = pygame.sprite.Group()

galinha = Galinha()
todas_as_sprites.add(galinha)

for i in range(4):
    nuvem = Nuvens()  
    todas_as_sprites.add(nuvem)  

largura_piso = 150
num_pisos = math.ceil(largura * 2 / largura_piso)  # garante que preencha toda a largura

for i in range(num_pisos):
    piso = Piso(i)
    todas_as_sprites.add(piso)

arbusto = Arbusto()
todas_as_sprites.add(arbusto)

# ===== Loop Principal =====
relogio = pygame.time.Clock()  
while True:
    relogio.tick(30)  # limita a 30 FPS
    tela.blit(fundo, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if galinha.rect.y != galinha.pos_y_inicial:
                    pass
                else:
                    galinha.pular()

    todas_as_sprites.update()
    todas_as_sprites.draw(tela)

    pygame.display.flip()
