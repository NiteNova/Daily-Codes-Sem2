import random

#1 Mild (Smallest and biggest elements of a list)
guh = []
for i in range(11):
    guh.append(random.randrange(1, 101))
print("Mild list:", guh)


#Smallest element
smol = guh[0]
for j in range(len(guh)):
    if guh[j] < smol:
        smol = guh[j]
print(smol)

#Biggest Element
biggie = guh[0]
for g in range(len(guh)):
    if guh[g] > biggie:
        biggie = guh[g]
print(biggie)

print()

#2 Medium (Buuble Sort)
wah = []
for p in range(11):
    wah.append(random.randrange(1, 101))
print("Medium List:", wah)

print()
for j in range(len(wah)):
    swapped = False
    for i in range(len(wah)-1):
        if wah[i] > wah[i+1]:
            wah[i], wah[i+1] = wah[i+1], wah[i]
            swapped = True
            
    if swapped == False:
        break

print("New Medium List:", wah)


        
        
print(wah)
