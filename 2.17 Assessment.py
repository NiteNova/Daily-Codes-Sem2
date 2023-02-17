#medium check for understanding

input = int(input("Enter your level: "))

def targetScore(lol):
    if lol == 1:
        return 50
    elif lol == 2:
        return 40
    elif lol == 3:
        return 30
    elif lol == 4:
        return 20
    elif lol == 5:
        return 10
    
    
print("Your score is",(targetScore(input)))

