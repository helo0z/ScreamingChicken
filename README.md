Documentação do Projeto: Screaming Chicken (Python + Pygame)
1. Visão Geral

Tecnologia Utilizada:
Python 3 + Pygame + NumPy

Descrição:
Screaming Chicken é um jogo runner 2D no estilo infinito, inspirado no Dino Game do Chrome, onde o jogador controla uma galinha estilizada que corre automaticamente e precisa pular obstáculos para sobreviver o máximo de tempo possível.

Objetivo:
Criar uma experiência simples, divertida e altamente viciante, com progressão contínua de dificuldade, mudanças visuais no cenário conforme o tempo de sobrevivência e elementos secretos (Easter Eggs) que incentivam a exploração e a curiosidade do jogador.

2. Descrição do Projeto
2.1 O que é Screaming Chicken?
Screaming Chicken é um jogo de plataforma runner 2D em que o personagem principal corre automaticamente por um cenário horizontal infinito, repleto de obstáculos gerados de forma processual.
O jogador controla os saltos da galinha por meio de comandos tradicionais (teclado/mouse), focando em tempo de reação, ritmo e precisão.
O tom do jogo é cartunesco, cômico e leve, com animações exageradas e progressão de dificuldade contínua, tornando-o ideal para jogadores casuais e sessões rápidas.

2.2 Funcionalidades Principais e Mecânicas de Jogo
Movimentação e Progressão
A galinha se move automaticamente da esquerda para a direita.
A velocidade inicial é constante e aumenta gradualmente conforme o tempo de sobrevivência.
O aumento de dificuldade segue uma progressão linear com limite máximo configurável.
O jogo não possui fim definido (runner infinito).
Cenário Dinâmico (Mudança por Tempo de Sobrevivência)
O cenário muda automaticamente conforme o tempo de sobrevivência do jogador, inspirado no sistema do Dino Game do Chrome.

Exemplos de variação:
Fase inicial: cenário claro (dia).
Após determinado tempo: transição para entardecer.
Tempos avançados: cenário noturno, com mudanças de paleta, iluminação e elementos visuais.
As transições são suaves, sem interromper a jogabilidade.
As mudanças servem como feedback visual de progressão, aumentando a sensação de avanço e desafio.

Obstáculos e Terreno
Obstáculos gerados de forma processual.

O algoritmo considera:
Distância mínima entre obstáculos.
Variedade visual.
Aumento gradual da dificuldade.

Tipos de obstáculos:
Cactos: altura média, exigem salto padrão.
Cercas: mais baixas, surgem em sequência.
Pedras grandes: exigem saltos mais precisos.
Em estágios avançados, obstáculos móveis podem ser introduzidos.

Sistema de Colisão e Game Over
Colisões baseadas em caixas delimitadoras (hitbox).
Ao colidir:
O jogo entra no estado de Game Over.
Exibe pontuação atual e recorde.
Oferece opção de reinício.
Animações de impacto e desaceleração reforçam o feedback visual.

Pontuação e Progresso
Pontuação baseada no tempo de sobrevivência e distância percorrida.
Recordes são armazenados localmente.
Marcos importantes exibem mensagens de incentivo:
Ex: “Você sobreviveu por 60 segundos!”

2.3 Interfaces e Feedback Visual
HUD (Tela de Jogo)
Pontuação atual exibida no canto superior da tela.
Indicação visual clara do estado do jogo.
Animações fluidas com interpolação simples para simular física.

Telas do Jogo
Menu Inicial: iniciar jogo, opções, skins e créditos.
Tela de Pausa: continuar, reiniciar ou sair.
Tela de Game Over: pontuação atual, recorde e botão de jogar novamente.
Tela de Opções: ajustes básicos de áudio, dificuldade inicial e preferências visuais.
Tela de Skins: seleção de aparências da galinha.

