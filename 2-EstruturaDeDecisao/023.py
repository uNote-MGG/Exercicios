# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

import math

while True:
   
    numero = float(input("Insira um numero para se o número é inteiro ou decimal: "))
    arrendodado = round(numero)

    if arrendodado == numero:
        print("Numero Inteiro")
    else:
        print("Numero Decimal")