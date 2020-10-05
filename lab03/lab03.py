######################################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Bruto x Liquido
# Nome: Bruno Morari    
# RA: 168107    
######################################################################

salarioBruto = float(input())
salarioDesc = 0

if salarioBruto <= 1045.00 :
  inss = salarioBruto * 0.075
  salarioDesc = salarioBruto - inss

elif salarioBruto <= 2089.60 :
  inss = salarioBruto * 0.09
  salarioDesc = salarioBruto - inss

elif salarioBruto <= 3134.00 :
  inss = salarioBruto * 0.12
  salarioDesc = salarioBruto - inss

elif salarioBruto <= 6101.06 :
  inss = salarioBruto * 0.14
  salarioDesc = salarioBruto - inss

else :
  inss = 6101.06 * 0.14
  salarioDesc = salarioBruto - inss

impostoRenda = 0
salarioLiq = 0

if salarioDesc <= 1903.98 :
  salarioLiq = salarioDesc - impostoRenda

elif salarioDesc <= 2826.65 :
  impostoRenda = salarioDesc * 0.075 - 142.80
  salarioLiq = salarioDesc - impostoRenda

elif salarioDesc <= 3751.05 :
  impostoRenda = salarioDesc * 0.15 - 354.80
  salarioLiq = salarioDesc - impostoRenda

elif salarioDesc <= 4664.68 :
  impostoRenda = salarioDesc * 0.225 - 636.13
  salarioLiq = salarioDesc - impostoRenda

else :
  impostoRenda = salarioDesc * 0.275 - 869.36
  salarioLiq = salarioDesc - impostoRenda

print("Bruto: R$", format(salarioBruto, ".2f").replace(".",","))
print("INSS: R$", format(inss, ".2f").replace(".",","))
print("IR: R$", format(impostoRenda, ".2f").replace(".",","))
print("Liquido: R$", format(salarioLiq, ".2f").replace(".",","))