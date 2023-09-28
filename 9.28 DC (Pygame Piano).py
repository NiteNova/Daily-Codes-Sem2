
import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False
key = -1

class WhiteKeys:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        self.press = False
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.xpos, self.ypos, 100, 300))
        pygame.draw.rect(screen, (0, 0, 0), (self.xpos, self.ypos, 100, 300), 2)
    def update(self):
        if self.press == True:
            pygame.draw.rect(screen, (150,150,150), (xpos,ypos,100,300))
    def play(self, k):
        self.press = True
    def letgo(self):
        self.press = False
    def givecoords(self):
        return self.xpos

#Instinate  Keys
keys = []    
for i in range(8):
    keys.append(WhiteKeys(i*100, 500))

#Audio section
pygame.mixer.init()
key_sounds = []
for a in range(len(keys)):
    key_sounds.append(pygame.mixer.Sound(f"key0{a}.mp3"))


#gameloop###################################################
while True:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    #update/timer section---------------------------------------    
    for g in range(len(keys)):
        h = keys[g].givecoords()
        if mousePos[0] > h and mousePos[1] > 500:
            key = g 
        else:
            key = -1
    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        press = True

    if event.type == pygame.MOUSEBUTTONUP:
        press = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos


    #render section---------------------------------------------

    #the keys 
    for j in range(len(keys)):
        keys[j].draw()

    #if a key is pressed, highlight in grey and play the sound:
    if press == True:
        for p in range (len(keys)):
            if key == -1:
                print("no key")
            elif key == p:
                keys[p].update()
                pygame.mixer.Sound.play(key_sounds[p])
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()
