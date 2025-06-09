# Documentação do Projeto: Screaming Chicken em Python com Pygame

## 1. Visão Geral
**Tecnologia Utilizada:** Python + Pygame + sounddevice/pyaudio. <br>
**Descrição:** Jogo runner controlado por voz onde o jogador emite sons para fazer uma galinha pular obstáculos, inspirado no Dino Game do Chrome.<br>
**Objetivo:** Criar uma experiência interativa e divertida que utiliza reconhecimento de áudio simples para controle, com mecânicas de jogo acessíveis e potencial viral.

***


## 2. Descrição do Projeto
### O que é Chicken Scream? <br>
Screaming Chicken é um jogo de plataforma runner 2D em que o personagem principal, uma galinha estilizada, corre automaticamente por um cenário horizontal repleto de obstáculos gerados de forma procedural. A principal inovação está no controle por voz: o jogador deve utilizar o microfone para emitir sons — como gritos, assobios ou qualquer ruído — para fazer a galinha pular e evitar colisões. A intensidade (volume) do som captado define a altura do salto, criando uma experiência interativa incomum que mistura jogabilidade clássica com controle vocal experimental.

A proposta combina simplicidade de jogabilidade com um elemento caótico e cômico, estimulando a curiosidade e o engajamento de jogadores casuais, streamers e públicos mais jovens.

### 2.1 Funcionalidades Principais e Mecânicas de Jogo
* **Movimentação e Progressão:** <br>
  * A galinha se move automaticamente da esquerda para a direita em uma velocidade constante inicial.
  * A velocidade do deslocamento aumenta de forma incremental conforme o tempo de sobrevivência, intensificando o desafio gradualmente (aceleração linear com fator de limite máximo).
  * O cenário é infinito, mas usa técnicas de looping visual e geração randômica de terreno para parecer variado e dinâmico. <br>

* **Obstáculos e Terreno:**
  * Os obstáculos são posicionados com base em um algoritmo de geração procedural que considera distância mínima entre elementos, variedade visual e dificuldade crescente.
  * Tipos de obstáculos:
    * Cactos: altura média, exigem salto moderado.
    * Cercas: mais baixas, surgem em sequência para dificultar múltiplos pulos.
    * Pedras grandes: exigem pulos altos, surgem em velocidade mais avançada.
  * Alguns obstáculos móveis poderão ser adicionados em modos alternativos (ex: corvos voando em altura variável). <br>

* **Controle por Voz - Mecânica Central:**
  * A detecção do som é feita com sounddevice, utilizando análise em tempo real de amostras de áudio.
  * Cada frame coleta uma janela de som e calcula o RMS (root mean square) ou volume médio.
  * O volume é mapeado para altura de pulo com três zonas:
    * Silêncio / Ruído baixo: a galinha não pula.
    * Volume médio: pulo baixo (~altura padrão).
    * Volume alto: pulo alto (~pulo estendido).
  * Um filtro de ruído com threshold configurável evita ativações involuntárias causadas por ruídos ambientes. <br>

* **Sistema de Colisão e Game Over:**
  * A colisão é detectada por bounding boxes entre a galinha e obstáculos.
  * Ao colidir, o jogo entra no estado de Game Over, exibindo a pontuação, recorde e opção de reinício.
  * A animação de colisão inclui som de impacto, desaceleração e queda da galinha. <br>

* **Pontuação e Progresso:**
  * A pontuação é baseada na distância percorrida (tempo de sobrevivência).
  * Recordes são armazenados localmente (com possibilidade futura de leaderboard online).
  * Ao atingir marcos de distância, mensagens de incentivo podem ser exibidas (ex: "Você correu 500 metros!"). <br>


### 2.2 Interfaces e Feedback Visual
* **Tela de Jogo (HUD):** <br>
  * Exibição constante da pontuação atual no canto superior esquerdo.
  * Indicação visual do volume captado (barra de intensidade de som) — ajuda o jogador a calibrar a força do grito.
  * Animações de pulo e colisão são fluídas, com uso de interpolação para representar melhor a física. <br>

* **Telas do Jogo:** <br>
  * Menu Inicial: opções de iniciar, configurações, skins e créditos.
  * Tela de Pausa: opção de continuar, reiniciar ou sair.
  * Tela de Game Over: mostra pontuação atual, recorde e botão de jogar novamente.
  * Tela de Configurações: ajusta sensibilidade de microfone, volume de som, dificuldade inicial, etc. <br>
  

### 2.3 Interfaces e Feedback Visual
* **Movimentação e Progressão:** <br>
  * A galinha se move automaticamente da esquerda para a direita em uma velocidade constante inicial.
  * A velocidade do deslocamento aumenta de forma incremental conforme o tempo de sobrevivência, intensificando o desafio gradualmente (aceleração linear com fator de limite máximo).
  * O cenário é infinito, mas usa técnicas de looping visual e geração randômica de terreno para parecer variado e dinâmico. <br>


### 2.4 Interfaces e Feedback Visual
* **Movimentação e Progressão:** <br>
  * A galinha se move automaticamente da esquerda para a direita em uma velocidade constante inicial.
  * A velocidade do deslocamento aumenta de forma incremental conforme o tempo de sobrevivência, intensificando o desafio gradualmente (aceleração linear com fator de limite máximo).
  * O cenário é infinito, mas usa técnicas de looping visual e geração randômica de terreno para parecer variado e dinâmico. <br>


### 2.5 Interfaces e Feedback Visual
* **Movimentação e Progressão:** <br>
  * A galinha se move automaticamente da esquerda para a direita em uma velocidade constante inicial.
  * A velocidade do deslocamento aumenta de forma incremental conforme o tempo de sobrevivência, intensificando o desafio gradualmente (aceleração linear com fator de limite máximo).
  * O cenário é infinito, mas usa técnicas de looping visual e geração randômica de terreno para parecer variado e dinâmico. <br>


### 2.6 Interfaces e Feedback Visual
* **Movimentação e Progressão:** <br>
  * A galinha se move automaticamente da esquerda para a direita em uma velocidade constante inicial.
  * A velocidade do deslocamento aumenta de forma incremental conforme o tempo de sobrevivência, intensificando o desafio gradualmente (aceleração linear com fator de limite máximo).
  * O cenário é infinito, mas usa técnicas de looping visual e geração randômica de terreno para parecer variado e dinâmico. <br>

  
### 2.7 Arquitetura do Código
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
