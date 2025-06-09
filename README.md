# Documentação do Projeto: Chicken Scream em Python com Pygame

## 1. Visão Geral
**Tecnologia Utilizada:** Python + Pygame + sounddevice/pyaudio. <br>
**Descrição:** Jogo runner controlado por voz onde o jogador emite sons para fazer uma galinha pular obstáculos, inspirado no Dino Game do Chrome.<br>
**Objetivo:** Criar uma experiência interativa e divertida que utiliza reconhecimento de áudio simples para controle, com mecânicas de jogo acessíveis e potencial viral.

***


## 2. Descrição do Projeto
### O que é Chicken Scream? <br>
Jogo de ação onde uma galinha corre automaticamente e o jogador deve gritar ou emitir sons no microfone para fazê-la pular obstáculos. A intensidade do som afeta a altura do pulo.

### 2.1 Funcionalidades Principais
* **Motor do Jogo:** <br>
  * Movimento automático lateral da galinha.
  * Geração procedural de obstáculos (cactos, cercas, pedras).
  * Sistema de colisão e game over.
  * Pontuação baseada em distância percorrida.
  * Aumento progressivo de dificuldade. <br>

* **Controle por Áudio:**
  * Captura de volume do microfone em tempo real.
  * Mapeamento de intensidade sonora para altura do pulo.
  * Filtro de ruído para evitar falsos positivos. <br>

* **Interface:**
  * Renderização 2D dos elementos do jogo.
  * Telas de menu, game over e pausa.
  * Exibição de pontuação e recorde.
  * Feedback visual para pulos e colisões. <br>

* **Extras:**
  * Efeitos sonoros temáticos.
  * Múltiplas skins para a galinha.
  * Sistema de achievements.
  * Modos de jogo alternativos. <br>

### 2.2 Arquitetura do Código
chicken_scream/
├── main.py           	 	# Inicialização e loop principal
├── core/             		 # Lógica central
│   ├── game.py        	# Gerenciador de estado do jogo
│   ├── player.py      	# Comportamento da galinha
│   └── obstacles.py   	# Geração de obstáculos
├── audio/             		# Sistema de áudio
│   ├── input.py       	# Captura do microfone
│   └── effects.py     	# Efeitos sonoros
├── ui/                		# Interface
│   ├── renderer.py    	# Renderização gráfica
│   ├── screens.py     	# Telas do jogo
│   └── hud.py         	# Elementos de HUD
└── utils/             		# Utilitários
    ├── config.py      	# Configurações
    ├── score.py       	# Gerenciamento de pontuações
    └── assets.py      	# Carregamento de recursos



## 3. Etapas de Entrega
### **Etapa 1: Protótipo Básico (Semana 1-2)**
* Configuração do ambiente de desenvolvimento.
* Estrutura inicial do projeto.
* Implementação básica do movimento da galinha.
* Sistema simples de geração de obstáculos.
* Captura básica de áudio do microfone. <br>

### **Etapa 2: Lógica Principal (Semana 3-4)**
* Controle refinado por voz.
* Sistema completo de colisões.
* Pontuação e aumento progressivo de dificuldade.
* Geração procedural melhorada de obstáculos.
* Implementação do game over. <br>

### **Etapa 3: Polimento (Semana 5)**
* Menu inicial e telas auxiliares.
* Efeitos sonoros e visuais.
* Sistema de recordes.
* Opções de configuração.
* Balanceamento de dificuldade. <br>

### **Etapa 4: Testes e Finalização (Semana 6)**
* Testes com diferentes dispositivos de áudio.
* Otimização de performance.
* Correção de bugs.
* Documentação final.
* Empacotamento para distribuição.

## 4. Requisitos Técnicos
### 4.1 Dependências
Python <br>
Copy <br>
Download <br>
pygame==2.5.2 <br>
sounddevice==0.4.6 <br>
numpy==1.26.0 <br>

### 4.2 Easter Egg: Galinha Ninja
**Como ativar:**
1. Pular no mínimo 7 vezes consecutivas sem colidir
2. No 7º pulo, clicar com o botão direito do mouse

**Efeito:**
Transformação visual em galinha ninja
Invulnerabilidade temporária (5 segundos)
Efeitos sonoros especiais

**Implementação:**
python
Copy
Download <br>

class Player:
    def __init__(self):
        self.consecutive_jumps = 0
        
    def jump(self):
        self.consecutive_jumps += 1
        if self.consecutive_jumps == 7:
            self.check_ninja_egg()
            
    def check_ninja_egg(self):
        if pygame.mouse.get_pressed()[2]:  # Botão direito
            self.activate_ninja_mode()
            
    def activate_ninja_mode(self):
        # Implementação dos efeitos especiais
        pass



## 5. Considerações Finais
O projeto será desenvolvido de forma iterativa, com testes constantes para garantir uma experiência de jogo estável, fluida e divertida. A introdução do Ovo de Páscoa traz um toque de surpresa, incentivando a curiosidade e a exploração por parte do jogador.
Este documento será atualizado conforme o avanço do desenvolvimento, refletindo eventuais ajustes, melhorias e decisões tomadas ao longo do processo.
