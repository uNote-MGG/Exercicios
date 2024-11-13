# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
# pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

PRECO_GASOLINA = 2.50
PRECO_ALCOOL = 1.90
nome_posto = 'Chel'
menu = f'''

Bem Vindo ao Posto {nome_posto}
[L] Quantros Litros deseja abastecer
[S] Sair

'''

menu2 = f'''
Bem Vindo ao Posto {nome_posto}
[A] Álcool valor R$ 1.90 Litro
[G] Gasolina valor R$ 2.50 Litro
 
'''

def desconto_alcool (litros):
    if litros <= 20:
        total_a_pagar = litros * (PRECO_ALCOOL - (PRECO_ALCOOL * (3/100)))
    else:
        total_a_pagar = litros * (PRECO_ALCOOL -(PRECO_ALCOOL * (5/100)))
    return total_a_pagar

def desconto_gasolina(litros):
    if litros <= 20:
        total_a_pagar = litros * (PRECO_GASOLINA - (PRECO_GASOLINA * (4/100)))
    else:
        total_a_pagar = litros * (PRECO_GASOLINA -(PRECO_GASOLINA * (6/100)))
    return total_a_pagar


while True:

    print(menu)
    opcao2 = input("informe uma opção: \n").lower()

    if opcao2 == 'l':
        litros = float(input("Infome os Litros: \n"))
        if litros <= 0:
            print("Litros Invalido")
        else:
            print(menu2)
        opcao = input("informe uma opção: \n").lower()
        if opcao == 'a':
            desconto_alcool(litros)
            total_a_pagar = desconto_alcool(litros)
            print(f"Total a Pagar R$ {total_a_pagar:.2f}")
        
        elif opcao =='g':
            desconto_gasolina(litros)
            total_a_pagar = desconto_gasolina(litros)
            print(f"\nTotal a Pagar R$ {total_a_pagar:.2f}")
        else:
            print("\nOpção Invalida!!!")
        
    elif opcao2 == 's':
        break   
    else:
        print("\nOpção Invalida!!!")