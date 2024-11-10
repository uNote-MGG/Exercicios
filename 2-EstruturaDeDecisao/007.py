#Faça um Programa que leia três números e mostre o maior e o menor deles.

while True:
    def maior_numero(num1,num2,num3):
        if num1 > num2 and num1 > num3:
            print(f"Maior numero {num1}")
        elif num2 > num1 and num2 > num3:
            print(f"Maior numero {num2}")
        else:
            print(f"Maior Numero {num3}")

    def menor_numero(num1, num2,num3):
        if num1 < num2 and num1 < num3:
            print(f"Menor numero {num1}")
        elif num2 < num1 and num2 < num3:
            print(f"Menor numero {num2}")
        else:
            print(f"Menor Numero {num3}")

    num1= float(input("Informe um numero: "))
    num2 = float(input("Informe o segundo numero: "))
    num3 = float(input("Informe o terceiro numero: "))
            
    maior_numero(num1,num2,num3)
    menor_numero(num1,num2,num3)