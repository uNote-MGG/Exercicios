# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente 
# receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne 
# comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar.

preco_total = 0
menu = '''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira
Cada cliente poderá levar apenas um dos tipos de carne da promoção
Se compra for feita no cartão Tabajara o cliente 
receberá ainda um desconto de 5% sobre o total da compra

                       Até 5 Kg             Acima de 5 Kg
[1]File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
[2]Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
[3]Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
[4]Sair

'''
menu2 = '''
Forma de pagamento 
[1]Cartão Tabajara o cliente desconto de 5%
[2]Cartao outros

'''
file_duplo = 4.90
alcatra = 5.90
picanha = 6.90

while True:

    print(menu)

    opcao = int(input("Escolha uma opção : "))

    if opcao == 1:
        pedido = float(input("Insira a quantiade desejada: "))
        if pedido > 5 :
            preco_total = pedido * 5.80
        else:
            preco_total = pedido * file_duplo
            breakpoint
        
    elif opcao == 2:
        pedido = float(input("Insira a quantiade desejada: "))
        if pedido > 5 :
            preco_total = pedido * 6.80
        else:
            preco_total = pedido * alcatra
    elif opcao == 3:
        pedido = float(input("Insira a quantiade desejada: "))
        if pedido > 5 :
            preco_total = pedido * 7.80
        else:
            preco_total = pedido * picanha
    elif opcao == 4 :
        break
    else:
        print("Opção invalida")
    
    print(menu2)
    opcao2 = int(input("Escolha uma opção : "))
    if opcao2 == 1 :
        preco_total -= preco_total * (5/100)
        print(f"Preço total a pagar R$ {preco_total:.2f}")
    elif opcao2 == 2 :
        print(f"Preço total a pagar R$ {preco_total:.2f}")
    else:
        print("Opção invalida")
    



