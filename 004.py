#OBJECT ORIENTED APPROACH
#Collisions
import pygame

pygame.init()

#window
win = pygame.display.set_mode((500, 480))
#name of the game
pygame.display.set_caption("Caroline Wanjiku")

clock = pygame.time.Clock()

# loading the splites
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.is_jump = False
        self.jumpcount = 10
        self.left = False
        self.right = False
        self.walkcount = 0
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        #DRAWING OBJECTS IN THE GAME. Start with window(win), colour, location & size
        if self.walkcount + 1 >= 27:
            self.walkcount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
            elif self.right:
                win.blit(walkRight[self.walkcount//3], (self.x,self.y))
                self.walkcount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        self.move()
        if self.walkcount + 1 >= 33:
            self.walkcount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkcount//3], (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(self.walkLeft[self.walkcount//3], (self.x, self.y))
            self.walkcount += 1
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]: 
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkcount = 0

    def hit(self):
        print("hit!")

def gamewindow():
    #filling to avoid streaching
    win.blit(bg, (0,0))
    carol.draw(win)
    charlie.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

#game play
carol = player(300, 410, 64, 64)
charlie = enemy(100, 410, 64, 64, 450)
shootloop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    #checking for events that occur during the game
    if shootloop > 0:
        shootloop += 1
    if shootloop > 3:
        shootloop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < charlie.hitbox[1] + charlie.hitbox[3] and bullet.y + bullet.radius > charlie.hitbox[1]:
            if bullet.x + bullet.radius > charlie.hitbox[0] and bullet.x - bullet.radius < charlie.hitbox[0] + charlie.hitbox[2]:
                charlie.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    #checking what keys have been pressed 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootloop == 0:
        if carol.left:
            facing = -1
        else: 
            facing = 1
        if len(bullets) < 7:
            bullets.append(projectile(round(carol.x  + carol.width//2), round(carol.y + carol.height//2), 6, (0,0,0), facing))
        shootloop = 1

    if keys[pygame.K_LEFT] and carol.x > carol.vel:
        carol.x -= carol.vel
        carol.left = True
        carol.right = False
        carol.standing = False
    elif keys[pygame.K_RIGHT] and carol.x < 500 - carol.width - carol.vel:
        carol.x += carol.vel
        carol.right = True
        carol.left = False
        carol.standing = False
    else:
        carol.standing = True
        carol.walkcount = 0
    if not(carol.is_jump):
        if keys[pygame.K_UP]:
            carol.is_jump = True
            carol.standing = True
            carol.walkcount = 0
    else:
        if carol.jumpcount >= -10:
            neg = 1
            if carol.jumpcount < 0:
                neg = -1
            carol.y -= (carol.jumpcount ** 2) * 0.5 * neg
            carol.jumpcount -= 1
        else:
            carol.is_jump = False
            carol.jumpcount = 10

    gamewindow()

pygame.quit()
