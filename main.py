
#Iniciar Pygame
import pygame, sys
pygame.init()

#Window
screen=pygame.display.set_mode((500,500))

#Window Name

pygame.display.set_caption("Tic Tac Toe")

#Global Variables
box = [175,150,150,200]

##Mapa Lógico
map = [[0,0,0],[0,0,0],[0,0,0]]

#Definir areas do jogo
quadrado1 = pygame.Rect(10,10,160,160)
quadrado2 = pygame.Rect(10+160,10,160,160)
quadrado3 = pygame.Rect(10+160+160,10,160,160)

quadrado4 = pygame.Rect(10,10+160,160,160)
quadrado5 = pygame.Rect(10+160,10+160,160,160)
quadrado6 = pygame.Rect(10+160+160,10+160,160,160)

quadrado7 = pygame.Rect(10,10+160+160,160,160)
quadrado8 = pygame.Rect(10+160,10+160+160,160,160)
quadrado9 = pygame.Rect(10+160+160,10+160+160,160,160)


#Funções
def text(words, center, size,  color):
    """
    Parameters:
    words : string
    center : tuple (coords)
    size : integer
    color : name of color (from var "COLORS")
    """
    font = pygame.font.SysFont(None, size)
    text = font.render(words, True, color, None)
    textRect = text.get_rect()
    textRect.center = center
    screen.blit(text, textRect)

def coluna_victory(i):
    #imagem das colunas
    coluna = pygame.image.load("Colunas.png")
    colunaRect = coluna.get_rect()
    #definir posição da imagem
    if i == 0:
        colunaRect.center = quadrado4.center
    elif i == 1:
        colunaRect.center = quadrado5.center
    elif i == 2:
        colunaRect.center = quadrado6.center
    screen.blit(coluna,colunaRect)
    pygame.display.update()

def linha_victory(i):
    #imagem da linha
    linha = pygame.image.load("linhas.png")
    linhaRect = linha.get_rect()
    #definir posição da imagem
    if i == 0:
        linhaRect.center = quadrado2.center
    elif i == 1:
        linhaRect.center = quadrado5.center
    elif i == 2:
        linhaRect.center = quadrado8.center
    screen.blit(linha,linhaRect)
    pygame.display.update()

def diagonal1_victory():
    #imagem da diagonal1
    diagonal1 = pygame.image.load("diagonal1.png")
    diagonal1Rect = diagonal1.get_rect()
    #definir posição da imagem
    diagonal1Rect.center = quadrado5.center
    screen.blit(diagonal1,diagonal1Rect)
    pygame.display.update()

def diagonal2_victory():
    #imagem da diagonal1
    diagonal2 = pygame.image.load("diagonal2.png")
    diagonal2Rect = diagonal2.get_rect()
    #definir posição da imagem
    diagonal2Rect.center = quadrado5.center
    screen.blit(diagonal2,diagonal2Rect)
    pygame.display.update()

def menu_final():
    #Play again
    font = pygame.font.SysFont(None,25)
    playagain = font.render("Play Again",True,(0, 197, 144))
    playagainRect = playagain.get_rect()
    playagainRect.center = (250,250)
    screen.blit(playagain,playagainRect)

    #Quit
    quit = font.render("Quit",True,(255, 0, 0))
    quitRect = quit.get_rect()
    quitRect.center = (250,280)
    screen.blit(quit,quitRect)

    pygame.display.update()
    click = False
    while True:
        #get mouse cod
        mx, my = pygame.mouse.get_pos()
        #Check colisions
        if click:
            if playagainRect.collidepoint((mx,my)):
                menu_inicial()
            if quitRect.collidepoint((mx,my)):
                pygame.quit()
                sys.exit()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


def x_victory():
    #Quadrado
    pygame.draw.rect(screen,(0, 204, 255),box)
    text("X player Wins!",(250,200),30,(255, 204, 0))
    menu_final()
    
def o_victory():
    #Quadrado
    pygame.draw.rect(screen,(0, 204, 255),box)
    text("O player Wins!",(250,200),30,(255, 204, 0))
    menu_final()
    
def draw():
    #Quadrado
    pygame.draw.rect(screen,(0, 204, 255),box)
    text("Draw!",(250,200),30,(255, 255, 255))
    menu_final()

