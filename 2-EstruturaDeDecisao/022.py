# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
while True:
    numero = int(input("Insira um numero para descobrir se e para ou impar: "))
    par = numero % 2

    if par == 0:
        print("Numero par")
    else:
        print("Numero impar")