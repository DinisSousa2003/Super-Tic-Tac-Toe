#Iniciar Pygame
import pygame, math, time
from pygame.cursors import sizer_y_strings
from math import floor
import sys

pygame.init()


#Window
screen = pygame.display.set_mode((720,770))

#Window Name
pygame.display.set_caption("Super Tic Tac Toe")


#Carregar Imagens
x_corrente = pygame.image.load("Imagens/XOandWins/x_atual.png")
x_correnteRect = x_corrente.get_rect()
o_corrente = pygame.image.load("Imagens/XOandWins/o_atual.png")
o_correnteRect = o_corrente.get_rect()
player_correnteRect = x_correnteRect
player_corrente = x_corrente
grid_next = pygame.image.load("Imagens/Grids/grid actual.png")
grid_small = pygame.image.load("Imagens/Grids/grid small.png")
gridmain = pygame.image.load("Imagens/Grids/grid main.png")
gridmainfirst = pygame.image.load("Imagens/Grids/grid main1.png")
linhawin = pygame.image.load("Imagens/XOandWins/linhas.png")
linhawinRect = linhawin.get_rect()
colunawin = pygame.image.load("Imagens/XOandWins/colunas.png")
colunawinRect = colunawin.get_rect()
diagonal1win = pygame.image.load("Imagens/XOandWins/diagonal1.png")
diagonal1winRect = diagonal1win.get_rect()
diagonal2win = pygame.image.load("Imagens/XOandWins/diagonal2.png")
diagonal2winRect = diagonal2win.get_rect()

#Imagem gif Respect
gif_Respect = []
for i in range(6):
    gif_Respect.append(pygame.image.load(f"Imagens/GifMissionPassed/Mission_Passed{i+1}.png"))

#Imagem gif Inicial

def load_gif_inicial(gif_Inicial,i):
    image = pygame.image.load(f"Imagens/GifInicial/{i}.jpg").convert()
    image = pygame.transform.scale(image, (300, 321))
    gif_Inicial.append(image)

    return gif_Inicial

#Importar sons
Win_Sound = pygame.mixer.Sound("Sons/win music.mp3")
X_Sound = pygame.mixer.Sound("Sons/'x' sound.mp3")
O_Sound = pygame.mixer.Sound("Sons/'o' sound.mp3")
Button_Sound = pygame.mixer.Sound("Sons/Button.wav")
Music = pygame.mixer.music.load("Sons/Game Music.mp3")



#Variáveis globais
logicdraw = " "

gamesquares = []

grid_games = []

choose_jogo = [[0]*2 for i in range(9)]
logicRects = [[[0]*3 for small_line in range(3)] for game in range(9)]
starting_move_done = True
turn = 1

##Definir X e O
xplayer = pygame.image.load("Imagens/XOandWins/x.png").convert()
xplayerRect = xplayer.get_rect()
oplayer = pygame.image.load("Imagens/XOandWins/o.png").convert()
oplayerRect = oplayer.get_rect()
player = xplayer
playerRect = xplayerRect

def text(words, center, size,  color):
    """
    Parameters:
    words : string
    center : tuple (coords) or align
    size : integer
    color : name of color (from var "COLORS")
    """
    font = pygame.font.SysFont(None, size)
    text = font.render(words, True, color, None)
    textRect = text.get_rect()
    if center == "topleft":
        textRect.topleft = (10,10)
    elif center == "bottomleft":
        textRect.bottomleft = (10,760)
    elif center == "bottomright":
        textRect.bottomright = (710,760)
    else:
        textRect.center = center
    screen.blit(text, textRect)
    return textRect

