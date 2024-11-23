# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

menu = '''
[1] Fazer Calculo
[2] Sair
'''
while True:
    print(menu)
    opcao = int(input("Escolha uma Opção: "))
    if opcao == 1:
        anos = 0
        pais_a = int(input("Digite a População Do Pais A: "))
        if pais_a <= 0:
            print("População Informada incorreta")
        else:
            pais_b = int(input("Digite a População Do Pais B: "))
        if pais_b <= 0:
            print("População Informada incorreta")
        else:
            taxa_crescimento_a = float(input("Digite a taxa de crescimento do Pais A: "))
            taxa_crescimento_a = taxa_crescimento_a / 100
            taxa_crescimento_b = float(input("Digite a taxa de crescimento do Pais B: "))
            taxa_crescimento_b = taxa_crescimento_b / 100
            while True:   
                resultado_por_ano = pais_a * taxa_crescimento_a
                pais_a += resultado_por_ano
                print(f"População Pais A {int(pais_a)}")

                resultado_por_ano_b = pais_b * taxa_crescimento_b
                pais_b += resultado_por_ano_b
                print(f"População Pais B {int(pais_b)}")
                anos += 1
                if pais_a >= pais_b:
                    print(f"Sera Nescessario {anos} Anos para o pais A alcançar a população do pais B")
                    break

    elif opcao == 2:
        print("Obrigado Por utilizar o Programa")
        break
    else:
        print("Opcao Incorreta")
    