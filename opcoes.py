import pygame
import os

# --- Configurações Básicas ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE_SELECIONADO = (0, 255, 0)
AMARELO_OURO = (255, 215, 0)
LARANJA_CANGACO = (205, 133, 63) # Cor de couro
ROSA_UNICORNIO = (255, 105, 180) # Rosa Choque

# Caminhos
base_path = os.path.dirname(os.path.abspath(__file__))
path_imagens = os.path.join(base_path, "imagens")

def carregar_imagens(largura, altura):
    imagens = {}
    try:
        fundo = pygame.image.load(os.path.join(path_imagens, "FundoUm.jpeg"))
        imagens['fundo'] = pygame.transform.scale(fundo, (largura, altura))
        
        galinha = pygame.image.load(os.path.join(path_imagens, "galinha1.png")).convert_alpha()
        imagens['galinha'] = pygame.transform.scale(galinha, (128, 128))
    except Exception as e:
        print(f"Erro imagens: {e}")
        imagens['fundo'] = pygame.Surface((largura, altura))
        imagens['fundo'].fill((0, 100, 0))
        imagens['galinha'] = pygame.Surface((128, 128))
        imagens['galinha'].fill(BRANCO)
    return imagens

def aplicar_filtro_cor(imagem, cor_filtro):
    img_copia = imagem.copy()
    filtro = pygame.Surface(img_copia.get_size()).convert_alpha()
    filtro.fill(cor_filtro)
    img_copia.blit(filtro, (0,0), special_flags=pygame.BLEND_RGBA_MULT)
    return img_copia

