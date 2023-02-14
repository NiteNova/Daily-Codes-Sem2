
#pygame hearts
#gets you started to draw a valentine's day card

import pygame #gaming module (aka library) 
import timer
import random
pygame.init() #initializes Pygame
pygame.display.set_caption("Valentine's day card") #sets the window title
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800)) #creates game screen
font = pygame.font.Font('freesansbold.ttf', 32) #load font
img = pygame.image.load("dog.jpg") #make sure this is saved to the same folder as your code

windowOpen = True

class heart:
    def __init__ (self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.xpos, self.ypos), 20) #top left circle
        pygame.draw.circle(screen, (255, 0, 0), (self.xpos + 40, self.ypos), 20) #top right circle
        pygame.draw.polygon(screen, (255, 0, 0), ((self.xpos-20, self.ypos+5),(self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50))) #triangle to form base
    def move(self):
        if self.ypos >= 800:
            self.ypos = 0
            return self.ypos
        self.ypos += 1
        
h1 = heart(180, 200)
h2 = heart(300, 200)
h3 = heart(250, 50)

hearts = []
for i in range (70):
    hearts.append(heart(random.randrange(10, 750), (random.randrange(10, 750))))

#game loop goes here

while windowOpen == True:
    
            
            
    screen.fill((0, 0, 0))
    
    for i in range (len(hearts)):
        hearts[i].draw()
    for i in range (len(hearts)):
        hearts[i].move()

    
    
    #text
    text1 = font.render('I Love You!', True, (250, 100, 100)) #numbers give color
    text2 = font.render('Happy Valentines Day', True, (250, 0, 0), (200,150,150)) #this one includes background color
    screen.blit(text1, (200, 100)) #numbers give position
    screen.blit(text2, (400, 300))


    
    
    pygame.display.flip() #this flips all those shapes onto the game screen (needed for every game)
pygame.quit()