def end():

    pygame.mixer.music.stop()
    Win_Sound.play()

    def check_win(xpoints,opoints):
        if opoints > xpoints:
            text("O WINS!!! (X="+str(xpoints)+" O="+str(opoints)+")",(360,385),70,(250,250,250))
        elif xpoints > opoints:
            text("X WINS!!! (X="+str(xpoints)+" O="+str(opoints)+")",(360,385),70,(250,250,250))
        else:
            text("IT'S A DRAW!!! (X="+str(xpoints)+" O="+str(opoints)+")",(360,385),70,(250,250,250))

    xpoints, opoints = pontuacao()
    screen.fill((0,0,0))
    
    #Check win
    check_win(xpoints,opoints)

    #play again button
    playagainRect = text("Play Again",(360,450),40,(0,197,144))

    #Quitbutton
    quitRect = text("Quit",(360,480),40,(255,0,0))

    #gif instruments (framerate and current time)
    framerate = 0.10
    c_t = time.time()
    frame = 0

    
    click = False
    run = True
    while run:

        if time.time() > c_t:
            frame = (frame + 1) % 6
            screen.blit(gif_Respect[frame], (115, 55))
            #obter imagem
            pygame.display.update()
            c_t += framerate

        #Check mouse pos
        mx, my = pygame.mouse.get_pos()

        if click:
            if playagainRect.collidepoint((mx,my)):
                Button_Sound.play()
                menu_inicial()
            if quitRect.collipoint((mx,my)):
                Button_Sound.play()
                run = False
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
    
        pygame.display.update()


#jogo 0:  0- 9
#jogo 1:  9-18
#jogo 2: 18-27
#jogo 3: 27-36
#jogo 4: 36-45
#jogo 5: 45-54
#jogo 6: 54-65
#jogo 7: 63-72
#jogo 8: 72-81

def full(gamenext):
    def detect_end():
        controlo = True
        for game in range(9):
            for line in range(3):
                for column in range(3):
                    if logic_map[game][line][column] == "a":
                        controlo = False
        if controlo:
            end()


    detect_end()
    controlo = False
    for i in range(3):
        for a in range(3):
            if logic_map[gamenext][i][a] == 'a':
                controlo = True
    if controlo:
        controlo = False
        return gamenext
    else:
        if gamenext == 8:
            gamenext = 0
        else:
            gamenext += 1
        return full(gamenext)

def if_full(gamenext):
    return range(choose_jogo[full(gamenext)][0],choose_jogo[full(gamenext)][1])
    

#com base no quadrado jogado retorna range(quadrado inicial,quadrado final+1)
def choose_games(quadrado_jogado):
    game, linha, coluna = transform(quadrado_jogado)
    gamenext = line_and_column_to_pos(linha,coluna)
    return if_full(gamenext)
    



def transform(pos_grid_grande):
    #posição de 0-80 -> jogo (0-8), linha(0-2), coluna(0-2)
    #take the rect on the list and discover where it is

    game = pos_grid_grande // 9

    pos_grid_pequena = pos_grid_grande % 9

    linha = pos_grid_pequena // 3
    coluna = pos_grid_pequena % 3

    return(game, linha, coluna)

def line_and_column_to_pos(line, column):
    #useful to dicover the next 'game' to be played
    #line, column -> pos in the grid

    return line*3 + column

def build_logicRects(gamesquares):
    #constroi 81 retangulos que serão usados na parte logica em matriz de 3
    for i in range(81):
        game, linha, coluna = transform(i)
        logicRects[game][linha][coluna] = gamesquares[i]

def create_logic_map():
    # 'x' for x, 'o' for o, ' ' for empty
    global logic_map
    logic_map = [[['a']*3 for small_line in range(3)] for game in range(9)] #a matrix that contains 9 matrices, each with one game
    
    #to write in the logic map give the following keys: logic_map[game][line][column]

