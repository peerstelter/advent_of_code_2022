# A = Rock
# B = Paper
# C = Sissor

# X = Rock      = 1 point
# Y = Paper     = 2 Points
# Z = Sissor    = 3 points

# Loose  = 0 points
# Draw  = 3 points
# Win   = 6 points

# A X || BY || CZ = Draw
# A Z || BX || CY = Loose
# A Y || BZ || CX = Win
import os
score = 0
contents = []

while True:
    try:
        line = input()
    except EOFError:
        break
    if line:
        contents.append(line)
    else:
        contents.append(0)
print("\n ___________________\n")

for x in contents:
    
    if x == "A X":
        score += 4
    elif x == "B Y":
        score += 5
    elif x == "C Z":
        score += 6

    elif x == "A Z":
        score += 3
    elif x == "B X":
        score += 1
    elif x == "C Y":
        score += 2

    elif x == "A Y":
        score += 8
    elif x == "B Z":
        score += 9
    elif x == "C X":
        score += 7

print("\nTotal Score part One: ")
print(score)
print("\n")



# X = Lose
# Y = Draw
# Z = Win
# 
# # A = Rock
# B = Paper
# C = Sissor

# X = Rock      = 1 point
# Y = Paper     = 2 Points
# Z = Sissor    = 3 points

# Loose  = 0 points
# Draw  = 3 points
# Win   = 6 points
# 
# 
# 
scoreTwo = 0

for x in contents:
    
    if x == "A X":
        scoreTwo += 3
    elif x == "A Y":
        scoreTwo += 4
    elif x == "A Z":
        scoreTwo += 8

    elif x == "B X":
        scoreTwo += 1
    elif x == "B Y":
        scoreTwo += 5
    elif x == "B Z":
        scoreTwo += 9

    elif x == "C X":
        scoreTwo += 2
    elif x == "C Y":
        scoreTwo += 6
    elif x == "C Z":
        scoreTwo += 7


print("\nTotal Score part One: ")
print(scoreTwo)
print("\n")