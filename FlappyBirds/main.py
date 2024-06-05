import random
import sys # we will use sys.exit to exit program
import pygame
from pygame.locals import *

#Global variables for the game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
PLAYER = 'imgs/bird1.png'
BACKGROUND = 'imgs/bg.png'
PIPE = 'imgs/pipe.png'

def welcomeScreen():
    #Show welcome image on the screen
    playerx = int(SCREENWIDTH/5)
    playery =  int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    basex = 0
    while True:
        for event in pygame.event.get():
            #if user click on cross button, close the game
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            #if the user presses space or up, start the game 
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))   
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0 

    #Create two pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    #mylist of upper pipe
    upperPipe = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']}
    ]
    #mylist of lower pipe
    lowerPipe = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']}
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = -10
    playerMinVelY = -8
    playerAccVelY = -1

    playerFlapAccv = -8 #velocity while flapping
    playerFlapped = False #Its true only while player flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.type == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
        crashTest = isCollide(playerx, playery, upperPipe, lowerPipe)#This function will return true if the player crash
        if crashTest:
            return
        
        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipe:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}")

        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccVelY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pips to left 
        for upperPipe, lowerPipe in zip(upperPipe, lowerPipe):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX


        # add a new pipe when the first pipe is about to cross the leftmost part of screen 
        if upperPipe and 0 < upperPipe[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipe.append(newpipe[0])
            lowerPipe.append(newpipe[1])


        # if the pipe out of screen remove
        if upperPipe[0]['x']< -GAME_SPRITES['pipe'][0].get_width():
            upperPipe.pop(0)
            lowerPipe.pop(0)
        
        # lets blit out sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipe, lowerPipe):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))


        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipe, lowerPipe):
    return False
#generate position of two pipe(one bottom and top rotated) for blitting on the screen
def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2*offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper pipe
        {'x': pipeX, 'y': y2} #lower pipe
    ]    
    return pipe


if __name__ == "__main__":
    #This will be the main point where our game will start
    pygame.init()#Initilize all pygame's modeules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('FlappyBird by Ashrya')
    GAME_SPRITES['base'] = pygame.image.load('imgs/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() #Shows welcome screen to user until he press a buttom
        mainGame()
     