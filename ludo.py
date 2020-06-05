# made by:- Tushar Gupta
# Classic Ludo game made in python using pygame library
# INDIAN INSTITUTE OF INFORMATION TECHNOLOGY, ALLAHABAD


#importing the library
import pygame
pygame.init()
from random import randint

#creating the window
win = pygame.display.set_mode((532, 560))
pygame.display.set_caption("Ludo")
clock = pygame.time.Clock()


#importing the art
mouse = [pygame.image.load('data/mouse.png')]
ludo = [pygame.image.load('data/ludo.jpg')]
Blue = [pygame.image.load('data/b.png')]
green = blue = [pygame.image.load('data/g1.png')]
red = [pygame.image.load('data/r1.png')]
yellow = [pygame.image.load('data/y1.png')]
inst = [pygame.image.load('data/inst.png')]
play = [pygame.image.load('data/play.png')]
exiti = [pygame.image.load('data/exit.png')]
menu = [pygame.image.load('data/menu.png')]
instructions = [pygame.image.load('data/instructions.png')]
back =[pygame.image.load('data/back.png')]
dice = [pygame.image.load('data/one.png'),pygame.image.load('data/two.png'),pygame.image.load('data/three.png'),pygame.image.load('data/four.png'),pygame.image.load('data/five.png'),pygame.image.load('data/six.png')]
music = pygame.mixer.music.load('data/bkmusic.mp3')
pygame.mixer.music.play(-1)
winner = [pygame.image.load('data/winner.png')]
tik = pygame.mixer.Sound('data/tik.wav')
value = -2

#defining the positions of the tiles
#x position
greenx = [38, 73, 110, 145, 180, 215, 215, 215, 215, 215, 215, 250, 286, 286, 286, 286, 286, 286, 322, 357, 393, 429, 464, 500, 500, 500, 464, 429, 393, 357, 322, 286, 286, 286, 286, 286, 286, 250, 215, 215, 215, 215, 215, 215, 180, 145, 110, 73, 38, 3, 3, 38, 73, 110, 145, 180]
yellowx = [286, 286, 286, 286, 286, 322, 357, 393, 429, 464, 500, 500, 500, 464, 429, 393, 357, 322, 286, 286, 286, 286, 286, 286, 250, 215, 215, 215, 215, 215, 215, 180, 145, 110, 73, 38, 3, 3, 3, 38, 73, 110, 145, 180, 215, 215, 215, 215, 215, 215, 250, 250, 250, 250, 250, 250]
bluex = [464, 429, 393, 357, 322, 286, 286, 286, 286, 286, 286, 250, 215, 215, 215, 215, 215, 215, 180, 145, 110, 73, 38, 3, 3, 3, 38, 73, 110, 145, 180, 215, 215, 215, 215, 215, 215, 250, 286, 286, 286, 286, 286, 286, 322, 357, 393, 429, 464, 500, 500, 464, 429, 393, 357, 322]
redx = [215, 215, 215, 215, 215, 180, 145, 110, 73, 38, 3, 3, 3, 38, 73, 110, 145, 180, 215, 215, 215, 215, 215, 215, 250, 286, 286, 286, 286, 286, 286, 322, 357, 393, 429, 464, 500, 500, 500, 464, 429, 393, 357, 322, 286, 286, 286, 286, 286, 286, 250, 250, 250, 250, 250, 250]
#y position
greeny = [215, 215, 215, 215, 215, 179, 144, 109, 74, 39, 3, 3, 3, 39, 74, 109, 144, 179, 215, 215, 215, 215, 215, 215, 251, 287, 287, 287, 287, 287, 287, 323, 358, 393, 428, 463, 500, 500, 500, 463, 428, 393, 358, 323, 287, 287, 287, 287, 287, 287, 251, 251, 251, 251, 251, 251]
yellowy = [39, 74, 109, 144, 179, 215, 215, 215, 215, 215, 215, 251, 287, 287, 287, 287, 287, 287, 323, 358, 393, 428, 463, 500, 500, 500, 463, 428, 393, 358, 323, 287, 287, 287, 287, 287, 287, 251, 215, 215, 215, 215, 215, 215, 179, 144, 109, 74, 39, 3, 3, 39, 74, 109, 144, 179]
bluey = [287, 287, 287, 287, 287, 323, 358, 393, 428, 463, 500, 500, 500, 463, 428, 393, 358, 323, 287, 287, 287, 287, 287, 287, 251, 215,215, 215, 215, 215, 215, 179, 144, 109, 74, 39, 3, 3, 3, 39, 74, 109, 144, 179, 215, 215, 215, 215, 215, 215, 251, 251, 251, 251, 251, 251]
redy = [463, 428, 393, 358, 323, 287, 287, 287, 287, 287, 287, 251, 215, 215, 215, 215, 215, 215, 179, 144, 109, 74, 39, 3, 3, 3, 39, 74, 109, 144, 179, 215, 215, 215, 215, 215, 215, 251, 287, 287, 287, 287, 287, 287, 323, 358, 393, 428, 463, 500, 500, 463, 428, 393, 358, 323]


