import pygame
import sys
import os

largura = 1280
altura = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (255, 255, 0)

def tela_game_over(screen):
    base_path = os.path.dirname(os.path.abspath(__file__))
    diretorio_imagens = os.path.join(base_path, "imagens")
    
    # Fontes baseadas no estilo do menu original
    try:
        font_titulo = pygame.font.SysFont("comicsansms", 90, bold=True)
        font_botao = pygame.font.SysFont("comicsansms", 48, italic=True, bold=True)
    except:
        font_titulo = pygame.font.get_default_font()
        font_botao = pygame.font.get_default_font()

    # Carregar o fundo solicitado: fundoTres
    try:
        # Tenta carregar com a extensão .jpeg como está na sua main
        caminho_fundo = os.path.join(diretorio_imagens, "fundoTres.jpeg")
        fundo = pygame.image.load(caminho_fundo).convert()
        fundo = pygame.transform.scale(fundo, (largura, altura))
    except:
        fundo = pygame.Surface((largura, altura))
        fundo.fill((20, 20, 50)) # Fallback azul escuro

    def desenhar_texto_com_contorno(texto, fonte, cor, centro):
        # Cria o efeito de contorno (outline) para legibilidade
        offsets = [(-2, -2), (-2, 2), (2, -2), (2, 2), (0, -2), (0, 2), (-2, 0), (2, 0)]
        for ox, oy in offsets:
            surf_contorno = fonte.render(texto, True, BLACK)
            rect_contorno = surf_contorno.get_rect(center=(centro[0] + ox, centro[1] + oy))
            screen.blit(surf_contorno, rect_contorno)
        
        surf_principal = fonte.render(texto, True, cor)
        rect_principal = surf_principal.get_rect(center=centro)
        screen.blit(surf_principal, rect_principal)
        return rect_principal

    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(fundo, (0, 0))

        # Título centralizado
        desenhar_texto_com_contorno("GAME OVER", font_titulo, (255, 80, 80), (largura // 2, 220))

        # Lógica de Hover (muda cor se o mouse estiver em cima)
        color_retry = HIGHLIGHT if (largura//2 - 200 < mouse_pos[0] < largura//2 + 200 and 390 < mouse_pos[1] < 450) else WHITE
        color_menu = HIGHLIGHT if (largura//2 - 200 < mouse_pos[0] < largura//2 + 200 and 490 < mouse_pos[1] < 550) else WHITE

        rect_retry = desenhar_texto_com_contorno("tentar novamente", font_botao, color_retry, (largura // 2, 420))
        rect_menu = desenhar_texto_com_contorno("menu principal", font_botao, color_menu, (largura // 2, 520))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rect_retry.collidepoint(mouse_pos):
                    return "retry"
                if rect_menu.collidepoint(mouse_pos):
                    return "menu"

        pygame.display.flip()