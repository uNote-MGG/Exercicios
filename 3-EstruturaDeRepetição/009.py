# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
numero = 0
for inpar in range(50):
    numero += 1
    if numero %2:
        print(numero)

for inpar in range(1,50,2):
    print(inpar)