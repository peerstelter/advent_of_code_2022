import os
prioSum = 0
contents = []

def priosumme (buchstabe):
    scorelist = ['0' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,'p','q','r','s','t', 'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    prioSum = 0
    for x in range(len(buchstabe)):
        y = scorelist.index(buchstabe[x])
        prioSum += y
        #print("\n*** " + str(y) + " ***")
    return prioSum

while True:
    try:
        line = str(input())
    except EOFError:
        break
    if line:
        contents.append(line)
    else:
        contents.append(0)
print("\n ___________________\n")

buchStabe = []
for x in contents:
    value = str(x)
    a = []
    b = []
    if len(value) >= 0:
        for i in range(0,len(value)):
            if i <= len(value)//2-1:
                a.append(value[i])
            else:
                b.append(value[i])
            
        for i in range(len(a)):
            y = []
            z = []
            for j in range(len(b)):
                y = a[i]
                z = b[j]
                if y == z:
                    buchStabe.append(a[i])
                    break
            if y == z:
                break

print("\n\n" + "-------" + "\n")

print(priosumme(buchStabe))