def pontuacao():
    xpoints = count_points('x')
    opoints = count_points('o')

    font = pygame.font.SysFont(None, 50)
    xpontuacao = font.render("X - " + str(xpoints), True, (255,255,255), None)
    xpontuacaoRect = xpontuacao.get_rect()
    xpontuacaoRect.center = (180,745)
    
    pygame.draw.rect(screen, (0,0,0), xpontuacaoRect)
    screen.blit(xpontuacao, xpontuacaoRect)

    opontuacao = font.render("O - " + str(opoints), True, (255,255,255), None)
    opontuacaoRect = opontuacao.get_rect()
    opontuacaoRect.center = (540,745)

    pygame.draw.rect(screen, (0,0,0), opontuacaoRect)
    screen.blit(opontuacao, opontuacaoRect)
    return (xpoints, opoints)

def count_points(player):
    
    #player must be 'x' or 'o'

    points = 0

    def count_lines(points):
        for game in range(9):
            for line in range(3):
                current_line = logic_map[game][line]
                if current_line[0] == current_line[1] == current_line[2] == player:
                    points +=1
                    linhawinRect.center = logicRects[game][line][1].center
                    screen.blit(linhawin,linhawinRect)
        return points
    
    points = count_lines(points) #FIRST CHECKPOINT, LINES

    def count_columns(points):
        for game in range(9):
            current_game = logic_map[game]
            for column in range(3):
                if current_game[0][column] == current_game[1][column] == current_game[2][column] == player:
                    points += 1
                    colunawinRect.center = logicRects[game][1][column].center
                    screen.blit(colunawin,colunawinRect)
        return points
    
    points = count_columns(points) #SECOND CHECKPOINT, LINES + COLUMNS

    def count_diagonal(points):
        for game in range(9):
            current_game = logic_map[game]

            if current_game[0][0] == current_game[1][1] == current_game[2][2] == player:
                points += 1
                diagonal1winRect.center = logicRects[game][1][1].center
                screen.blit(diagonal1win,diagonal1winRect)

            if current_game[2][0] == current_game[1][1] == current_game[0][2] == player:
                points += 1
                diagonal2winRect.center = logicRects[game][1][1].center
                screen.blit(diagonal2win,diagonal2winRect)
        
        return points
    
    points = count_diagonal(points) #FINAL POINTS BABYYYYYYY

    return points #this are the points of the input player


def load_atributes():
    #Reseta mapa Lógico
    create_logic_map()

    #Load Listas e matrizes
    for i in range(9):
        for a in range(2):
            choose_jogo[i][a] = i*9+9*a

    gamesquares.clear()
    
    #b linha do pequeno
    #i coluna do pequeno
    #a linha do grande
    #c coluna do grande
    for linha_grande in range(3):
        y_quadrado = 10 + (233+2)*linha_grande
        for coluna_grande in range(3):
            x_quadrado = 10 + (233+2)*coluna_grande
            for b in range(3): 
                for i in range(3):
                    gamesquares.append(pygame.Rect.copy(pygame.Rect(x_quadrado+(77)*i,y_quadrado+(77)*b,77,77)))
    build_logicRects(gamesquares)
    global starting_move_done
    starting_move_done = True
    global turn
    turn = 1

def x_o():
    global turn, player, playerRect, player_corrente, player_correnteRect, logicdraw
    if turn%2 == 0:
        player = oplayer
        playerRect = oplayerRect
        player_corrente = o_corrente
        player_correnteRect = o_correnteRect
        logicdraw = 'o'
        O_Sound.play()
    else:
        player = xplayer
        playerRect = xplayerRect
        player_corrente = x_corrente
        player_correnteRect = x_correnteRect
        logicdraw = 'x'
        X_Sound.play()
    turn+=1

