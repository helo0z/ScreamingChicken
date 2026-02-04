import pygame
import sys
import os
from main import main
from opcoes import abrir_opcoes

# --------- Configurações ---------
largura = 1280
altura = 720
FPS = 60

base_path = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(base_path, "audio", "lobby.mp3")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 0)

pygame.init()

icon_path = os.path.join(os.path.dirname(__file__), "imagens", "chickenjanela.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)
pygame.display.set_caption("Screaming Chicken")

FONT_BUTTON = pygame.font.SysFont("comicsansms", 48, italic=True, bold=True)

tela = pygame.display.set_mode((largura, altura))

caminho_fundo = os.path.join(os.path.dirname(__file__), "imagens", "menu.jpeg")
fundo_original = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo_original, (largura, altura))


class Button:
    def __init__(self, text, pos, callback, font=FONT_BUTTON):
        self.text = text
        self.callback = callback
        self.pos = pos
        self.font = font
        self.default_color = WHITE
        self.highlight_color = HIGHLIGHT
        self.label = self.font.render(self.text, True, self.default_color)
        self.rect = self.label.get_rect(center=pos)

    def draw(self, surface, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            color = self.highlight_color
        else:
            color = self.default_color

        # Contorno
        outline_color = BLACK
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for ox, oy in offsets:
            pos = self.rect.move(ox, oy)
            outline_surf = self.font.render(self.text, True, outline_color)
            surface.blit(outline_surf, pos)

        text_surf = self.font.render(self.text, True, color)
        surface.blit(text_surf, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        mid_x = largura // 2
        start_y = 380
        gap = 60

        self.buttons = [
            Button("play",    (mid_x, start_y), self.start_game),
            Button("options", (mid_x, start_y + gap), self.show_options),
            Button("quit",    (mid_x, start_y + 2 * gap), self.exit_game),
        ]

        self.running = True
        
        # Estado das skins
        self.skins_desbloqueadas = False
        self.skin_atual = 0 

        # Animação
        self.animating_circle = True
        self.circle_radius = 0
        self.circle_center = (largura // 2, altura // 2)
        self.animation_done = False

    def start_game(self):
        self.running = False 

    def show_options(self):
        # Chama a tela de opções passando o estado atual
        nova_escolha, status_unlock = abrir_opcoes(self.screen, self.skin_atual, self.skins_desbloqueadas)
        
        # Se não fechou a janela (-1), atualiza os dados
        if nova_escolha != -1:
            self.skin_atual = nova_escolha
            # Se desbloqueou lá dentro, salva aqui fora para não pedir código de novo
            if status_unlock:
                self.skins_desbloqueadas = True

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        clock = pygame.time.Clock()
        max_radius = int((largura ** 2 + altura ** 2) ** 0.5)

        while self.running:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                
                # Clique nos botões
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.animation_done:
                    for btn in self.buttons:
                        btn.check_click(mouse_pos)

            self.screen.blit(fundo, (0, 0))

            if self.animating_circle:
                mask = pygame.Surface((largura, altura))
                mask.fill(BLACK)
                mask.set_colorkey((255, 0, 255))
                pygame.draw.circle(mask, (255, 0, 255), self.circle_center, self.circle_radius)
                self.screen.blit(mask, (0, 0))
                self.circle_radius += 20
                if self.circle_radius > max_radius:
                    self.animating_circle = False
                    self.animation_done = True

            if self.animation_done:
                for btn in self.buttons:
                    btn.draw(self.screen, mouse_pos)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.mixer.music.stop()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((largura, altura))
        self.skin_escolhida = 0 
        self.skins_desbloqueadas = False

    def run(self):
        while True: # Loop mestre do aplicativo
            # 1. Abre o Menu
            menu = Menu(self.screen)
            # Passa o estado atual das skins para o menu não resetar
            menu.skin_atual = self.skin_escolhida
            menu.skins_desbloqueadas = self.skins_desbloqueadas
            
            menu.run()
            
            # 2. Quando o menu.run() termina (clicou em Play), salva as configs
            self.skin_escolhida = menu.skin_atual
            self.skins_desbloqueadas = menu.skins_desbloqueadas
            
            # 3. Inicia o Jogo
            # O jogo vai rodar até o jogador morrer e escolher "Menu" ou fechar
            self.game_loop()
            
    def game_loop(self):
        main(self.skin_escolhida)

if __name__ == "__main__":
    Game().run()