2.4 Modos de Jogo Alternativos (Extras)
Modo Desafio
Obstáculos mais frequentes.
Menor espaço entre eles.
Pontuação dobrada.
Fases com tempo limitado (ex: 30 segundos por fase).

2.5 Sistema de Skins e Recompensas
Skins desbloqueáveis ao atingir conquistas específicas:
Sobreviver por determinado tempo.
Alcançar distâncias específicas.
Todas as skins são apenas estéticas, sem impacto na jogabilidade.
Algumas skins são obtidas exclusivamente através de segredos do jogo (Easter Eggs).

2.6 Easter Egg – Palavra Secreta
Descrição
O jogo possui um Easter Egg totalmente oculto, sem qualquer indicação explícita ao jogador.
Como funciona
O jogador deve:
Acessar o Menu Principal.
Entrar na opção “Opções”.
Digitar uma palavra secreta (não revelada pelo jogo).
Não há dicas diretas: o jogador precisa descobrir sozinho que o segredo existe e adivinhar a palavra correta.

Recompensa
Ao acertar a palavra secreta:
O jogador desbloqueia duas skins exclusivas gratuitamente.
Uma mensagem especial confirma a descoberta do Easter Egg.

Objetivo do Easter Egg
Incentivar curiosidade.
Estimular exploração dos menus.
Criar um senso de mistério e recompensa para jogadores atentos.

2.7 Aspectos de Design e Sonoplastia
Trilha sonora leve, com loops curtos.
Efeitos sonoros distintos para:
Saltos.
Colisões.
Desbloqueios e conquistas.
Feedback sonoro especial ao desbloquear skins ou segredos.
Estilo visual cartunesco, com cores vibrantes e animações exageradas.

2.8 Mecânica de Dificuldade Progressiva
A velocidade do jogo aumenta a cada intervalo de tempo definido.
A frequência de obstáculos cresce conforme a sobrevivência.
Após determinado tempo:
Introdução de obstáculos mais complexos.
Cenários mais escuros ou visualmente desafiadores.

2.9 Arquitetura do Código
ScreamingChicken-main/
├── audio/                # Áudios do jogo
│   ├── FaseUm.mp3
│   ├── lobby.mp3
│   └── pulo.mp3
├── core/
│   └── game.py           # Loop principal do jogo
├── imagens/              # Sprites e fundos
│   ├── arbusto.png
│   ├── chicken.png
│   ├── FundoUm.jpeg
│   ├── menu.jpeg
│   ├── nuvem.png
│   └── piso.jpg
├── main.py               # Inicialização e lógica geral
└── README.md

3. Etapas de Entrega
Etapa 1 – Protótipo Básico (Semana 1–2)
Configuração do ambiente.
Estrutura inicial do projeto.
Movimento básico da galinha.
Geração simples de obstáculos.

Etapa 2 – Lógica Principal (Semana 3–4)
Sistema de colisões.
Pontuação e progressão de dificuldade.
Mudança dinâmica de cenário.
Implementação do Game Over.

Etapa 3 – Polimento (Semana 5)
Menus e interfaces.
Efeitos sonoros e visuais.
Sistema de skins.
Implementação do Easter Egg.

Etapa 4 – Testes e Finalização (Semana 6)
Testes de desempenho.
Ajustes de balanceamento.
Correção de bugs.
Documentação final e empacotamento.

4. Requisitos Técnicos
4.1 Dependências
Python 3.10+
pygame==2.5.2
numpy==1.26.0
Instalação:
pip install pygame==2.5.2 numpy==1.26.0

5. Considerações Finais
Screaming Chicken aposta em simplicidade, progressão visual clara e elementos secretos para criar uma experiência divertida e rejogável.
A mudança dinâmica de cenário reforça a sensação de evolução, enquanto o Easter Egg secreto adiciona profundidade e engajamento para jogadores mais curiosos.
O documento será atualizado conforme o desenvolvimento evoluir, refletindo ajustes técnicos, criativos e de balanceamento.