#jogadas
def play_move(mx,my,i):
    global jogada, starting_move_done
    if gamesquares[i].collidepoint(mx,my):
        #mudar mapa grande 
        if starting_move_done == True:
            screen.blit(gridmain, (10, 10))
            starting_move_done = False 
        else:   #troca vermelho por branco
            grid_clean()
            screen.blit(player,player_correnteRect)
        
        #Vez de jogar
        jogada=i  #guarda em jogada o quadrado jogado
        x_o()

        player_correnteRect.center = gamesquares[i].center
        screen.blit(player_corrente,player_correnteRect)
        gamesquares[i]=pygame.Rect(2000,2000,1,1)
        
        #desenhar 'x' 'o' com base no jogo
        game, linha, coluna = transform(i)
        logic_map[game][linha][coluna] = logicdraw
        #seleciona next grid
        grid_actual()

        #conta pontos
        pontuacao()
        #obter imagens
        pygame.display.update()
        



def first_move(mx,my):
    if starting_move_done == True:
        for i in range(81): #permite jogar em qualquer quadrado dos 81 existentes
            play_move(mx,my,i)
        return False
    return True

def moves(mx,my):
    for i in choose_games(jogada):
        play_move(mx,my,i)

def grid_actual():
    game, linha, coluna = transform(jogada)
    screen.blit(grid_next,grid_games[full(line_and_column_to_pos(linha,coluna))])

def grid_clean():
    game, linha, coluna = transform(jogada)
    screen.blit(grid_small,grid_games[full(line_and_column_to_pos(linha,coluna))])

def game(start):
    global turn,jogada
    screen.fill((0,0,0))
    if start:
        jogada=0

        #resetar squares e listas, resetar mapa logico etc.
        load_atributes()

        #Mapa do jogo grid main
        screen.blit(gridmainfirst, (10, 10))

        #Desenhar as pequenas grids e guarda-las numa lista
        initial_pos = (16, 16)
        increment = 233 +2 #size of small grid + big grid thickness
        for column in range(3):
            for line in range(3):
                screen.blit(grid_small, (initial_pos[0] + increment*line, initial_pos[1] + increment*column))
                grid_games.append((initial_pos[0] + increment*line, initial_pos[1] + increment*column))

        pontuacao()
    else:
        gamestate = pygame.image.load("Imagens/gamestate.jpg")
        screen.blit(gamestate,(0,0))
    exitRect = text("EXIT","bottomleft",45,(255,0,0))
    helpRect = text("HELP","bottomright",45,(255,0,0))
    #obter imagem
    pygame.display.update()

    #detetar o click
    click = False
    run = True
    while run:
        #obter mouse pos        
        mx, my = pygame.mouse.get_pos()
        
        #check colisions
        if click:
            if first_move(mx,my): #1º move? devolve False se sim e True se nao
                moves(mx,my)
            if helpRect.collidepoint((mx,my)):
                Button_Sound.play()
                pygame.image.save(screen,"Imagens/gamestate.jpg")
                instruction_menu(True)
            if exitRect.collidepoint((mx,my)):
                Button_Sound.play()
                menu_inicial()

        pygame.display.update()
        click = False
        #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def instructions(local,comefromgame):
    prev = False
    nxt = True
    screen.fill((0,0,0))
    a = 0
    if local == 0:
        local = "Instruçoes/0Game and Logic/0_"
        max_a = 3
    elif local == 1:
        local = "Instruçoes/1Connection and Moves/1_"
        max_a = 4
    elif local ==2:
        local = "Instruçoes/2Points/2_"
        max_a = 1
    run1 = True
    while run1:
        page = pygame.image.load(f"{local}{a}.png").convert()
        screen.blit(page,(0,0))
        go_backRect = text("Return","topleft",30,(255,0,0))
        pygame.draw.rect(screen,(0,0,0),go_backRect)
        go_backRect = text("Return","topleft",30,(255,0,0))
        if a != 0:
            prev = True
            previousRect = text("<-- Previous","bottomleft",30,(255,255,255))
        if a < max_a:
            nextRect = text("Next -->","bottomright",30,(255,255,255))
        else:
            nxt = False
        pygame.display.update()
        run = True
        click = False
        while run:
            mx,my = pygame.mouse.get_pos()
            if click:
                if go_backRect.collidepoint((mx,my)):
                    Button_Sound.play()
                    if comefromgame:
                        instruction_menu(True)
                    else:
                        instruction_menu(False)
                if prev and previousRect.collidepoint((mx,my)):
                    Button_Sound.play()
                    a -= 1
                    run = False
                if nxt and nextRect.collidepoint((mx,my)):
                    Button_Sound.play()
                    a += 1
                    run = False
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run1 = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

