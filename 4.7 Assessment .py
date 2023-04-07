print("This is problem 1")
#Problem 1
for i in range(-20, 41, 5):
  print(i)

print()
print("This is problem 2")
#Problem 2
for i in range(5):
  for j in range(1):
    print("*", end = "")
  print("*")

print()
######## LOOK HERE #########
print("I don't know if you wanted it to be 5 len and 2 width or other way around")

for l in range(2):
  for p in range (5):
    print("*", end = "")
  print("*")
######## LOOK HERE #########


print()
print("This is problem 3")

#Problem 3
guh = 50
while guh >= 0:
  print(guh)
  guh -= 10

print()
print("This is problem 4")

#Problem 4
wah = True

while wah == True:
  print("Here is a cookie!")
  user = input("Do you want another one?\n")
  if user == "yes" or user == "Yes":
    print("COOKIE!")
  else:
    wah = False
  
  
