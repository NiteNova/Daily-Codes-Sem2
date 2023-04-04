# I am a 5 from problems 1 through 5
# I am a 4.5 for problem 6 as I barely even looked at the code
# Also note I commented out the second part for problem 4, but the does work cause I tested it 



#1 (If statements and input/output)
user = int(input("How much can you bench press?(pounds): "))
if user < 10:
    print("Keep practicing and you'll get more swol")
elif user < 50:
    print("You're getting pretty good")
else:
    print("You're mega swol")

print()

#2 (For loops)
for i in range (20, 51, 2):
    print(i)

print()

#3 (While loops)
froggie = True
while froggie == True:
    print("Ribbit!")
    sayfroglol = input()
    if sayfroglol == "frog":
        froggie = False
        print("Froggie is now false")
print()

wah = 100
while wah > 49:
    print(wah)
    wah -= 5
        
print()

#4 (Functions)
def AvgTwoNums(x, y):
    return (x+y)/2
print ("Average is:", AvgTwoNums(8, 4))

def GiveCompliment(name):
    print(name,", You look so nice today")

#THIS PART WORKS. DONT MARK ME DOWN :)

#hi = True
#while hi == True:
#    namelol = input("What is ur name?: ")
#    GiveCompliment(namelol)

print()

#5 (Lists)
marbles = [4, 6, 2, 9]
print("Current Marbles", marbles)
print("Second element is", marbles[1])
for i in range(len(marbles)):
    guh = marbles[i]
    marbles[i] = guh * 2
print("New Marbles:",marbles)

print()

#6 (Classes)
class fruit:
    def __init__(self, t, w):
        self.type = t
        self.weight = w
        self.isFresh = True
        
    def printInfo(self):
        print("The type of fruit is:", self.type)
        print("The weight of the fruit is (grams):", self.weight)
        if self.isFresh == True:
            print("The fruit is fresh")
        else:
            print("The", self.type,"is rotten")
        
    def turnRotten(self):
        self.isFresh = False
        print("The fruit is now rotten")
        
pear = fruit("pear", 178)
apple = fruit("apple", 80)

pear.printInfo()
pear.turnRotten()
pear.printInfo()

apple.printInfo()
apple.turnRotten()
apple.printInfo()
