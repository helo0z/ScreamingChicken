import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, randint
import math
from datetime import datetime

# ===== Inicialização =====
pygame.init()
pygame.mixer.init()

# ===== Configurações e Diretórios =====
largura = 1280
altura = 720

# Garante que o caminho base seja onde este arquivo está
base_path = os.path.dirname(os.path.abspath(__file__))
diretorio_imagens = os.path.join(base_path, "imagens")
diretorio_sons = os.path.join(base_path, "audio")

# ===== Cores =====
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO_ERRO = (255, 0, 0) # Para identificar se a imagem falhar

# ===== CLASSES =====

class Galinha(pygame.sprite.Sprite):
    """Classe que representa a galinha animada."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        # --- Carregamento de Som ---
        try:
            self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, "pulo.mp3"))
            self.som_pulo.set_volume(1)
        except:
            print("Aviso: Som de pulo não encontrado.")
            self.som_pulo = None
        
        # --- Carregamento de Imagens ---
        self.imagens_galinha = []
        
        try:
            # Carrega frames 1 a 5
            frames = []
            for i in range(1, 6):
                caminho_img = os.path.join(diretorio_imagens, f"galinha{i}.png")
                img = pygame.image.load(caminho_img).convert_alpha()
                frames.append(img)
            
            # Cria a animação de ida e volta (1,2,3,4,5,4,3,2...)
            sprite_sheet = frames + frames[-2:0:-1]

            # Escala as imagens
            for img in sprite_sheet:
                # Ajustado para manter a proporção original que você definiu
                img_redim = pygame.transform.scale(img, (64*2, 64*2.5))
                self.imagens_galinha.append(img_redim)

        except Exception as e:
            print(f"ERRO CRÍTICO: Não foi possível carregar a galinha. Detalhes: {e}")
            surf = pygame.Surface((100, 100))
            surf.fill(VERMELHO_ERRO)
            self.imagens_galinha.append(surf)
        
        # Inicialização da Animação
        self.index_lista = 0
        self.image = self.imagens_galinha[self.index_lista]
        self.rect = self.image.get_rect()
        
        # Ajuste fino da posição Y para tocar o chão corretamente
        self.pos_y_inicial = altura - 102 - (64*2.5) + 40
        self.rect.center = (200, self.pos_y_inicial)
        
        self.pulo = False
        self.mask = pygame.mask.from_surface(self.image)

    def pular(self):
        self.pulo = True
        if self.som_pulo:
            self.som_pulo.play()
        
    def update(self):
        # Lógica do Pulo
        if self.pulo:
            if self.rect.y <= 250: # Altura do pulo
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        # Lógica da Animação
        self.index_lista += 0.35 # Velocidade da batida de asas
        indice = int(self.index_lista)
        if indice >= len(self.imagens_galinha):
            indice = 0
            self.index_lista = 0
        self.image = self.imagens_galinha[indice]
        self.mask = pygame.mask.from_surface(self.image)


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        try:
            imagem_original = pygame.image.load(os.path.join(diretorio_imagens, "nuvem.png")).convert_alpha()
            self.image = pygame.transform.scale(imagem_original, (150, 90))
        except:
            self.image = pygame.Surface((150, 90))
            self.image.fill(WHITE)
            
        self.rect = self.image.get_rect()
        self.rect.y = randint(10, 150)
        self.rect.x = randrange(largura, largura + 600) 

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura + randrange(150, 500, 50)
            self.rect.y = randrange(10, 140, 10)
        self.rect.x -= 7

class Piso(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        try:
            imagem_original = pygame.image.load(os.path.join(diretorio_imagens, "piso.png")).convert_alpha()
            self.image = pygame.transform.scale(imagem_original, (100, 150))
        except:
            self.image = pygame.Surface((100, 150))
            self.image.fill((100, 100, 100))

        self.rect = self.image.get_rect()  
        self.rect.y = altura - 150
        self.rect.x = pos_x * 80

    def update(self):
        if self.rect.topright[0] < 0: 
            self.rect.x = largura
        self.rect.x -= 10

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self, indice: int):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens_obstaculos = []
        try:
            lista_imgs = ["arbusto.png", "cerca.png", "espantalho.png"]
            for nome in lista_imgs:
                img = pygame.image.load(os.path.join(diretorio_imagens, nome)).convert_alpha()
                self.imagens_obstaculos.append(img)
            
            self.image = pygame.transform.scale(self.imagens_obstaculos[indice], (170, 160))
        except:
            self.image = pygame.Surface((100, 100))
            self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.bottom = altura - 15
        self.rect.x = largura + randint(200, 800)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.x = largura + randint(200, 600)
            self.rect.bottom = altura - 15


# ===== Loop Principal =====
def main(skin_escolhida=0):
    
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Screaming Chicken")
    
    # Carrega Ícone
    try:
        icon_path = os.path.join(diretorio_imagens, "chickenjanela.png")
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
    except: pass

    # Carrega Música
    try:
        caminho_musica = os.path.join(diretorio_sons, "FaseUm.mp3")
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(-1) 
    except Exception as e:
        print(f"Erro música: {e}")

    # Carrega Fundo Inicial
    img_fundo = 1 
    try:
        caminho_fundo = os.path.join(diretorio_imagens, "FundoUm.jpeg")
        fundo_original = pygame.image.load(caminho_fundo)
        fundo = pygame.transform.scale(fundo_original, (largura, altura))
    except:
        fundo = pygame.Surface((largura, altura))
        fundo.fill((135, 206, 235))
    
    # Grupos
    todas_as_sprites = pygame.sprite.Group()
    obstaculos = pygame.sprite.Group()

    # --- CRIA A GALINHA ---
    galinha = Galinha() 
    todas_as_sprites.add(galinha)

    # Nuvens
    for i in range(4):
        nuvem = Nuvens()  
        todas_as_sprites.add(nuvem)  

    # Pisos
    largura_piso = 80
    num_pisos = math.ceil(largura * 2 / largura_piso)  
    for i in range(num_pisos):
        piso = Piso(i)
        todas_as_sprites.add(piso)

    # Obstáculos
    distancia_minima = 400 

    for i in range(3):
        indice = randint(0, 2)
        obst = Obstaculos(indice)
        obst.rect.x = largura + (i * distancia_minima) + randint(100, 300)
        obstaculos.add(obst)
        todas_as_sprites.add(obst)

    relogio = pygame.time.Clock()  
    inicio = datetime.now()
    
    fundo_atual = fundo
    fundo_proximo = None
    alpha_fundo = 255
    transicionando = False
    rodando = True

    while rodando:
        relogio.tick(30) 
        
        # --- LÓGICA DE DESENHO DO FUNDO ---
        tela.blit(fundo_atual, (0, 0)) 
        
        if transicionando and fundo_proximo:
            alpha_fundo += 15
            fundo_proximo.set_alpha(alpha_fundo)
            tela.blit(fundo_proximo, (0, 0)) 
            
            if alpha_fundo >= 255:
                fundo_atual = fundo_proximo
                transicionando = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if galinha.rect.y >= galinha.pos_y_inicial - 10: # Pequena margem de erro
                        galinha.pular()

        # --- LÓGICA DE TROCA DE FUNDO ---
        fim = datetime.now()
        tempo_passado = (fim - inicio).seconds
        
        if tempo_passado >= 10 and not transicionando:
            if img_fundo == 1:
                img_fundo = 2
                nome_fundo = "FundoDois.jpeg"
            elif img_fundo == 2:
                img_fundo = 3
                nome_fundo = "FundoTres.jpeg"
            else:
                img_fundo = 1
                nome_fundo = "FundoUm.jpeg"
            
            try:
                caminho_fundo = os.path.join(diretorio_imagens, nome_fundo)
                prox_img = pygame.image.load(caminho_fundo).convert()
                fundo_proximo = pygame.transform.scale(prox_img, (largura, altura))
                alpha_fundo = 0
                transicionando = True
            except: 
                pass
            
            inicio = datetime.now() 

        # --- UPDATE ÚNICO ---
        todas_as_sprites.update()

        # --- LÓGICA DE COLISÃO ---
        colisoes = pygame.sprite.spritecollide(galinha, obstaculos, False, pygame.sprite.collide_mask)

        if colisoes:
            print("GAME OVER! A galinha colidiu.")
            rodando = False 

        # --- DESENHO FINAL ---
        todas_as_sprites.draw(tela)
        pygame.display.flip()

if __name__ == "__main__":
    main(0)