# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
num1 = int(input("Insira um Numero: "))
num2 = int(input("Insira o segundo Numero: "))

for intervalo in range(num1+1,num2,):
    print(intervalo)