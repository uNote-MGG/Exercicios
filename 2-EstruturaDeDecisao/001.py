#Faça um Programa que peça dois números e imprima o maior deles.

while True:

    print("\nSera pedido 2 numeros e será exibido o maior entre eles\n")

    numero_1 = int(input("\nDigite um Numero: \n"))
    numero_2 = int(input("\nDigite o segundo Numero: \n"))

    if numero_1 > numero_2:
        print(f"\nMaior Numero {numero_1}")
    else:
        print(f"\nMaior Numero {numero_2}")
