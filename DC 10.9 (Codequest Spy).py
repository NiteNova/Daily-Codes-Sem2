cases = int(input(""))

for i in range (cases):
    line = (input("").lower())
    sep = []
    sep = line.split("|")

    g = sep[0]
    k = list(g)

    p = sep[1]
    n = list(p)

    duplicat_exist = True

    for n in range(len(p)):
        if p[n].isalpha():
            for _ in range(len(g)):
                if p[n] == g[_]:
                    break
            else:
                duplicat_exist = False
    if duplicat_exist == True:
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")
