import pygame
import random

pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

map = [[random.randrange(0, 2)]*80 for i in range (80)]
print (map)

while True: #gameloop
    clock.tick(60)
    event = pygame.event.get()
    
    #input section
    for event in pygame.event.get():
        break
    #update section
    for i in range (80):
        for j in range(80):
            counter = 0
            if i < 79 and map[i+1][j] == 1: #check above
                counter += 1
            if j < 79 and map[i][j+1] == 1: #check right
                counter += 1
            if i < 79 and j < 79 and map[i+1][j+1] == 1: #check top right corner
                counter += 1
            if i <79 and j >= 0 and map[i+1][j-1] == 1: #check top left corner
                counter += 1
                
            if i > 0 and map[i-1][j] == 1: #check down
                counter += 1
            if j > 0 and map[i][j-1] == 1: #check left
                counter += 1    
            if i >= 0 and j < 79 and map[i-1][j-1] == 1: #bottom right corner
                counter += 1
            if i >=0  and j <79 and map[i-1][j+1] == 1: #bottom left corner
                counter += 1
                
            if map[i][j] == 1 and counter <= 1:
                map[i][j] = 0
                #print("I died from loneliness guh")
            if map[i][j] == 1 and counter >=4:
                map[i][j] = 0
               # print("I died from overcrowding guh")           
            if map[i][j] == 0 and counter ==3:
                map[i][j] = 1
                #print("i baby")    
    
    #pygame.time.wait(200)
    
    
    #render section
    screen.fill((0,0,0))
    
    for i in range (80):
        for j in range(80):
            if map[i][j]==0:
                pygame.draw.rect(screen, (0,0,0), (j*10, i*10, 10, 10))
                #pygame.draw.rect(screen, (255, 255, 255), (j*10, i*10, 10, 10), 1)
            if map[i][j]== 1:
                pygame.draw.rect(screen, (0,200,200), (j*10, i*10, 10, 10))
    
    pygame.display.flip()

pygame.quit()
