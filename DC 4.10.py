import pygame
import random

#set up pygame stuff
pygame.init()  
pygame.display.set_caption("top down game")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

#game variables
timer = 0 #used for sheep movement
score = 0
gameover = False

#images and fonts
SheepPic = pygame.image.load("sheep.jpg")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Score:', True, (200, 200, 0))
text2 = font.render(str(score), True, (200, 200, 0))
text3 = font.render('YOU WIN!', True, (200, 200, 0))

#CONSTANTS (not required, just makes code easier to read)
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

#function defintions------------------------------------
#can you tell me what the parameters are for these functions, and what they return (if anything)?

class Sheep():
    def __init__(self,sheepx,sheepy,direction,sheepcaught):
        self.direction = direction
        self.sheepx = sheepx
        self.sheepy = sheepy
        self.sheepcaught = sheepcaught
    def sheepMove(self):
        if timer % 50 == 0: #only change direction every 50 game loops
            self.direction = random.randrange(0, 4) #set random direction
        if self.direction == LEFT and self.sheepx > 0:
            self.sheepx -= 2 #move left
        elif self.direction == RIGHT and self.sheepx+70 < 800:
            self.sheepx += 2 #move right
        elif self.direction == UP and self.sheepy > 0: 
            self.sheepy -= 2 #move up
        elif self.direction == DOWN and self.sheepy+50 < 800:
            self.sheepy += 2 #move down
        return self.direction

    def collision(self,xpos,ypos):
        if (xpos+40 > self.sheepx 
            and xpos < self.sheepx+40 
            and ypos+40 > self.sheepy 
            and ypos < self.sheepy+40) and self.sheepcaught == False: #only catch uncaught sheeps!
            self.sheepcaught = True #catch da sheepies!
            global score #make it so this function can change this value
            score +=1
    def draw(self):
        if self.sheepcaught == False:
            screen.blit(SheepPic, (self.sheepx, self.sheepy))



#create sheep!
#numbers in list represent xpos, ypos, direction moving, and whether it's been caught or not!
sheepList = []
for i in range(6):
    sheepList.append(Sheep(i*100+75, i*100, RIGHT, False))
#make more sheeps here!



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity (left/right speed) of player
vy = 0 #y velocity (up/down speed) of player
keys = [False, False, False, False] #this list holds whether each key has been pressed

while gameover == False and score < 6: #GAME LOOP############################################################
    clock.tick(60) #FPS
    timer+=1
    
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

      
        #check if a key has been PRESSED
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True

        #check if a key has been LET GO
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
          
    #physics
    #section--------------------------------------------------------------------
    
    #player movement!--------
    if keys[LEFT] == True:
        vx = -3
    elif keys[RIGHT] == True:
        vx = 3
    elif keys[UP] == True:
        vy = -3
    elif keys[DOWN] == True:
        vy = 3
    else:
        vx = 0
        vy = 0


    #player movement!--------
    if keys[LEFT] == True:
        vx = -3
    elif keys[RIGHT] == True:
        vx = 3
    elif keys[UP] == True:
        vy = -3
    elif keys[DOWN] == True:
        vy = 3
    else:
        vy = 0
        vx = 0

    #player/sheep collision!
    for j in range(len(sheepList)):
        if sheepList[j].sheepcaught == False:
            sheepList[j].collision(xpos,ypos)

    #update player position
    xpos+=vx 
    ypos+=vy
    
    #update sheep position
    for sheeps in range(len(sheepList)):
        sheepList[sheeps].sheepMove()

  
    # RENDER
    # Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 40, 40))

    #draw sheep

    for sheeps in range(len(sheepList)):
        sheepList[sheeps].draw()
    
    #display score
    screen.blit(text, (20, 20))
    text2 = font.render(str(score), True, (200, 200, 0))#update score number
    screen.blit(text2, (140, 20))

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------

#end screen
screen.fill((0,0,0)) 
screen.blit(text3, (400,400))
pygame.display.flip()
pygame.time.wait(2000)#pause for a bit before ending

pygame.quit()
