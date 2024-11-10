#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

while True:

    genero = input("Digite seu Genero F - Feminino ou M - Masculino\n ")
    genero = genero.lower()

    if genero == "m":
        print("M - Masculino")
    elif genero == "f":
        print("F - Feminino")
    else:
        print("Sexo Inválido")