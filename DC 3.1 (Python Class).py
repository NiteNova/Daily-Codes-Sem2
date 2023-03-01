import random

class chicken:
    def __init__(self, name):
        self.name = name
        self.hunger = 0

    def update(self):
        self.hunger += 5
        if self.hunger < 30:
           i = random.randrange(1, 3)
           if i == 1:
               print("bok BOK!")
               return 1
           else:
               return 0
    def feed(self, guh,):
        self.hunger -= guh
        print("peck peck!")
        print("Chicken:", self.name,"hunger's ", self.hunger)

    def pet(self):
        print("bawk bawk")
       
    def printinfo(self):
        print(self.name)
        print("Chicken:", self.name,"hunger's ", self.hunger)

numEggs = 0

c1 = chicken("Kevin")
c2 = chicken("Alex")
c3 = chicken("Alan")


gameloop = True
while gameloop == True:
    numEggs += c1.update()
    numEggs += c2.update()
    numEggs += c3.update()
    print(numEggs)
    choice = input("What would you like to do with your chicken?: Pet, Feed, Printinfo: ")
    if choice == "Pet" or choice == 'pet':
        c1.pet()
        c2.pet()
        c3.pet()
    elif choice == "Feed":
        c1.feed(5)
        c2.feed(10)
        c3.feed(6)
    elif choice == "Printinfo":
        c1.printinfo()
        c2.printinfo()
        c3.printinfo()
