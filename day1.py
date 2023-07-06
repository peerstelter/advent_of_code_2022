import os


meistenCalorien = 0
aktuelleCalorien = 0

welcherElfMax = 0
AktuellerElf = 1

elvescal = []

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if line:
        contents.append(int(line))
    else:
        contents.append(0)
print("\n ___________________\n")
print(contents)


for x in contents:
    a = x
    #print(a)
    if a == 0:
        if aktuelleCalorien > meistenCalorien:
            meistenCalorien = aktuelleCalorien
            welcherElfMax = AktuellerElf
        AktuellerElf += 1
        elvescal.append(aktuelleCalorien)
        aktuelleCalorien = 0
        #print("new elf\n")
    else:
        #print("add to elf\n")
       
        aktuelleCalorien += a
        print("\nend of file!\n")

    
print("Welcher Elf Max: " + str(welcherElfMax) + "\n" + "meisten Calorien: " + str(meistenCalorien))
elvescal.sort()
elvescal.reverse()

print("\n")
print(elvescal[0])
print("\n")
print(elvescal[1])
print("\n")
print(elvescal[2])
print("\n")

totalmaxofthree = elvescal[0] + elvescal[1] + elvescal[2]
print("\nTotal max of the max Three Elves: " + str(totalmaxofthree) + "\n")