def desenhar_card_skin(superficie, x, y, imagem_galinha, nome_skin, cor_texto, selecionado=False):
    largura_card = 250
    altura_card = 350
    
    # Fundo do card (mais escuro se não selecionado)
    fundo_card = pygame.Surface((largura_card, altura_card))
    fundo_card.set_alpha(180)
    fundo_card.fill(PRETO)
    superficie.blit(fundo_card, (x, y))
    
    # Borda
    cor_borda = VERDE_SELECIONADO if selecionado else BRANCO
    espessura = 5 if selecionado else 2
    pygame.draw.rect(superficie, cor_borda, (x, y, largura_card, altura_card), espessura)

    # Galinha
    rect_img = imagem_galinha.get_rect(center=(x + largura_card//2, y + 150))
    superficie.blit(imagem_galinha, rect_img)

    # Nome da Skin
    fonte = pygame.font.SysFont("comicsansms", 24, bold=True) # Fonte mais divertida
    texto = fonte.render(nome_skin, True, cor_texto)
    rect_texto = texto.get_rect(center=(x + largura_card//2, y + 280))
    superficie.blit(texto, rect_texto)
    
    # Status
    msg = "SELECIONADO" if selecionado else "Disponível"
    cor_status = VERDE_SELECIONADO if selecionado else BRANCO
    fonte_p = pygame.font.SysFont("arial", 14, bold=True)
    texto_msg = fonte_p.render(msg, True, cor_status)
    rect_msg = texto_msg.get_rect(center=(x + largura_card//2, y + 310))
    superficie.blit(texto_msg, rect_msg)

def desenhar_input_codigo(superficie, texto_atual, x, y):
    fonte = pygame.font.SysFont("arial", 30)
    
    rect_input = pygame.Rect(x, y, 300, 50)
    pygame.draw.rect(superficie, BRANCO, rect_input)
    pygame.draw.rect(superficie, PRETO, rect_input, 2)

    img_texto = fonte.render(texto_atual, True, PRETO)
    superficie.blit(img_texto, (rect_input.x + 10, rect_input.y + 5))

    fonte_instrucao = pygame.font.SysFont("arial", 20, bold=True)
    instrucao = fonte_instrucao.render("Digite o código secreto:", True, BRANCO)
    superficie.blit(instrucao, (x, y - 30))

# --- FUNÇÃO PRINCIPAL ---
def abrir_opcoes(tela, skin_atual, ja_desbloqueado):
    largura, altura = tela.get_size()
    imgs = carregar_imagens(largura, altura)
    
    # --- CRIAÇÃO DAS SKINS ---
    # 0: Original
    skin_original = imgs['galinha']
    
    # 1: Cangaceiro (Laranja/Marrom)
    skin_cangaceiro = aplicar_filtro_cor(imgs['galinha'], (210, 105, 30, 150))
    
    # 2: Unicórnio (Rosa)
    skin_unicornio = aplicar_filtro_cor(imgs['galinha'], (255, 105, 180, 150))
    
    clock = pygame.time.Clock()
    rodando_opcoes = True
    
    nova_skin = skin_atual
    desbloqueado = ja_desbloqueado
    texto_codigo = ""

    font_btn = pygame.font.SysFont("comicsansms", 30, bold=True)
    lbl_voltar = font_btn.render("VOLTAR", True, BRANCO)
    rect_voltar = lbl_voltar.get_rect(center=(largura//2, 650))

    # Cálculos de Posição (Para 3 cartas centralizadas)
    # Largura total = 1280. Cartas tem 250px. Espaço entre elas 50px.
    # Pos X Carta 1: 215
    # Pos X Carta 2: 515
    # Pos X Carta 3: 815
    y_cartas = 180
    x_c1 = 215
    x_c2 = 515
    x_c3 = 815

    while rodando_opcoes:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1, desbloqueado
            
            # DIGITAÇÃO DO CÓDIGO
            if event.type == pygame.KEYDOWN:
                if not desbloqueado:
                    if event.key == pygame.K_BACKSPACE:
                        texto_codigo = texto_codigo[:-1]
                    else:
                        if len(texto_codigo) < 10 and event.unicode.isalnum():
                            texto_codigo += event.unicode.upper()
                    
                    if texto_codigo == "OVO":
                        desbloqueado = True
                        texto_codigo = ""
                        try:
                            som = pygame.mixer.Sound(os.path.join(base_path, "audio", "pulo.mp3"))
                            som.play()
                        except: pass

            # CLIQUES DO MOUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Botão Voltar
                    if rect_voltar.collidepoint(mouse_pos):
                        rodando_opcoes = False
                    
                    # Seleção de Skins (Se desbloqueado)
                    if desbloqueado:
                        # Carta 1: Original
                        if x_c1 < mouse_pos[0] < x_c1 + 250 and y_cartas < mouse_pos[1] < y_cartas + 350:
                            nova_skin = 0
                        # Carta 2: Cangaceiro
                        elif x_c2 < mouse_pos[0] < x_c2 + 250 and y_cartas < mouse_pos[1] < y_cartas + 350:
                            nova_skin = 1
                        # Carta 3: Unicórnio
                        elif x_c3 < mouse_pos[0] < x_c3 + 250 and y_cartas < mouse_pos[1] < y_cartas + 350:
                            nova_skin = 2

        # --- DESENHO ---
        tela.blit(imgs['fundo'], (0, 0))

        fonte_titulo = pygame.font.SysFont("comicsansms", 60, bold=True)
        txt_titulo = fonte_titulo.render("OPÇÕES DE SKIN", True, BRANCO)
        
        # Sombra do Título
        sombra = fonte_titulo.render("OPÇÕES DE SKIN", True, PRETO)
        tela.blit(sombra, (largura//2 - txt_titulo.get_width()//2 + 3, 53))
        tela.blit(txt_titulo, (largura//2 - txt_titulo.get_width()//2, 50))

        if desbloqueado:
            # Desenha as 3 cartas
            desenhar_card_skin(tela, x_c1, y_cartas, skin_original, "A Clássica", BRANCO, selecionado=(nova_skin == 0))
            desenhar_card_skin(tela, x_c2, y_cartas, skin_cangaceiro, "Galampião", LARANJA_CANGACO, selecionado=(nova_skin == 1))
            desenhar_card_skin(tela, x_c3, y_cartas, skin_unicornio, "Galinhacórnio", ROSA_UNICORNIO, selecionado=(nova_skin == 2))
        else:
            # Caixa de Código
            desenhar_input_codigo(tela, texto_codigo, largura//2 - 150, altura//2 - 25)
            
            fonte_aviso = pygame.font.SysFont("arial", 20, italic=True)
            aviso = fonte_aviso.render("Digite 'OVO' para liberar o galinheiro secreto", True, (200, 200, 200))
            rect_aviso = aviso.get_rect(center=(largura//2, altura//2 + 50))
            tela.blit(aviso, rect_aviso)

        # Botão Voltar
        cor_btn = AMARELO_OURO if rect_voltar.collidepoint(mouse_pos) else BRANCO
        lbl_voltar = font_btn.render("VOLTAR", True, cor_btn)
        tela.blit(lbl_voltar, rect_voltar)

        pygame.display.flip()
        clock.tick(60)
    
    return nova_skin, desbloqueado