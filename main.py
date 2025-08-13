import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
from random import randint

# ===== Diretórios =====
diretorio_principal = os.path.dirname(__file__)  # Diretório do arquivo atual
diretorio_imagens = os.path.join(diretorio_principal, "imagens")  # Pasta das imagens
diretorio_sons = os.path.join(diretorio_principal, "sons")        # Pasta dos sons

# ===== Configurações =====
largura = 1280   # largura da janela do jogo
altura = 720     # altura da janela do jogo

# Caminho da música (uma pasta acima, dentro da pasta 'audio')
base_path = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(base_path, "..", "audio", "FaseUm.mp3")

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

# ===== Sprite da Galinha =====
sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "chicken.png")).convert_alpha()

class Galinha(pygame.sprite.Sprite):
    """Classe que representa a galinha animada."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_galinha = []
        for i in range(4): # Recorta os frames do sprite e aumenta o tamanho da galinha
            img = sprite_sheet.subsurface((i * 64, 0), (64, 64))
            img = pygame.transform.scale(img, (64*3, 64*3))
            self.imagens_galinha.append(img)
        
        self.index_lista = 0
        self.image = self.imagens_galinha[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, altura - 130)  # posição inicial da galinha


    def update(self):
        """Atualiza o frame da animação da galinha."""
        self.index_lista += 0.25
        if self.index_lista > 3: # 3 é o último índice da lista de imagens_galinha
            self.index_lista = 0
        self.image = self.imagens_galinha[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        imagem_original = pygame.image.load(os.path.join(diretorio_imagens, "nuvem.png")).convert_alpha()
        # Redimensiona a imagem para o tamanho desejado
        self.image = pygame.transform.scale(imagem_original, (150, 90))  # <- aqui, use self.image
        self.rect = self.image.get_rect()
        self.rect.y = randint(30, 300) # sorteio de posição aleatória (na vertical) no intervalo descrito
        self.rect.x = randrange(largura, largura + 600) # sorteio de posição inicial (na horizontal) para que as nuvens não apareçam todas juntas no início

    def update(self):
        """Atualiza a posição da nuvem."""
        if self.rect.topright[0] < 0:  # Se a nuvem sair da tela, reinicia a posição - tento como referencia o canto direito da imagem, para que o movimento fique mais natural
            self.rect.x = largura
            self.rect.y = randrange(50, 200, 50) # sempre que as nuvens ultrapassarem a borda esquerda da tela, haverá um novo sorteio das posições verticais
        self.rect.x -= 6 # Move a nuvem na posição x, na velocidade 6 


# ===== Grupo de sprites =====
todas_as_sprites = pygame.sprite.Group()
galinha = Galinha()
todas_as_sprites.add(galinha)

for i in range(4):
    nuvem = Nuvens()  
    todas_as_sprites.add(nuvem)  

# ===== Loop Principal =====
relogio = pygame.time.Clock()  # controla a taxa de frames por segundo
while True:
    relogio.tick(30)  # limita a 30 FPS
    # Desenha o fundo (pode usar fill para cor sólida, mas aqui usa a imagem)
    tela.blit(fundo, (0, 0))

    # Captura os eventos do jogo (fechar janela, etc)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Atualiza e desenha todos os sprites na tela
    todas_as_sprites.update()
    todas_as_sprites.draw(tela)

    pygame.display.flip()  # atualiza o display
