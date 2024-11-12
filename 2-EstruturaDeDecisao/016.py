




# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, 
# informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


# x = (-b ± √(b² - 4ac)) / 2a

while True:
    a = float(input("Digite o valor de a: "))

    if a == 0:
        print("A equação não é do segundo grau.")
        break

    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c


    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui uma raiz real: x =", x)
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("A equação possui duas raízes reais: x1 =", x1, "e x2 =", x2)

    continuar = input("Deseja calcular outra equação? (s/n): ")
    if continuar.lower() != 's':
        break