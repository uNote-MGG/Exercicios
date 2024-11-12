# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
while True:
    
    triangulo_lado_um = int(input("Insira o primeiro lado do triangulo: \n"))
    triangulo_lado_dois = int(input("Insira o segundo lado do triangulo: \n"))
    triangulo_lado_tres = int(input("Insira o terceiro lado do triangulo: \n"))

    if triangulo_lado_um == 0 or triangulo_lado_dois == 0 or triangulo_lado_tres == 0:
        print("Tamanho de Triangulo Invalido !!!\n")
        break

    if triangulo_lado_um == triangulo_lado_dois and triangulo_lado_um == triangulo_lado_tres:
            print("Triângulo Equilátero: três lados iguais\n")

    elif triangulo_lado_um != triangulo_lado_dois and triangulo_lado_um != triangulo_lado_tres and triangulo_lado_dois != triangulo_lado_tres:
            print("Triângulo Escaleno: três lados diferentes\n")

    else:
            print("Triângulo Isósceles: quaisquer dois lados iguais\n")

    
