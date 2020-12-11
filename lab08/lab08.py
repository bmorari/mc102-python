######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Ocorrência de Palavras 
# Nome: Bruno Morari    
# RA: 168107    
######################################################################

wordSimilar = 0
occurence = 0
arrayOfCaracteres = [".", ",", ":", ";", "!", "?"]
helpArray = []

# LEITURA DOS DADOS

numberLines = int(input())

arrayOfLines = []
for i in range(numberLines):
    arrayOfLines.append(str(input()))

numberWords = int(input())

arrayOfWords = []
for i in range(numberWords):
    arrayOfWords.append(str(input()))

# TRANSFORMAR TODAS AS LINHAS PARA MINÚSCULO

for i in range(len(arrayOfLines)):
    arrayOfLines[i] = arrayOfLines[i].lower()

# REMOVER OS CARACTERES ESPECIAIS

for i in range(len(arrayOfCaracteres)):
    for n in range(len(arrayOfLines)):
        arrayOfLines[n] = arrayOfLines[n].replace(arrayOfCaracteres[i], "")

# CONTAGEM E IMPRESSÃO DA OCORRÊNCIA DE PALAVRAS

for i in range(len(arrayOfWords)):

    for m in range(len(arrayOfLines)):
        helpArray = arrayOfLines[m].split(" ")
        occurence += helpArray.count(arrayOfWords[i].lower())

    for n in range(len(arrayOfLines)):
        wordSimilar = wordSimilar + arrayOfLines[n].count(arrayOfWords[i].lower())

    print("Palavra buscada:", arrayOfWords[i])
    print("Ocorrencia:", occurence)
    print("Palavras similares:", wordSimilar - occurence)
    wordSimilar = 0
    occurence = 0
    