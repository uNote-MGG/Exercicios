# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
import math
while True:
    menu = '''
    Escolha uma Opção do menu 
    para descobrir se seus numeros é

    [1] Par ou Ímpar
    [2] Positivo ou Negativo
    [3] Inteiro ou Decimal
    [4] Parar


    '''


    def par_ou_impar (numero_um, numero_dois):
        numero_par_ou_impar_um = numero_um % 2
        
        if numero_par_ou_impar_um ==0:
            print("Primeiro numero par")
        else:
            print("Primeiro numero impar")
        numero_par_ou_impar_dois = numero_dois % 2
        if numero_par_ou_impar_dois ==0:
            print("Segundo numero par")
        else:
            print("Segundo numero impar")

    def positivo_negativo (numero_um, numero_dois):

        if numero_um > 0:
            print("Primeiro numero positivo")
        else:
            print("Primeiro numero negativo")
        if numero_dois > 0:
            print("Segundo numero positivo")
        else:
            print("Segundo numero negativo")

    def inteiro_descimal (numero_um, numero_dois):
        arrendondamento_um = round(numero_um)
        arrendondamento_dois = round(numero_dois)

        if arrendondamento_um == numero_um:
            print("Primeiro numero inteiro")
        else:
            print("Primeiro numero decimal")
        
        if arrendondamento_dois == numero_dois:
            print("Segundo numero inteiro")
        else:
            print("Segundo numero decimal")

    print(menu)
    opcao_menu = int(input("Informe a opção: "))
    if opcao_menu == 4:
        break
    numero_um = float(input("Informe um numero: "))
    numero_dois = float(input("Informe o segundo numero: "))
    if opcao_menu == 1 :
        par_ou_impar(numero_um,numero_dois)
    elif opcao_menu == 2 :
        positivo_negativo(numero_um,numero_dois)
    elif opcao_menu == 3 :
        inteiro_descimal(numero_um,numero_dois)
    else:
        print("Opção Invalida")



