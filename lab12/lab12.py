###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Filtros de Imagens
# Nome: Bruno Morari
# RA: 168107
###################################################


'''
Função que recebe uma imagem e imprime essa imagem no formato PGM
'''
def imprime_imagem(imagem):
    print("P2")
    print(len(imagem[0]), len(imagem))
    print("255")
    for i in range(len(imagem)):
        print(" ".join(str(x) for x in imagem[i]))

'''
Função que retorna a mediana de uma lista. Se o tamanho da lista
for par, a função retorna a parte inteira da média entre os elementos
centrais
'''
def mediana(lista):
    lista_ordenada = sorted(lista)
    elemento_central = len(lista_ordenada) // 2
    if len(lista) % 2 == 1:
        return lista_ordenada[elemento_central]
    else:
        #retorna a parte inteira da média entre os elementos centrais
        return (lista_ordenada[elemento_central-1] + lista_ordenada[elemento_central]) // 2

''' 
Função que recebe a matriz que representa a imagem original e
retorna a imagem resultante da aplicação do filtro negativo 
'''
def filtro_negativo(imagem):
    for i in range(len(imagem)):
        for j in range(len(imagem[i])):
            imagem[i][j] = 255 - imagem[i][j]
    return imagem

'''
Função que recebe a matriz que representa a imagem original e 
retorna a imagem resultante da aplicação do filtro da mediana
'''


def filtro_mediana(imagem):
    count = 0
    imagem2 = []
    aux = 0
    for i in range(len(imagem)):
        for j in range(len(imagem[i])):

            if i == 0 and j == 0:
                aux = mediana([ imagem[i][j], imagem[i][j+1], imagem[i+1][j], imagem[i+1][j+1] ])
                imagem2.append(aux)

            elif i == 0 and j == (m-1):
                aux = mediana([ imagem[i][j], imagem[i][j-1], imagem[i+1][j], imagem[i+1][j-1] ])
                imagem2.append(aux)

            elif i == (n-1) and j == 0:
                aux = mediana([ imagem[i][j], imagem[i][j+1], imagem[i-1][j], imagem[i-1][j+1] ])
                imagem2.append(aux)

            elif i == (n-1) and j == (m-1):
                aux = mediana([ imagem[i][j], imagem[i][j-1], imagem[i-1][j], imagem[i-1][j-1] ])
                imagem2.append(aux)

            elif i == 0:
                aux = mediana([ imagem[i][j], imagem[i][j-1], imagem[i][j+1], imagem[i+1][j], imagem[i+1][j-1], imagem[i+1][j+1] ])
                imagem2.append(aux)

            elif i == (n-1):
                aux = mediana([ imagem[i][j], imagem[i][j-1], imagem[i][j+1], imagem[i-1][j], imagem[i-1][j-1], imagem[i-1][j+1] ])
                imagem2.append(aux)

            elif j == 0:
                aux = mediana([ imagem[i][j], imagem[i][j+1], imagem[i-1][j], imagem[i-1][j+1], imagem[i+1][j], imagem[i+1][j+1] ])
                imagem2.append(aux)

            elif j == (m-1):
                aux = mediana([ imagem[i][j], imagem[i][j-1], imagem[i-1][j], imagem[i-1][j-1], imagem[i+1][j], imagem[i+1][j-1] ])
                imagem2.append(aux)

            else:
                aux = mediana([ imagem[i-1][j-1], imagem[i-1][j], imagem[i-1][j+1], imagem[i][j-1], imagem[i][j], imagem[i][j+1], imagem[i+1][j-1], imagem[i+1][j], imagem[i+1][j+1] ])
                imagem2.append(aux)

    for k in range(len(imagem)):
        for g in range(len(imagem[k])):
            imagem[k][g] = imagem2[count]
            count += 1

    return imagem

'''
Função que recebe três parâmetros: 

imagem: matriz que representa a imagem original
M: matriz núcleo
D: divisor

Essa função retorna a imagem resultante da aplicação de um filtro 
que usa convolução
'''
def convolucao(imagem, lista, div):

    imagem2 = []
    count = 0
    l1 = 0
    l2 = 0
    l3 = 0
    aux = 0
    result = 0

    for i in range(len(imagem)):
        for j in range(len(imagem[i])):

            if i == 0:
              continue
            elif i == (n-1):
              continue
            elif j == 0:
              continue
            elif j == (m-1):
              continue
            else:
                l1 = int(lista[0][0]*imagem[i-1][j-1] + lista[0][1]*imagem[i-1][j] + lista[0][2]*imagem[i-1][j+1])
                l2 = int(lista[1][0]*imagem[i][j-1] + lista[1][1]*imagem[i][j] + lista[1][2]*imagem[i][j+1])
                l3 = int(lista[2][0]*imagem[i+1][j-1] + lista[2][1]*imagem[i+1][j] + lista[2][2]*imagem[i+1][j+1])
                result = (l1 + l2 + l3) / div

                if result < 0:
                    aux = 0
                    imagem2.append(aux)

                elif result > 255:
                    aux = 255
                    imagem2.append(aux)

                else:
                    imagem2.append(int(result))

    del imagem[0]
    del imagem[-1]

    for k in range(len(imagem)):
        del imagem[k][0]
        del imagem[k][-1]

    for x in range(len(imagem)):
        for y in range(len(imagem[x])):
            imagem[x][y] = imagem2[count]
            count += 1

    return imagem

# Leitura da entrada

filtro = input()
_ = input() # P2 (linha a ser ignorada)

m, n = [int(x) for x in input().split()]

_ = input() # 255 - linha a ser ignorada

imagem = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    imagem.append(linha)

# Aplica o filtro

if filtro == "negativo":
    filtro_negativo(imagem)
elif filtro == "mediana":
    filtro_mediana(imagem)
elif filtro == "edge-detect":
    lista = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    div = 1
    convolucao(imagem, lista, div)
elif filtro == "blur":
    lista = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    div = 9
    convolucao(imagem, lista, div)
elif filtro == "sharpen":
    lista = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    div = 1
    convolucao(imagem, lista, div)

# Imprime a imagem gerada
imprime_imagem(imagem)