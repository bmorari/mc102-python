######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Street Fighter
# Nome: Bruno Morari    
# RA: 168107    
######################################################################

hpRyu = int(input())
hpKen = int(input())

try:
    listaGolpes = []
    while True:
        listaGolpes.append(int(input()))
except:
    countRyu = 0
    countKen = 0

    for i in range(len(listaGolpes)):

        # KEN
        if listaGolpes[i] < 0:
            hpRyu += listaGolpes[i]
            countKen += 1
            if hpRyu <= 0:
                hpRyu = 0
            print('KEN APLICOU UM GOLPE:', -listaGolpes[i])
            print('HP RYU =', hpRyu)
            print('HP KEN =', hpKen)

        # RYU
        elif listaGolpes[i] > 0:
            hpKen -= listaGolpes[i]
            countRyu += 1
            if hpKen <= 0:
                hpKen = 0
            print('RYU APLICOU UM GOLPE:', listaGolpes[i])
            print('HP RYU =', hpRyu)
            print('HP KEN =', hpKen)

if hpRyu < hpKen:
    print('LUTADOR VENCEDOR: KEN')
    print('GOLPES RYU =', countRyu)
    print('GOLPES KEN =', countKen)
else:
    print('LUTADOR VENCEDOR: RYU')
    print('GOLPES RYU =', countRyu)
    print('GOLPES KEN =', countKen)