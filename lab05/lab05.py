######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Números da Mega-Sena 
# Nome: Bruno Morari    
# RA: 168107    
######################################################################

n1 = int(input())
n2 = 0
n3 = int(input())
n4 = int(input())
n5 = 0
n6 = int(input())

possibleArray1 = []
possibleArray2 = []

if n1 % 2 == 0:

    for i in range(n1, n3):
        if i % 2 != 0:
            possibleArray1.append(i)
        else:
            continue
    
    for n in range(n4, n6):
        if n % 2 == 0:
            possibleArray2.append(n)
        else:
            continue

else:

    for i in range(n1, n3):
        if i % 2 == 0:
            possibleArray1.append(i)
        else:
            continue

    for n in range(n4, n6):
        if n % 2 != 0:
            possibleArray2.append(n)
        else:
            continue

arrayTuples = []

for i in range(len(possibleArray1)):
    for n in range(len(possibleArray2)):
        if (n1 + possibleArray1[i] + n3 + n4 + possibleArray2[n] + n6) % 7 != 0 and (n1 + possibleArray1[i] + n3 + n4 + possibleArray2[n] + n6) % 13 != 0:
            arrayTuples.append((possibleArray1[i], possibleArray2[n]))

print("Primeiro:", "{:02}".format(n1))
print("Terceiro:", "{:02}".format(n3))
print("Quarto:", "{:02}".format(n4))
print("Sexto:", "{:02}".format(n6))
print("Lista de apostas:")

for i in range(len(arrayTuples)):
    print("{:02} - {:02} - {:02} - {:02} - {:02} - {:02}".format(n1, arrayTuples[i][0], n3, n4, arrayTuples[i][1], n6))
