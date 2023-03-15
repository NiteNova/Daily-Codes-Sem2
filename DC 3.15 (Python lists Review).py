import random

#mild python list
#1
colors = ['blue', 'purple', 'green', 'red', 'yellow']
print(colors[0])
print(colors[2])
print(colors[4])
colors.append('pink')
print(colors)
#2
paychecks = [10, 20, 90, 30]
sum = 0
for i in range (len(paychecks)):
    sum += paychecks[i]
print(sum) 
#3
foods = []
num = int(input("How much types of food do you want to pack?: "))
for j in range (num):
    user = input("Enter food: ")
    foods.append(user)
print(foods)

#Medium python list
guh = []
for i in range(0, 12):
    guh.append(random.randrange(1, 11))
print(guh)

#1
biggest = guh[0]
for i in range (len(guh)):
    if guh[i] > biggest:
        biggest = guh[i]
print(biggest)        

smallest = guh[0]
for j in range (len(guh)):
    if guh[j] < smallest:
        smallest = guh[j]
print(smallest)

#2
guh.sort()
for i in range (10):
    if guh[i]+1 == guh[i+1]:
        if guh[i]+2 == guh[i+2]:
            print("The list contains", guh[i], guh[i+1], guh[i+2])
#3
guh2 = []
for i in range(12):
    guh2.append(guh[11-i])
print("Original list: ", guh)
print("Reversed list: ", guh2)
