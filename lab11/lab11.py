###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Tetris 2020
# Nome: Bruno Morari
# RA: 168107
###################################################

def verifica_jogo(lista_ref, tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca):
  for i in range(altura_tabuleiro):
    for j in range(largura_tabuleiro):

      if(tabuleiro[i][j]== "."):
        
        for n in range(len(lista_ref)):
          if(0 > i+lista_ref[n][0] or i+lista_ref[n][0] >= altura_tabuleiro or 0 > j+lista_ref[n][1] or j+lista_ref[n][1] >= largura_tabuleiro or tabuleiro[i+lista_ref[n][0]][j+lista_ref[n][1]] != "."):
            break

          if(n == len(lista_ref) -1):

            for v in range(len(lista_ref)):
              tabuleiro[i+lista_ref[v][0]][j+lista_ref[v][1]] = "#"
            status_do_jogo = "O jogo deve continuar"
            return tabuleiro, status_do_jogo

  status_do_jogo = "Fim de jogo"

  return tabuleiro, status_do_jogo

def maior(velha, ponto):
  if(velha > ponto):
    return False
  else:
    return True
	

# Leitura do tabuleiro

altura_tabuleiro, largura_tabuleiro = [int(x) for x in input().split()]
cont_ponto = 0
tabuleiro = []
for i in range(altura_tabuleiro):
  linha = input()
  for j in range(len(linha)):
    if(linha[j]=="."):
      cont_ponto += 1
  tabuleiro.append(list(linha))
                         
# Leitura da peça

altura_peca, largura_peca = [int(x) for x in input().split()]

peca = []
lista_ref = []
ini_l = 0
ini_c = 0
primeiro = 0
cont_velha = 0
for i in range(altura_peca):
  linhaPeca = input()
  peca.append(list(linhaPeca))
  for j in range(len(list(linhaPeca))):
    if(linhaPeca[j] == "#"):
      cont_velha += 1
      if(primeiro == 0):
          primeiro = 1
          ini_l = i
          ini_c = j
      lista_ref.append((i-ini_l, j-ini_c))

# Impressão da configuração atualizada do tabuleiro

if(maior(cont_velha, cont_ponto)): #significa que tem a possibilidade de dar bom
  tabuleiro, status_do_jogo = verifica_jogo(lista_ref, tabuleiro, altura_tabuleiro, largura_tabuleiro, peca, altura_peca, largura_peca)
else:
  status_do_jogo = "Fim de jogo"


for linha in tabuleiro:
  print("".join(linha))

# Impressão do status do jogo
print(status_do_jogo)