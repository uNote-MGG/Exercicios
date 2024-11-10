#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

while True:

    print("Sera mostrado se o numero e positivo ou negativo \n")
    numero = int(input("Ecolha um numero positivo ou negativo : "))

    if numero < 0 :
        print("O Numero e Negativo\n")
    else:
        print("Numero Positivo\n")