def check_victory():
    #Vitoria na horizontal
    for i in range(3):
        if map[i][0] == map[i][1] == map[i][2]:
            if map[i][0] == 1 or map[i][0] == 2:
                linha_victory(i)
            if map[i][0] == 1:
                x_victory()
            if map[i][0] == 2:
                o_victory()

    #Vitoria na vertical
    for i in range(3):
        if map[0][i] == map[1][i] == map[2][i]:
            if map[0][i] == 1 or map[0][i] == 2:
                coluna_victory(i)
            if map[0][i] == 1:
                x_victory()
            if map[0][i] == 2:
                o_victory()

    #Vitorias na diagonal
    ##Diagonal 1
    if map[0][0] == map[1][1] == map[2][2]:
            if map[0][0] == 1 or map[0][0] == 2:
                diagonal1_victory()
            if map[0][0] == 1:
                x_victory()
            if map[0][0] == 2:
                o_victory()
    if map[0][2] == map[1][1] == map[2][0]:
            if map[1][1] == 1 or map[1][1] == 2:
                diagonal2_victory()
            if map[1][1] == 1:
                x_victory()
            if map[1][1] == 2:
                o_victory()

def check_draw():
    c=0
    for i in range(3):
        for a in range(3):
            if map[i][a] != 0:
                c+=1
    if c == 9:
        draw()

def clean_map():
    for i in range(3):
        for a in range(3):
            map[i][a] = 0

def game():
    turn = 1
    #Resetar mapa logico
    clean_map()
    #Mapa do Jogo
    grid = pygame.image.load("grid.png").convert()
    gridRect = grid.get_rect()
    gridRect.center = (250,250)
    screen.fill((0,0,0))
    screen.blit(grid,gridRect)
    pygame.display.update()
    click = False
    
    #Definir X e O
    xplayer = pygame.image.load("x.png").convert()
    xplayerRect = xplayer.get_rect()
    oplayer = pygame.image.load("o.png").convert()
    oplayerRect = oplayer.get_rect()

    #variaveis de quadrado
    q1=q2=q3=q4=q5=q6=q7=q8=q9= True

    #Loop do jogo
    while True:
        #Obter pos do mouse
        mx, my = pygame.mouse.get_pos()

        #verificar colisão e vez de jogar
        if click:
            if turn%2 == 0:
                player = oplayer
                playerRect = oplayerRect
                pl = 2
            else:
                player = xplayer
                playerRect = xplayerRect
                pl = 1


            if quadrado1.collidepoint((mx,my)) and q1:
                turn += 1
                q1 = False
                playerRect.center = quadrado1.center
                screen.blit(player,playerRect)
                map[0][0] = pl
            if quadrado2.collidepoint((mx,my)) and q2:
                turn += 1
                q2 = False
                playerRect.center = quadrado2.center
                screen.blit(player,playerRect)
                map[0][1] = pl
            if quadrado3.collidepoint((mx,my)) and q3:
                turn += 1
                q3 = False
                playerRect.center = quadrado3.center
                screen.blit(player,playerRect)
                map[0][2] = pl


            if quadrado4.collidepoint((mx,my)) and q4:
                q4 = False
                turn += 1
                playerRect.center = quadrado4.center
                screen.blit(player,playerRect)
                map[1][0] = pl
            if quadrado5.collidepoint((mx,my)) and q5:
                q5 = False
                turn += 1
                playerRect.center = quadrado5.center
                screen.blit(player,playerRect)
                map[1][1] = pl
            if quadrado6.collidepoint((mx,my)) and q6:
                q6 = False
                turn += 1
                playerRect.center = quadrado6.center
                screen.blit(player,playerRect)
                map[1][2] = pl


            if quadrado7.collidepoint((mx,my)) and q7:
                turn += 1
                q7 = False
                playerRect.center = quadrado7.center
                screen.blit(player,playerRect)
                map[2][0] = pl
            if quadrado8.collidepoint((mx,my)) and q8:
                turn += 1
                q8 = False
                playerRect.center = quadrado8.center
                screen.blit(player,playerRect)
                map[2][1] = pl
            if quadrado9.collidepoint((mx,my)) and q9:
                turn += 1
                q9 = False
                playerRect.center = quadrado9.center
                screen.blit(player,playerRect)
                map[2][2] = pl
            
            check_victory()
            check_draw()

        click = False

        #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        

def play_button():
    font = pygame.font.SysFont(None,20)
    text = font.render("Play",True,(0,197,144))
    playRect = text.get_rect()
    playRect.center = (250,300)
    screen.blit(text,playRect)
    click = False
    run = True
    pygame.display.update()
    #Loop
    while run:
        #check mouse positions
        mx, my = pygame.mouse.get_pos()
        #Check posições
        if playRect.collidepoint((mx,my)):
            if click:
                run = False
                game()

        ##Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()



def menu_inicial():
    screen.fill((0,0,0))
    text("Tic Tac Toe",(250,250),40,(250,250,250))
    play_button()


if __name__ == "__main__":
    menu_inicial()



pygame.quit()
sys.exit()