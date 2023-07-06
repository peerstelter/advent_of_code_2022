import os


def priosumme (buchstabe):
    scorelist = ['0' , 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' ,'p','q','r','s','t', 'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    prioSum = 0
    for x in range(len(buchstabe)):
        y = scorelist.index(buchstabe[x])
        prioSum += y
    return prioSum

def readInput():
    contents = []
    while True:
        try:
            line = str(input())
        except EOFError:
            break
        if line:
            contents.append(line)
        else:
            contents.append(0)
    return contents

puzzelInput = readInput()

tempStabe = []
count = 0
while count < len(puzzelInput):

    a =[]
    b=[]
    c=[]
    aS= str(puzzelInput[count])
    if len(aS) >=0:
        for i in range(0, len(aS)):
            a.append(aS[i])
    #print(a)

    bS= str(puzzelInput[count + 1])
    if len(aS) >=0:
        for i in range(0, len(bS)):
            b.append(bS[i])
    #print(b)

    cS= str(puzzelInput[count + 2])
    if len(cS) >=0:
        for i in range(0, len(cS)):
            c.append(cS[i])
    #print(c)

    for i in range(len(a)):
        y = []
        x = []
        s = []
        
        for j in range(len(b)):
            for k in range(len(c)):
                y = a[i]
                x = b[j]
                s = c[k]

                if y == x == s:
                    tempStabe.append(y)
                    break
            if y == x == s:
                break
        if y == x == s:
            break

    count+=3

print("\n\n_____________\n")
    
print(tempStabe)
print(priosumme(tempStabe))
    