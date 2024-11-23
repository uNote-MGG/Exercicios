# Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro

contador = 0
contador2 = 0
while contador < 20:
    contador += 1
    print(contador)

while contador2 < 20:
    contador2 += 1
    print(contador2,end=", ")

print("Git")

for i in range(1, 21):
    print(i)

numeros = ""
for i in range(1, 20):
    numeros += f"{i}, "
numeros += "20"

print(numeros)