import pygame

pygame.init()

#window
win = pygame.display.set_mode((500, 480))
#name of the game
pygame.display.set_caption("Caroline Wanjiku")

clock = pygame.time.Clock()
x = 50
y = 400
width = 64
height = 64
vel = 8

is_jump = False
jumpcount = 10

left = False
right = False
walkcount = 0

# loading the images
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


def gamewindow():
    global walkcount
    #filling to avoid streaching
    win.blit(bg, (0,0))
    #DRAWING OBJECTS IN THE GAME. Start with window(win), colour, location & size
    if walkcount + 1 >= 27:
        walkcount = 0
    
    if left:
        win.blit(walkLeft[walkcount//3], (x,y))
        walkcount += 1
    elif right:
        win.blit(walkRight[walkcount//3], (x,y))
        walkcount += 1
    else:
        win.blit(char, (x,y))
    pygame.display.update()

#game play
run = True
while run:
    clock.tick(27)
    #checking for events that occur during the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #checking what keys have been pressed 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkcount = 0
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            right = False
            left = False
            walkcount = 0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            is_jump = False
            jumpcount = 10

    gamewindow()

pygame.quit()