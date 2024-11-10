# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

while True:
    
    produtos= ['Laranja','Pera','Uva']

    def mais_barato(preco_um,preco_dois,preco_tres):
        if preco_um < preco_dois and preco_um < preco_tres:
            print(f"A fruta {produtos[0]} é a mais barata custando R$ {preco_um:.2f} ")
        elif preco_dois < preco_um and preco_dois < preco_tres:
            print(f"A fruta {produtos[1]} é a mais barata custando R$ {preco_dois:.2f} ")
        else:
            print(f"A fruta {produtos[2]} é a mais barata custando R$ {preco_tres:.2f} ")


    preco_um = float(input(f"Informe o Preço da {produtos[0]}\n"))
    preco_dois = float(input(f"Informe o Preço da {produtos[1]}\n"))
    preco_tres = float(input(f"Informe o Preço da {produtos[2]}\n"))

    mais_barato(preco_um,preco_dois,preco_tres)