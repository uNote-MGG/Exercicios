# Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
media = 0
for numeros in range(5):
    numero = int(input("Insira 5 Numeros: "))
    soma += numero
    media += numero
print(f"Media {media/5}")
print(f"Soma {soma}")