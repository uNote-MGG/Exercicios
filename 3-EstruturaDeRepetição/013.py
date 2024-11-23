# Faça um programa que peça dois números, base e expoente, 
# Calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Insira o numero base: "))
expoente = int(input("Insira o Numero Expoente: "))
resultado = 1

for elevado in range(expoente):
    resultado *= base 
print(f"{base} elevado a {expoente} é {resultado}")