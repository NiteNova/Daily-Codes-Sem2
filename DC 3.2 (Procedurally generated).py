import random
mapGrid = [[0 for i in range(10)] for j in range (10)]
xpos = random.randrange(0, 9)
ypos = random.randrange(0, 9)
mapGrid[xpos][ypos] = 1

def direction(x, y):
    dir = random.randrange(0, 4)
    print(dir)
    if dir == 0:
        y += 1
        return x, y
    elif dir == 1:
        y -= 1
        return x, y
    elif dir == 2:
        x += 1
        return x, y
    elif dir == 3:
        x -= 1
        return x, y

ticker = 0
while ticker != 9:
    xpos, ypos = direction(xpos, ypos)
    print(xpos, ypos)
    if mapGrid[xpos][ypos] == 0:
        mapGrid[xpos][ypos] = random.randrange(2, 5)
        ticker +=1

for i in range (10):
    for j in range (10):
        if mapGrid[i][j] == 0:
            print("[ ]", end = "")
        else:
            print("[", end = "")
            print(mapGrid[i][j], end = "")
            print("]", end = "")
    print()

for row in mapGrid:
    print(row)