a = 1
b = 1
c = 1
d = 1

#defining the tockens
class player(object):
    def __init__ (self, x, y, tocken):
        self.x = x
        self.y = y
        self.tocken = tocken

    def draw(self, win):
        win.blit(self.tocken, (self.x,self.y))

#draw the window
def drawscreen(value, sxa, sya):
    win.blit(ludo[0], (0,0))
    win.blit(dice[value-1], (238, 238))
    for i in greenk:
        i.draw(win)
    for j in bluek:
        j.draw(win)
    for i in yellowk:
        i.draw(win)
    for j in redk:
        j.draw(win)

    if a == 2:
        win.blit(winner[0], (0, 0))
    if b == 2:
        win.blit(winner[0], (320, 0))
    if c == 2:
        win.blit(winner[0], (320, 320))
    if d == 2:
        win.blit(winner[0], (0, 320))
    win.blit(mouse[0], (sxa,sya))
        
    pygame.display.update()

    
#draw the menu page
def Drawmenu():
    win.blit(ludo[0], (0,0))
    win.blit(menu[0], (207, 90))
    win.blit(play[0], (175, 150))
    win.blit(inst[0], (175, 225))
    win.blit(exiti[0], (175, 300))
    pygame.display.update()

    
#draw the instruction page
def instruction():
    win.blit(ludo[0], (0,0))
    win.blit(back[0], (450, 10))
    win.blit(instructions[0], (57,73))
    pygame.display.update()


sx = -110
sy = -189
#main loop
font = pygame.font.SysFont('comiccsans', 40, True)
i = 1
run = False
Drawmenu()

#printing the menu page
while not(run):
    clock.tick(27)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            #defining the buttons
            if x > 180 and x <355:
                if y > 155 and y < 215:
                    run = True
                if y > 240 and y < 275:
                    instruction()
                    ze = True
                    while ze:
                        for eve in pygame.event.get():
                            if eve.type == pygame.QUIT:
                                pygame.quit()
                            
                            if eve.type == pygame.MOUSEBUTTONDOWN:
                                mx, my = pygame.mouse.get_pos()
                                if mx > 450 and mx < 510:
                                    if my > 10 and my < 70:
                                        ze = False
                                        Drawmenu()
                if y > 305 and y < 365:
                    pygame.quit()


#create tockens for different colors
#key = player(x-position, y-position, tocken)
#green
g1 = player(56, 56, green[0])
g3 = player(56, 128, green[0])
g2 = player(127, 56, green[0])
g4 = player(127, 128, green[0])
#blue
b3 = player(376, 446, Blue[0])
b1 = player(376, 376, Blue[0])
b4 = player(447,446, Blue[0])
b2 = player(447, 376, Blue[0])
#red
r1 = player(56, 376, red[0])
r2 = player(127, 376, red[0])
r3 = player(56, 446, red[0])
r4 = player(127, 446, red[0])
#yellow
y1 = player(376, 56, yellow[0])
y2 = player(447, 56, yellow[0])
y3 = player(376, 128, yellow[0])
y4 = player(447, 128, yellow[0])
            
greenk = [g1, g2, g3, g4]
yellowk = [y1, y2, y3, y4]
redk = [r1, r2, r3, r4]
bluek = [b1, b2, b3, b4]

gpos = [1, 1, 1, 1]
ypos = [1, 1, 1, 1]
rpos = [1, 1, 1, 1]
bpos = [1, 1, 1, 1]

#initialising the tockens in the house
#green
g1x = -1
g2x = -1
g3x = -1
g4x = -1

