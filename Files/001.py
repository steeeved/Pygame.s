import pygame

pygame.init()

#window
win = pygame.display.set_mode((500, 500))
#name of the game
pygame.display.set_caption("Caroline Wanjiku")

x = 50
y = 420
width = 40
height = 60
vel = 15

is_jump = False
jumpcount = 10

#game play
run = True
while run:
    pygame.time.delay(100)
    #checking for events that occur during the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #checking what keys have been pressed 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if not(is_jump):
        if keys[pygame.K_UP] and y > 5:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            is_jump = True
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

    #filling to avoid streaching
    win.fill((0, 0, 0))
    #DRAWING OBJECTS IN THE GAME. Start with window(win), colour, location & size
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()