def instruction_menu(comefromgame):
    screen.fill((0,0,0))
    game_and_logicRect = text("Game Map and Logic",(360,190),40,(255,255,255))
    connection_and_movesRect = text("Connection and Moves",(360,380),40,(255,255,255))
    pointsRect = text("Points",(360,570),40,(255,255,255))
    go_backRect = text("Return","topleft",30,(255,0,0))
    pygame.display.update()
    click = False
    run = True
    while run:
        #get mouse pos
        mx,my = pygame.mouse.get_pos()
        #butoes
        if click:
            if go_backRect.collidepoint((mx,my)):
                Button_Sound.play()
                if comefromgame:
                    game(False)
                else:
                    menu_inicial()
            if game_and_logicRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(0,comefromgame)
            if connection_and_movesRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(1,comefromgame)
            if pointsRect.collidepoint((mx,my)):
                Button_Sound.play()
                instructions(2,comefromgame)

        click = False
        #eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

def menu_inicial():
    first_cycle=True
    gif_Inicial = []
    #gif instruments (framerate and current time)
    framerate_gif_Inicial = 0.06
    c_t_gif_Inicial = time.time()
    frame_gif_Inicial = 0

    #x and o animation
    phrase_animation = "X"
    coords_animation = (160, 478)

    framerate_animation = 0.15
    c_t_animation = time.time()
    frame_animation = 0

    pygame.mixer.music.play(-1) #initialize music
    click = False
    #Draw
    screen.fill((0,0,0))
    text("Super Tic Tac Toe",(360,450),70,(250,250,250))
    

    #PLAY BUTTON
    playRect = text("Play",(360,520),40,(0,197,144))

    #instructions
    instructionRect = text("Instructions",(360,560),40,(255,0,0))

    #obter imagem
    pygame.display.update()
    
    run = True
    #Loop
    while run:
        #check mouse positions
        mx, my = pygame.mouse.get_pos()

        #x_and_o
        font = pygame.font.SysFont(None, 18)
        text_phrase_animation = font.render(phrase_animation, True, (180, 180, 180), None)
        screen.blit(text_phrase_animation, coords_animation)
        
        if time.time() > c_t_animation:
            phrase_animation += "   O" if phrase_animation[-1] == "X" else "   X"
            if len(phrase_animation) > 90:
                pygame.draw.rect(screen,(0, 0, 0),(160,478,720,25))
                phrase_animation = "X"
            c_t_animation += framerate_animation
            
        #gif
        if time.time() > c_t_gif_Inicial:
            frame_gif_Inicial = (frame_gif_Inicial) % 93
            if frame_gif_Inicial != 92 and first_cycle:
                gif_Inicial = load_gif_inicial(gif_Inicial,frame_gif_Inicial)
            else:
                if first_cycle:
                    gif_Inicial = load_gif_inicial(gif_Inicial,frame_gif_Inicial)
                first_cycle=False
            screen.blit(gif_Inicial[frame_gif_Inicial], (200, 55))
            frame_gif_Inicial += 1
            #obter imagem
            c_t_gif_Inicial += framerate_gif_Inicial
            pygame.display.update()
       #Check posições
        if click:
            if playRect.collidepoint((mx,my)):
                Button_Sound.play()
                gif_Inicial.clear()
                game(True)
            if instructionRect.collidepoint((mx,my)):
                Button_Sound.play()
                gif_Inicial.clear()
                instruction_menu(False)
        click = False
        ##Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True


if __name__ == "__main__":
    menu_inicial()