#yellow
y1x = -1
y2x = -1
y3x = -1
y4x = -1

#red
r1x = -1
r2x = -1
r3x = -1
r4x = -1

#blue
b1x = -1
b2x = -1
b3x = -1
b4x = -1

#define variables
blah = 0
turn = True
move = 0
wait = False
drawscreen(6, -100,-100)
click = False
done = False

#main game loop
while run:
    xcor = -100
    ycor = -100

    #checking who's winner
    if a == 1:
        blaha = 0
        for p in gpos:
            if p == 3:
                blaha += 1
            else:
                a = 1
        if blaha == 4:
            a = 2

    if b == 1:
        blahb = 0
        for p in ypos:
            if p == 3:
                blahb += 1
            else:
                b = 1
        if blahb == 4:
            b = 2
            
    if c == 1:
        blahc = 0
        for p in bpos:
            if p == 3:
                blahc += 1
            else:
                c = 1
        if blahc == 4:
            c = 2
                
    if d == 1:
        blahd = 0
        for p in rpos:
            if p == 3:
                blahd += 1
            else:
                d = 1
        if blahd == 4:
            d = 2

    if i == 5:
        i = 1

    if a == 2 and i == 1:
        i += 1

    if b == 2 and i == 2:
        i += 1

    if c == 2 and i == 3:
        i += 1

    if d == 2 and i == 4:
        i += 1
        
    clock.tick(100)
        
    #printing the text (whose chance)    
    if i == 1:
        win.fill((0,0,0))
        text = font.render('Player: Green', 1, (255, 255, 255))
        win.blit(text, (10, 534))
    elif i == 2:
        win.fill((0,0,0))
        text = font.render('Player: Yellow', 1, (255, 255, 255))
        win.blit(text, (10, 534))
    elif i == 3:
        win.fill((0,0,0))
        text = font.render('Player: Blue', 1, (255, 255, 255))
        win.blit(text, (10, 534))
    elif i == 4:
        win.fill((0,0,0))
        text = font.render('Player: Red', 1, (255, 255, 255))
        win.blit(text, (10, 534))    
    
    #checking for the event quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    #Rolling the dice
    if turn == True:
            keys = pygame.key.get_pressed()
            click = False
            drawscreen(blah,sx,sy)
            for _ in range(10):
                    blah = randint(1, 6)
            clock.tick(30)
            if keys[pygame.K_SPACE]:
                    done = True
                    value = blah
                    wait = True
                    turn = False
    drawscreen(value,sx,sy)

    count = 0

    while wait == True:
        for eventi in pygame.event.get():

            if eventi.type == pygame.QUIT:
                pygame.quit()
            
            #getting the mouse position
            if eventi.type == pygame.MOUSEBUTTONUP:
                sx, sy = pygame.mouse.get_pos()
                click = True
                wait = False
             
    if click:
        print('',end='')
        if i == 5:
                    i = 1
        
        #if we select green
        if i == 1:
                    #finding which tocken we select out of 4 tockens
                    if done:
                        if sx > g1.x and sx <g1.x +30:
                            if sy > g1.y and sy <g1.y + 30:
                                wait = False
                                
                                #if tocken is inside wait till dice rolls to 1
                                if gpos[0] == 1:
                                    if value == 1:
                                        g1x += value
                                        gpos[0] = 2                                                                        
                                        g1.x = greenx[g1x-1]
                                        g1.y = greeny[g1x-1]
                                        done = False
                                
                                #if tocken is out of the house do the following
                                if gpos[0] == 2:
                                    #if dice rolls to 6 you get a chance
                                    if value == 6:
                                        i -= 1
                                    g1x += value
                                    if g1x > 56:
                                        if g1x == 57:
                                            g1.x = 1000
                                            gpos[0] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            g1x -= value
                                    else:
                                        g1.x = greenx[g1x-1]
                                        g1.y = greeny[g1x-1]
                                        xcor = g1.x
                                        ycor = g1.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                    #same as the first one
                    if done:
                        if sx > g2.x and sx <g2.x +30:
                            if sy > g2.y and sy <g2.y + 30:
                                wait = False
                                if gpos[1] == 1:
                                    if value == 1:
                                        g2x += value
                                        gpos[1] = 2
                                        done = False
                                        g2.x = greenx[g2x-1]
                                        g2.y = greeny[g2x-1]                                    
                                if gpos[1] == 2:
                                    if value == 6:
                                        i -= 1
                                    g2x += value
                                    if g2x > 56:
                                        if g2x == 57:
                                            g2.x = 1000
                                            gpos[1] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            g2x -= value
                                    else:
                                        g2.x = greenx[g2x-1]
                                        g2.y = greeny[g2x-1]
                                        xcor = g2.x
                                        ycor = g2.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                

                    if done:   
                        if sx > g3.x and sx <g3.x +30:
                            if sy > g3.y and sy <g3.y + 30:
                                wait = False
                                if gpos[2] == 1:
                                    if value == 1:
                                        g3x += value
                                        gpos[2] = 2
                                        done = False
                                        g3.x = greenx[g3x-1]
                                        g3.y = greeny[g3x-1]
                                if gpos[2] == 2:
                                    if value == 6:
                                        i -= 1
                                    g3x += value
                                    if g3x > 56:
                                        if g3x == 57:
                                            g3.x = 1000
                                            gpos[2] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            g3x -= value
                                    else:
                                        g3.x = greenx[g3x-1]
                                        g3.y = greeny[g3x-1]
                                        xcor = g3.x
                                        ycor = g3.y        
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                

                    if done:
                        if sx > g4.x and sx <g4.x +30:
                            if sy > g4.y and sy <g4.y + 30:
                                wait = False
                                if gpos[3] == 1:
                                    if value == 1:
                                        g4x += value
                                        done = False
                                        gpos[3] = 2
                                        g4.x = greenx[g4x-1]
                                        g4.y = greeny[g4x-1]

                                        
                                if gpos[3] == 2:
                                    if value == 6:
                                        i -= 1
                                    g4x += value
                                    if g4x > 56:
                                        if g4x == 57:
                                            g4.x = 1000
                                            gpos[3] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            g4x -= value
                                    else:
                                        g4.x = greenx[g4x-1]
                                        g4.y = greeny[g4x-1]
                                        xcor = g4.x
                                        ycor = g4.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1

                    #checking if the tocken is on the safe position or not
                    ouch = True
                    if xcor == 38 and ycor == 215:
                        ouch = False
                    if xcor == 73 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 74:
                        ouch = False
                    if xcor == 286 and ycor == 39:
                        ouch = False
                    if xcor == 429 and ycor == 215:
                        ouch = False
                    if xcor == 464 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 463:
                        ouch = False
                    if xcor == 286 and ycor == 428:
                        ouch = False

                    #if tocken is not on the same position check if it kicks off other player tocken or not
                    if ouch:
                        if xcor == y1.x and ycor == y1.y:
                            tik.play()
                            y1.x = 376
                            y1.y = 56
                            ypos[0] = 1
                            y1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y2.x and ycor == y2.y:
                            tik.play()
                            y2.x = 447
                            y2.y = 56
                            ypos[1] = 1
                            y2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y3.x and ycor == y3.y:
                            tik.play()
                            y3.x = 376
                            y3.y = 128
                            ypos[2] = 1
                            y3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y4.x and ycor == y4.y:
                            tik.play()
                            y4.x = 447
                            y4.y = 128
                            ypos[3] = 1
                            y4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b1.x and ycor == b1.y:
                            tik.play()
                            b1.x = 376
                            b1.y = 376
                            bpos[0] = 1
                            b1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b2.x and ycor == b2.y:
                            tik.play()
                            b2.x = 447
                            b2.y = 376
                            bpos[1] = 1
                            b2x = -1
                            if value != 6:
                                i -= 1                 
                        if xcor == b3.x and ycor == b3.y:
                            tik.play()
                            b3.x = 376
                            b3.y = 446
                            bpos[2] = 1
                            b3x = -1
                        if xcor == b4.x and ycor == b4.y:
                            tik.play()
                            b4.x = 447
                            b4.y = 446
                            bpos[3] = 1
                            b4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r1.x and ycor == r1.y:
                            tik.play()
                            r1.x = 56
                            r1.y = 376
                            rpos[0] = 1
                            r1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r2.x and ycor == r2.y:
                            tik.play()
                            r2.x = 127
                            r2.y = 376
                            rpos[1] = 1
                            r2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r3.x and ycor == r3.y:
                            tik.play()
                            r3.x = 56
                            r3.y = 446
                            rpos[2] = 1
                            r3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r4.x and ycor == r4.y:
                            tik.play()
                            r4.x = 127
                            r4.y = 446
                            rpos[3] = 1
                            r4x = -1
                            if value != 6:
                                i -= 1
        
        #same as the first one
        elif i == 2:
                    if done:
                        if sx > y1.x and sx <y1.x +30:
                            if sy > y1.y and sy <y1.y + 30:
                                wait = False
                                if ypos[0] == 1:
                                    if value == 1:
                                        y1x += value
                                        ypos[0] = 2
                                        done = False
                                        y1.x = yellowx[y1x-1]
                                        y1.y = yellowy[y1x-1]

                                if ypos[0] == 2:
                                    if value == 6:
                                        i -= 1
                                    y1x += value
                                    if y1x > 56:
                                        if y1x == 57:
                                            y1.x = 1000
                                            ypos[0] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            y1x -= value
                                    else:
                                        y1.x = yellowx[y1x-1]
                                        y1.y = yellowy[y1x-1]
                                        xcor = y1.x
                                        ycor = y1.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                
                    if done:   
                        if sx > y2.x and sx <y2.x +30:
                            if sy > y2.y and sy <y2.y + 30:
                                wait = False
                                if ypos[1] == 1:
                                    if value == 1:
                                        y2x += value
                                        ypos[1] = 2
                                        done = False
                                        y2.x = yellowx[y2x-1]
                                        y2.y = yellowy[y2x-1]                                    
                                if ypos[1] == 2:
                                    if value == 6:
                                        i -= 1
                                    y2x += value
                                    if y2x > 56:
                                        if y2x == 57:
                                            y2.x = 1000
                                            ypos[1] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            y2x -= value
                                    else:
                                        y2.x = yellowx[y2x-1]
                                        y2.y = yellowy[y2x-1]
                                        xcor = y2.x
                                        ycor = y2.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                

                    if done:   
                        if sx > y3.x and sx <y3.x +30:
                            if sy > y3.y and sy <y3.y + 30:
                                wait = False
                                if ypos[2] == 1:
                                    if value == 1:
                                        y3x += value
                                        done = False
                                        ypos[2] = 2
                                        y3.x = yellowx[y3x-1]
                                        y3.y = yellowy[y3x-1]
                                if ypos[2] == 2:
                                    if value == 6:
                                        i -= 1
                                    y3x += value
                                    if y3x > 56:
                                        if y3x == 57:
                                            y3.x = 1000
                                            ypos[2] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            y3x -= value
                                    else:
                                        y3.x = yellowx[y3x-1]
                                        y3.y = yellowy[y3x-1]
                                        xcor = y3.x
                                        ycor = y3.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                

                    if done:
                        if sx > y4.x and sx <y4.x +30:
                            if sy > y4.y and sy <y4.y + 30:
                                wait = False
                                if ypos[3] == 1:
                                    if value == 1:
                                        y4x += value
                                        ypos[3] = 2
                                        done = False
                                        y4.x = yellowx[y4x-1]
                                        y4.y = yellowy[y4x-1]

                                        
                                if ypos[3] == 2:
                                    if value == 6:
                                        i -= 1
                                    y4x += value
                                    if y4x > 56:
                                        if y4x == 57:
                                            y4.x = 1000
                                            ypos[3] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            y4x -= value
                                    else:
                                        y4.x = yellowx[y4x-1]
                                        y4.y = yellowy[y4x-1]
                                        xcor = y4.x
                                        ycor = y4.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                

                    ouch = True
                    if xcor == 38 and ycor == 215:
                        ouch = False
                    if xcor == 73 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 74:
                        ouch = False
                    if xcor == 286 and ycor == 39:
                        ouch = False
                    if xcor == 429 and ycor == 215:
                        ouch = False
                    if xcor == 464 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 463:
                        ouch = False
                    if xcor == 286 and ycor == 428:
                        ouch = False

                    if ouch:
                        if xcor == b1.x and ycor == b1.y:
                            tik.play()
                            b1.x = 376
                            b1.y = 376
                            bpos[0] = 1
                            b1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b2.x and ycor == b2.y:
                            tik.play()
                            b2.x = 447
                            b2.y = 376
                            bpos[1] = 1
                            b2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b3.x and ycor == b3.y:
                            tik.play()
                            b3.x = 376
                            b3.y = 446
                            bpos[2] = 1
                            b3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b4.x and ycor == b4.y:
                            tik.play()
                            b4.x = 447
                            b4.y = 446
                            bpos[3] = 1
                            b4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r1.x and ycor == r1.y:
                            tik.play()
                            r1.x = 56
                            r1.y = 376
                            rpos[0] = 1
                            r1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r2.x and ycor == r2.y:
                            tik.play()
                            r2.x = 127
                            r2.y = 376
                            rpos[1] = 1
                            r2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r3.x and ycor == r3.y:
                            tik.play()
                            r3.x = 56
                            r3.y = 446
                            rpos[2] = 1
                            r3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r4.x and ycor == r4.y:
                            tik.play()
                            r4.x = 127
                            r4.y = 446
                            rpos[3] = 1
                            r4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g1.x and ycor == g1.y:
                            tik.play()
                            g1.x = 56
                            g1.y = 56
                            gpos[0] = 1
                            g1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g2.x and ycor == g2.y:
                            tik.play()
                            g2.x = 127
                            g2.y = 56
                            gpos[1] = 1
                            g2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g3.x and ycor == g3.y:
                            tik.play()
                            g3.x = 56
                            g3.y = 128
                            gpos[2] = 1
                            g3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g4.x and ycor == g4.y:
                            tik.play()
                            g4.x = 127
                            g4.y = 128
                            gpos[3] = 1
                            g4x = -1
                            if value != 6:
                                i -= 1
                                
        elif i == 3:
                    if done:
                        if sx > b1.x and sx <b1.x +30:
                            if sy > b1.y and sy <b1.y + 30:
                                wait = False
                                if bpos[0] == 1:
                                    if value == 1:
                                        b1x += value
                                        done = False
                                        bpos[0] = 2                                                                        
                                        b1.x = bluex[b1x-1]
                                        b1.y = bluey[b1x-1]

                                if bpos[0] == 2:
                                    if value == 6:
                                        i -= 1
                                    b1x += value
                                    if b1x > 56:
                                        if b1x == 57:
                                            b1.x = 1000
                                            bpos[0] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            b1x -= value
                                    else:
                                        b1.x = bluex[b1x-1]
                                        b1.y = bluey[b1x-1]
                                        xcor = b1.x
                                        ycor = b1.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                
                    if done:    
                        if sx > b2.x and sx <b2.x +30:
                            if sy > b2.y and sy <b2.y + 30:
                                wait = False
                                if bpos[1] == 1:
                                    if value == 1:
                                        b2x += value
                                        done = False
                                        bpos[1] = 2
                                        b2.x = bluex[b2x-1]
                                        b2.y = bluey[b2x-1]                                    
                                if bpos[1] == 2:
                                    if value == 6:
                                        i -= 1
                                    b2x += value
                                    if b2x > 56:
                                        if b2x == 57:
                                            b2.x = 1000
                                            bpos[1] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            b2x -= value
                                    else:
                                        b2.x = bluex[b2x-1]
                                        b2.y = bluey[b2x-1]
                                        xcor = b2.x
                                        ycor = b2.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                

                    if done:
                        if sx > b3.x and sx <b3.x +30:
                            if sy > b3.y and sy <b3.y + 30:
                                wait = False
                                if bpos[2] == 1:
                                    if value == 1:
                                        b3x += value
                                        bpos[2] = 2
                                        done = False
                                        b3.x = bluex[b3x-1]
                                        b3.y = bluey[b3x-1]
                                if bpos[2] == 2:
                                    if value == 6:
                                        i -= 1
                                    b3x += value
                                    if b3x > 56:
                                        if b3x == 57:
                                            b3.x = 1000
                                            bpos[2] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            b3x -= value
                                    else:
                                        b3.x = bluex[b3x-1]
                                        b3.y = bluey[b3x-1]
                                        xcor = b3.x
                                        ycor = b3.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                    

                    if done:
                        if sx > b4.x and sx <b4.x +30:
                            if sy > b4.y and sy <b4.y + 30:
                                wait = False
                                if bpos[3] == 1:
                                    if value == 1:
                                        b4x += value
                                        done = False
                                        bpos[3] = 2
                                        b4.x = bluex[b4x-1]
                                        b4.y = bluey[b4x-1]

                                        
                                if bpos[3] == 2:
                                    if value == 6:
                                        i -= 1
                                    b4x += value
                                    if b4x > 56:
                                        if b4x == 57:
                                            b4.x = 1000
                                            bpos[3] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            b4x -= value
                                    else:
                                        b4.x = bluex[b4x-1]
                                        b4.y = bluey[b4x-1]
                                        xcor = b4.x
                                        ycor = b4.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                

                    ouch = True
                    if xcor == 38 and ycor == 215:
                        ouch = False
                    if xcor == 73 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 74:
                        ouch = False
                    if xcor == 286 and ycor == 39:
                        ouch = False
                    if xcor == 429 and ycor == 215:
                        ouch = False
                    if xcor == 464 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 463:
                        ouch = False
                    if xcor == 286 and ycor == 428:
                        ouch = False

                    if ouch:
                        if xcor == y1.x and ycor == y1.y:
                            tik.play()
                            y1.x = 376
                            y1.y = 56
                            ypos[0] = 1
                            y1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y2.x and ycor == y2.y:
                            tik.play()
                            y2.x = 447
                            y2.y = 56
                            ypos[1] = 1
                            y2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y3.x and ycor == y3.y:
                            tik.play()
                            y3.x = 376
                            y3.y = 128
                            ypos[2] = 1
                            y3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y4.x and ycor == y4.y:
                            tik.play()
                            y4.x = 447
                            y4.y = 128
                            ypos[3] = 1
                            y4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r1.x and ycor == r1.y:
                            tik.play()
                            r1.x = 56
                            r1.y = 376
                            rpos[0] = 1
                            r1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r2.x and ycor == r2.y:
                            tik.play()
                            r2.x = 127
                            r2.y = 376
                            rpos[1] = 1
                            r2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r3.x and ycor == r3.y:
                            tik.play()
                            r3.x = 56
                            r3.y = 446
                            rpos[2] = 1
                            r3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == r4.x and ycor == r4.y:
                            tik.play()
                            r4.x = 127
                            r4.y = 446
                            rpos[3] = 1
                            r4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g1.x and ycor == g1.y:
                            tik.play()
                            g1.x = 56
                            g1.y = 56
                            gpos[0] = 1
                            g1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g2.x and ycor == g2.y:
                            tik.play()
                            g2.x = 127
                            g2.y = 56
                            gpos[1] = 1
                            g2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g3.x and ycor == g3.y:
                            tik.play()
                            g3.x = 56
                            g3.y = 128
                            gpos[2] = 1
                            g3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g4.x and ycor == g4.y:
                            tik.play()
                            g4.x = 127
                            g4.y = 128
                            gpos[3] = 1
                            g4x = -1
                            if value != 6:
                                i -= 1
                                
        elif i == 4:
                    if done:
                        if sx > r1.x and sx <r1.x +30:
                            if sy > r1.y and sy <r1.y + 30:
                                wait = False
                                if rpos[0] == 1:
                                    if value == 1:
                                        r1x += value
                                        rpos[0] = 2
                                        done = False
                                        r1.x = redx[r1x-1]
                                        r1.y = redy[r1x-1]

                                if rpos[0] == 2:
                                    if value == 6:
                                        i -= 1
                                    r1x += value
                                    if r1x > 56:
                                        if r1x == 57:
                                            r1.x = 1000
                                            rpos[0] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            r1x -= value
                                    else:
                                        r1.x = redx[r1x-1]
                                        r1.y = redy[r1x-1]
                                        xcor = r1.x
                                        ycor = r1.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                
                    if done:   
                        if sx > r2.x and sx <r2.x +30:
                            if sy > r2.y and sy <r2.y + 30:
                                wait = False
                                if rpos[1] == 1:
                                    if value == 1:
                                        r2x += value
                                        rpos[1] = 2
                                        done = False
                                        r2.x = redx[r2x-1]
                                        r2.y = redy[r2x-1]                                    
                                if rpos[1] == 2:
                                    if value == 6:
                                        i -= 1
                                    r2x += value
                                    if r2x > 56:
                                        if r2x == 57:
                                            r2.x = 1000
                                            rpos[1] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            r2x -= value
                                    else:
                                        r2.x = redx[r2x-1]
                                        r2.y = redy[r2x-1]
                                        xcor = r2.x
                                        ycor = r2.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                

                    if done:  
                        if sx > r3.x and sx <r3.x +30:
                            if sy > r3.y and sy <r3.y + 30:
                                wait = False
                                if rpos[2] == 1:
                                    if value == 1:
                                        r3x += value
                                        done = False
                                        rpos[2] = 2
                                        r3.x = redx[r3x-1]
                                        r3.y = redy[r3x-1]
                                if rpos[2] == 2:
                                    if value == 6:
                                        i -= 1
                                    r3x += value
                                    if r3x > 56:
                                        if r3x == 57:
                                            r3.x = 1000
                                            rpos[2] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            r3x -= value
                                    else:
                                        r3.x = redx[r3x-1]
                                        r3.y = redy[r3x-1]
                                        xcor = r3.x
                                        ycor = r3.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1
                                
                                

                    if done:
                        if sx > r4.x and sx <r4.x +30:
                            if sy > r4.y and sy <r4.y + 30:
                                wait = False
                                if rpos[3] == 1:
                                    if value == 1:
                                        r4x += value
                                        done = False
                                        rpos[3] = 2
                                        r4.x = redx[r4x-1]
                                        r4.y = redy[r4x-1]

                                        
                                if rpos[3] == 2:
                                    if value == 6:
                                        i -= 1
                                    r4x += value
                                    if r4x > 56:
                                        if r4x == 57:
                                            r4.x = 1000
                                            rpos[3] = 3
                                            if value != 6:
                                                i -= 1
                                        else:
                                            r4x -= value
                        
                                    else:
                                        r4.x = redx[r4x-1]
                                        r4.y = redy[r4x-1]
                                        xcor = r4.x
                                        ycor = r4.y
                                done = False
                                turn = True
                                i += 1
                            else:
                                count += 1
                        else:
                            count += 1

                    ouch = True
                    if xcor == 38 and ycor == 215:
                        ouch = False
                    if xcor == 73 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 74:
                        ouch = False
                    if xcor == 286 and ycor == 39:
                        ouch = False
                    if xcor == 429 and ycor == 215:
                        ouch = False
                    if xcor == 464 and ycor == 287:
                        ouch = False
                    if xcor == 215 and ycor == 463:
                        ouch = False
                    if xcor == 286 and ycor == 428:
                        ouch = False

                    if ouch:
                        if xcor == y1.x and ycor == y1.y:
                            tik.play()
                            y1.x = 376
                            y1.y = 56
                            ypos[0] = 1
                            y1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y2.x and ycor == y2.y:
                            tik.play()
                            y2.x = 447
                            y2.y = 56
                            ypos[1] = 1
                            y2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y3.x and ycor == y3.y:
                            tik.play()
                            y3.x = 376
                            y3.y = 128
                            ypos[2] = 1
                            y3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == y4.x and ycor == y4.y:
                            tik.play()
                            y4.x = 447
                            y4.y = 128
                            ypos[3] = 1
                            y4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b1.x and ycor == b1.y:
                            tik.play()
                            b1.x = 376
                            b1.y = 376
                            bpos[0] = 1
                            b1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b2.x and ycor == b2.y:
                            tik.play()
                            b2.x = 447
                            b2.y = 376
                            bpos[1] = 1
                            b2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b3.x and ycor == b3.y:
                            tik.play()
                            b3.x = 376
                            b3.y = 446
                            bpos[2] = 1
                            b3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == b4.x and ycor == b4.y:
                            tik.play()
                            b4.x = 447
                            b4.y = 446
                            bpos[3] = 1
                            b4x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g1.x and ycor == g1.y:
                            tik.play()
                            g1.x = 56
                            g1.y = 56
                            gpos[0] = 1
                            g1x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g2.x and ycor == g2.y:
                            tik.play()
                            g2.x = 127
                            g2.y = 56
                            gpos[1] = 1
                            g2x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g3.x and ycor == g3.y:
                            tik.play()
                            g3.x = 56
                            g3.y = 128
                            gpos[2] = 1
                            g3x = -1
                            if value != 6:
                                i -= 1
                        if xcor == g4.x and ycor == g4.y:
                            tik.play()
                            g4.x = 127
                            g4.y = 128
                            gpos[3] = 1
                            g4x = -1
                            if value != 6:
                                i -= 1
    
    #checking if we select a valid position or not
    if count == 4:
            wait = True
