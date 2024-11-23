# Faça um programa que leia 5 números e informe o maior número.
numero_maior = 0
for maior in range(5):
    numero = int(input("Escolha um Numero: "))
    if numero > numero_maior:
        numero_maior = numero
print(numero_maior)