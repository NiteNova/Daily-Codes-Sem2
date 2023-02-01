#Problem 1 --------------------------#Modulo Recursion
def add(n): #function definition
    if n/10 < 1: #base code
        return n
    else:
        return n%10+add(int(n/10)) #call itself

print(add(351)) 

#Problem 2 --------------------------#Adding Recursion

def sum(n): #function definition
    if n<=1: #base code
        return 1
    else:
        return n+sum(n-1) #call itself
    
print(sum(5)) 
#Problem 3 --------------------------#Power Recursion
def power(b, e): #function definition
    if e<=1: #base code
        return b
    else:
        return b*power(b, e-1) #call itself

print(power(2, 3))
