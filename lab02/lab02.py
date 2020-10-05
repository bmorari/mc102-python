######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Chegada na Estação
# Nome: Bruno Morari    
# RA: 168107    
######################################################################

x = int(input())
t = int(input())
v_1 = float(input())
v_2 = float(input())

t1 = x / v_1
t2 = x / v_2 + t / 60

if t1 > t2 :
  print(False)
else :
  print(True)