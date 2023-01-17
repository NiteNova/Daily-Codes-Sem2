list = [4, 4, 4]
def avg(list):
    g = 0
    for i in range(len(list)):
        g += list[i]
    return g/len(list)

print(avg(list)) 
