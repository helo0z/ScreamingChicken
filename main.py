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
        
        # --- Carregamento de Imagens (Dentro da classe para evitar erros) ---
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
                img_redim = pygame.transform.scale(img, (64*2, 64*2.5))
                self.imagens_galinha.append(img_redim)

        except Exception as e:
            print(f"ERRO CRÍTICO: Não foi possível carregar a galinha. Detalhes: {e}")
            # Se der erro, cria um quadrado vermelho para você ver onde ela está
            surf = pygame.Surface((100, 100))
            surf.fill(VERMELHO_ERRO)
            self.imagens_galinha.append(surf)
        
        # Inicialização da Animação
        self.index_lista = 0
        self.image = self.imagens_galinha[self.index_lista]
        self.rect = self.image.get_rect()
        
        self.pos_y_inicial = altura - 125 - 192//2
        self.rect.center = (200, altura - 40)
        self.pulo = False

    def pular(self):
        self.pulo = True
        if self.som_pulo:
            self.som_pulo.play()
        
    def update(self):
        # Lógica do Pulo
        if self.pulo:
            if self.rect.y <= 300:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_inicial

        # Lógica da Animação
        self.index_lista += 0.37
        indice = int(self.index_lista)
        if indice >= len(self.imagens_galinha):
            indice = 0
            self.index_lista = 0
        self.image = self.imagens_galinha[indice]


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

    def update(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.x = largura + randint(500, 900)
            self.rect.bottom = altura - 16


# ===== Loop Principal =====
def main(skin_escolhida=0): # Recebe o argumento para evitar o erro TypeError
    
    # Reinicia configurações de tela
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
        caminho_musica = os.path.join(diretorio_sons, "FaseUm.mp3") # Usando diretorio_sons que definimos lá em cima
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(1) 
        pygame.mixer.music.play(-1) 
    except Exception as e:
        print(f"Erro música: {e}")

    # Carrega Fundo
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

    # --- CRIA A GALINHA ---
    # Nota: No futuro, você usará 'skin_escolhida' aqui para decidir qual imagem carregar
    galinha = Galinha() 
    todas_as_sprites.add(galinha)

    # Nuvens
    for i in range(4):
        nuvem = Nuvens()  
        todas_as_sprites.add(nuvem)  

    # Pisos
    largura_piso = 150
    num_pisos = math.ceil(largura * 2 / largura_piso)  
    for i in range(num_pisos):
        piso = Piso(i)
        todas_as_sprites.add(piso)

    # Obstáculos
    obstaculos = pygame.sprite.Group()
    posicoes_usadas = []

    for i in range(3):
        indice = randint(0, 2)
        obst = Obstaculos(indice)
        if i == 0:
            obst.rect.x = largura + randint(300, 600)
        else:
            obst.rect.x = posicoes_usadas[-1] + randint(400, 700) 

        obstaculos.add(obst)
        todas_as_sprites.add(obst)
        posicoes_usadas.append(obst.rect.x)

    relogio = pygame.time.Clock()  
    inicio = datetime.now()
    
    rodando = True
    while rodando:
        relogio.tick(30) 
        
        # Desenha fundo
        tela.blit(fundo, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
            # Tecla ESC para voltar ao menu (opcional) ou fechar
            # if event.type == KEYDOWN and event.key == K_ESCAPE:
            #     rodando = False 

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if galinha.rect.y != galinha.pos_y_inicial:
                        pass
                    else:
                        galinha.pular()
        
        todas_as_sprites.update()
        todas_as_sprites.draw(tela)
        
        # Troca de Fundo (Timer)
        fim = datetime.now()
        tempo_passado = (fim - inicio).seconds
        if tempo_passado >= 3:
            novo_fundo = None
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
                fundo_original = pygame.image.load(os.path.join(diretorio_imagens, nome_fundo))
                fundo = pygame.transform.scale(fundo_original, (largura, altura))
            except: pass # Mantém o fundo anterior se der erro
            
            inicio = datetime.now() 
                
        pygame.display.flip()

if __name__ == "__main__":
    main(0)