# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Insira um Numero: "))
num2 = int(input("Insira o segundo Numero: "))
soma = 0
for intervalo in range(num1+1,num2,):
    print(intervalo)
    soma += intervalo
print(f"Soma Total entre os valores {soma}")
