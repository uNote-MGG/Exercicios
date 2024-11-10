#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

while True:

    
    letras = input("Infome uma letra \n")
    letras.lower()
    vogais = "aeiou"

    if letras in vogais:
        print("A letra", letras, "é uma vogal.")
    else:
        print("A letra", letras, "é uma consoante.")