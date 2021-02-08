# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:59:45 2021

@author: User
"""

import pygame, sys

pygame.init()

#COLORS
Green = (0, 197, 144)
Black = (0, 0, 0)
Baby_Blue = (0, 204, 255)
Golden = (255, 204, 0)
Red = (255, 0, 0)
White = (255, 255, 255)
Light_Grey = (211, 211, 211)

#SCREEN
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("TIC-TAC-TOE")

#DISPLAY TEXT
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


#PLAY BUTTON
font = pygame.font.SysFont(None, 45)
buttonPlay = font.render("PLAY", True, White, None)
buttonPlayRect = buttonPlay.get_rect()
buttonPlayRect.center = (250, 250)

#GAME LOOP
def menu():
    click = False
    run = True
    while run:
        
        screen.fill(Black)
         
        screen.blit(buttonPlay, buttonPlayRect)

        #Get mouse pos
        mx, my = pygame.mouse.get_pos()
        
        #Check collisions
        if buttonPlayRect.collidepoint((mx, my)):
            if click:
                play()
        
        click = False
        
        #EVENTS
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        
        pygame.display.update()  
        
##

def play():
    run = True
    while run:
        screen.fill(Red)
        
        text("DANI GAYYYY", (250, 200), 80, Light_Grey)
        
        #EVENTS
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu()
                    if event.key == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = True
                        
        pygame.display.update()          
        

if __name__ == "__main__":
    menu()