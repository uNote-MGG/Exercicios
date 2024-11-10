#Faça um Programa que leia três números e mostre-os em ordem decrescente.

numeros = []

numero_um = float(input("Escolha um numero \n"))
numeros.append(numero_um)
numero_dois = float(input("Escolha o segundo numero \n"))
numeros.append(numero_dois)
numero_tres = float(input("Escolha uo terceiro numero \n"))
numeros.append(numero_tres)

numeros.sort()
numeros.reverse()
print (numeros)


numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))
numero3 = float(input("Digite mais um numero: "))
if numero1 > numero2 > numero3:
    print(numero1, numero2, numero3)
elif numero1 > numero3 > numero2:
    print(numero1, numero3, numero2)
elif numero2 > numero1 > numero3:
    print(numero2, numero1, numero3)
elif numero2 > numero3 > numero1:
    print(numero2, numero3, numero1)
elif numero3 > numero1 > numero2:
    print(numero3, numero1, numero2)
else:
    print(numero3, numero2, numero1)