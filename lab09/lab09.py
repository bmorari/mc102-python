#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Copa do Mundo de Futebol
# Nome: Bruno Morari
# RA: 168107
#####################################################

# Leitura da lista de seleções

selecoes = []
resultados = []
dic = {}
for i in range(16):
    selecao = input()
    selecoes.append(selecao)
    dic[selecao] = {"partidas": 0,
                    "vitorias": 0,
                    "derrotas": 0,
                    "penaltis": 0,
                    "normal": 0,
                    "marcados": 0,
                    "sofridos": 0}

for i in range(16):
    resultado = input()
    resultados.append(resultado)

for i in range(len(resultados)):
    for n in range(len(selecoes)):
      dic[selecoes[n]]["partidas"] += resultados[i].count(selecoes[n])

helpArray = []
helpArray2 = []
campeao = []

for i in range(len(resultados)):
    helpArray = resultados[i].replace("(", "").replace(")", "")
    helpArray = helpArray.split()

    for n in range(len(helpArray)):
        if helpArray[n] == '1' or helpArray[n] == '2' or helpArray[n] == '3' or helpArray[n] == '4' or helpArray[n] == '5' or helpArray[n] == '6' or helpArray[n] == '7' or helpArray[n] == '8' or helpArray[n] == '9' or helpArray[n] == '0':
            helpArray2.append(int(helpArray[n]))

    if len(helpArray2) == 2:
        dic[helpArray[0]]["normal"] += 1
        dic[helpArray[4]]["normal"] += 1

        dic[helpArray[0]]["marcados"] += helpArray2[0]
        dic[helpArray[0]]["sofridos"] += helpArray2[1]

        dic[helpArray[4]]["marcados"] += helpArray2[1]
        dic[helpArray[4]]["sofridos"] += helpArray2[0]

        if helpArray2[0] > helpArray2[1]:
            dic[helpArray[0]]["vitorias"] += 1
            dic[helpArray[4]]["derrotas"] += 1
        else:
            dic[helpArray[0]]["derrotas"] += 1
            dic[helpArray[4]]["vitorias"] += 1

    else:
        dic[helpArray[0]]["penaltis"] += 1
        dic[helpArray[7]]["penaltis"] += 1

        dic[helpArray[0]]["marcados"] += helpArray2[0]
        dic[helpArray[0]]["sofridos"] += helpArray2[1]

        dic[helpArray[7]]["marcados"] += helpArray2[1]
        dic[helpArray[7]]["sofridos"] += helpArray2[0]

        if helpArray2[2] > helpArray2[3]:
            dic[helpArray[0]]["vitorias"] += 1
            dic[helpArray[7]]["derrotas"] += 1
        else:
            dic[helpArray[0]]["derrotas"] += 1
            dic[helpArray[7]]["vitorias"] += 1

    helpArray2 = []

verificarCampeao = []

for selecao in selecoes:
    print("-" * 50)
    print("Pais:", selecao)
    print("Partidas:", dic[selecao]["partidas"])
    print("Partidas decididas em tempo normal de jogo:", dic[selecao]["normal"])
    print("Partidas decicidas nos penaltis:", dic[selecao]["penaltis"])
    print("Vitorias:", dic[selecao]["vitorias"])
    print("Derrotas:", dic[selecao]["derrotas"])
    print("Gols marcados:", dic[selecao]["marcados"])
    print("Gols sofridos:", dic[selecao]["sofridos"])

    verificarCampeao.append([dic[selecao]["vitorias"], selecao])
    verificarCampeao.sort()

print("-" * 50)
print("Pais campeao:", verificarCampeao[-1][1])
print("-" * 50)