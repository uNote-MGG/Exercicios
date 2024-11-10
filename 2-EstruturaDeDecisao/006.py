# Faça um Programa que leia três números e mostre o maior deles.

while True:
    def maior_numero ():
        numero_um = float(input("Informe um numero: "))
        numero_dois = float(input("Informe o segundo numero: "))
        numero_tres = float(input("Informe o terceiro numero: "))
        if numero_um > numero_dois and numero_um > numero_tres:
            print(f"Maior Numero Digitado foi o 1 {numero_um}")
        elif numero_dois > numero_um and numero_dois > numero_tres:
            print(f"Maior Numero Digitado foi o 2 {numero_dois}")
        else:
            print(f"Maior Numero Digitado foi o 3 {numero_tres}")

    maior_numero()