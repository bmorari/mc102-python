###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Tabela de Vendas
# Nome: Bruno Morari
# RA: 168107
###################################################

# Leitura de dados

nLinhas = int(input())
padrao = input().split(",")
dados = []
for i in range(nLinhas):
    linha = input().split(",")
    dados.append(linha)
prioridades = input().split(" ")
prioridades.reverse()

# Ordenação dos dados

for k in prioridades:

  if k == "Produto":
    for i in range(len(dados) - 1, 0, -1):
      for j in range(i):
        if dados[j][0] > dados[j + 1][0]:
          dados[j][3], dados[j + 1][3] = dados[j + 1][3], dados[j][3]
          dados[j][2], dados[j + 1][2] = dados[j + 1][2], dados[j][2]
          dados[j][0], dados[j + 1][0] = dados[j + 1][0], dados[j][0]
          dados[j][1], dados[j + 1][1] = dados[j + 1][1], dados[j][1]

  elif k == "Setembro":
    for i in range(len(dados) - 1, 0, -1):
      for j in range(i):
        if int(dados[j][1]) > int(dados[j + 1][1]):
          dados[j][3], dados[j + 1][3] = dados[j + 1][3], dados[j][3]
          dados[j][2], dados[j + 1][2] = dados[j + 1][2], dados[j][2]
          dados[j][0], dados[j + 1][0] = dados[j + 1][0], dados[j][0]
          dados[j][1], dados[j + 1][1] = dados[j + 1][1], dados[j][1]

  elif k == "Outubro":
    for i in range(len(dados) - 1, 0, -1):
      for j in range(i):
        if int(dados[j][2]) > int(dados[j + 1][2]):
          dados[j][3], dados[j + 1][3] = dados[j + 1][3], dados[j][3]
          dados[j][2], dados[j + 1][2] = dados[j + 1][2], dados[j][2]
          dados[j][0], dados[j + 1][0] = dados[j + 1][0], dados[j][0]
          dados[j][1], dados[j + 1][1] = dados[j + 1][1], dados[j][1]

  elif k == "Novembro":
    for i in range(len(dados) - 1, 0, -1):
      for j in range(i):
        if int(dados[j][3]) > int(dados[j + 1][3]):
          dados[j][3], dados[j + 1][3] = dados[j + 1][3], dados[j][3]
          dados[j][2], dados[j + 1][2] = dados[j + 1][2], dados[j][2]
          dados[j][0], dados[j + 1][0] = dados[j + 1][0], dados[j][0]
          dados[j][1], dados[j + 1][1] = dados[j + 1][1], dados[j][1]

print("Produto           Setembro   Outubro  Novembro")
for linha in dados:
        print('{:15s}'.format(linha[0]), ''.join('{:>10}'.format(item) for item in linha[1:]))