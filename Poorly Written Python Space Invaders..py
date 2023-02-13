import pygame
import timer
import random

pygame.init()
pygame.display.set_caption("Space Invaders!")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False

#game variables
timer = 0;

#player variables
xpos = 400
ypos = 750
moveLeft = False
moveRight = False
shoot = False

#Bullet Class
class Bullet:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = False
    
    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos -= 7
        if self.ypos < 0:
            self.isAlive = False 
            self.xpos = xpos
            self.ypos = ypos
    

    def draw(self):
        pygame.draw.rect(screen, (250, 250, 250), (self.xpos-3, self.ypos-50, 10, 20))
        
bullet = Bullet(xpos+28, ypos)

#Missile Class
class missile:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos - 10
        self.ypos = ypos - 10
        self.isAlive = False

    def move(self, xpos, ypos):
        if self.isAlive == True:
            self.ypos += 5
        if self.ypos > 800:
            self.isAlive = False
            self.xpos = xpos - 10
            self.ypos = ypos - 10
            
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(screen, (250, 100, 0), (self.xpos, self.ypos, 10, 20))



#Enemy Class 
class Alien: 
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    def draw(self):
        if self.isAlive == True:
            pygame.draw.rect(screen, (250, 250, 250), (self.xpos, self.ypos, 40, 40))
        
        
    def move(self, timer):
        #print("timer in function is", timer)
        if timer % 650 == 0:
            self.ypos+= 100
            self.direction *=-1
            return 0
        
        if timer % 350 == 0:
            self.xpos+=20*self.direction
        return timer
    
    def collide (self, BulletX, BulletY):
        if self.isAlive:
            if (BulletX > self.xpos-10 and BulletX < self.xpos + 40 and BulletY < self.ypos + 70):
                print("hit!")
                self.isAlive = False
                return False
        return True
             
#Wall Class
class Walls:
    numHits = 0
    def __init__(self, xpos, ypos, numHits):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.numHits = numHits
        
    def draw(self):
        if self.numHits == 0:
            pygame.draw.rect(screen, (255, 255, 0), (self.xpos, self.ypos, 30, 30))
        if self.numHits == 1:
            pygame.draw.rect(screen, (255, 155, 0), (self.xpos, self.ypos, 30, 30))
        if self.numHits == 2:
            pygame.draw.rect(screen, (255, 50, 0), (self.xpos, self.ypos, 30, 30))
        
    
    def collide(self, BulletX, BulletY):
        if self.numHits < 3:
            if (BulletX > self.xpos-10 and BulletX < self.xpos + 30 and BulletY < self.ypos+15):
                print("hit!")
                self.numHits += 1
                return self.numHits 
        return True

missiles = []
for p in range (9):
    missiles.append(missile(p*80+75, 100))

#Dictates how many walls there are        
walls = [] 
for k in range (4): #creates 4 sets
    for i in range (2):
        for j in range(3):
            walls.append(Walls(j*30+200*k+50, i*30+560, 0))

#Dictates how many enemies there are    
armada = []
for m in range (4): #handles rows
    for n in range (9): #handles columns
        armada.append(Alien(n*80+50, m*60+50))


while not gameover: #GAME LOOP------------------------------------------------------------------------------------
    clock.tick(60)#fps
    timer += 1
    #print("timer in the game loop is", timer)
    

    #Input Section -------------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveRight = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moveRight = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True
               
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shoot = False

    
    #Physics Section -----------------------------------------------------------
    if moveLeft == True:
        vx =- 5
    elif moveRight == True:
        vx = 5
    else:
        vx = 0
    #update player position
    xpos += vx    
    
    #Alien movement
    for i in range (len(armada)):
        timer = armada[i].move(timer)
    
    for g in range (len(missiles)):
        missiles[g].move(xpos, ypos)
    
    #Alien Missiles
    chance = random.randrange(100)
    if chance < 2:
        pick = random.randrange(len(armada))
        if armada[pick].isAlive == True:
            for i in range(len(missiles)):
                if missiles[i].isAlive == False:
                    missiles[i].isAlive = True
                    missiles[i].xpos = armada[pick].xpos+5
                    missiles[i].ypos = armada[pick].ypos
                    break
                    
    
    
    #shoot bullet
    if shoot == True:
        bullet.isAlive = True
    
    if bullet.isAlive == True:
        bullet.move(xpos+28, ypos)
        if bullet.isAlive == True:
            #check for collision between bullet and enemy
            for i in range (len(armada)): #check bullet with entire armada's position
                bullet.isAlive = armada[i].collide(bullet.xpos, bullet.ypos) #if we hit, set bullet to false
                if bullet.isAlive == False:
                    break

        if bullet.isAlive == True:
            #check for collision between bullet and walls
            for i in range (len(walls)): #check bullet with entire walls' position
                bullet.isAlive = walls[i].collide(bullet.xpos, bullet.ypos) #if we hit, set bullet to false
                if bullet.isAlive == False:
                    break
        
    else:
        bullet.xpos = xpos + 28
        bullet.ypos = ypos
    
    #Render Section ------------------------------------------------------------
    screen.fill((0, 0, 0))
    
    #Draws the player
    pygame.draw.rect(screen, (50, 205, 0), (xpos, ypos, 60, 20))
    pygame.draw.rect(screen, (50, 205, 0), (xpos+5, ypos-10, 50, 20))
    pygame.draw.rect(screen, (50, 205, 0), (xpos+22, ypos-25, 15, 25))
    pygame.draw.rect(screen, (50, 205, 0), (xpos+27, ypos-35, 5, 10))
    
    bullet.draw()
    
    #Draws the missiles
    for p in range(len(missiles)):
        missiles[p].draw()
    
    #Draws the walls
    for k in range(len(walls)):
        walls[k].draw()
    
    #Draws the aliens
    for i in range(len(armada)):
        armada[i].draw()
    
    pygame.display.flip()
# END OF GAME LOOP------------------------------------------------------------------------------------------------
pygame.quit()
