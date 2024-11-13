# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.


preco_fixo_morango = 2.50
preco_fixo_maca = 1.80
peso_morango = 0
peso_maca = 0

while True:

    peso_morango = float(input("informe a quantidade de morango desejada : "))
    if peso_morango > 0:
        if peso_morango > 5:
            preco_fixo_morango = 2.20
    else:
        print("Quantidade invalida")
        break
    peso_maca = float(input("informe a quantidade de maça desejada : "))
    if peso_maca > 0:
        if peso_maca > 5:
            preco_fixo_maca = 1.50
    else:
        print("Quantidade invalida")
        break
    peso_total = peso_morango + peso_maca

    def preco_total_morango (peso_morango):
        preco_morango = peso_morango * preco_fixo_morango
        return preco_morango

    def preco_total_maca (peso_maca):
        preco_maca = peso_maca * preco_fixo_maca
        return preco_maca

    preco_morango = preco_total_morango (peso_morango)
    preco_maca = preco_total_maca (peso_maca)


    def price_total (preco_morango, preco_maca):
        preco_total = preco_morango + preco_maca
        return preco_total

    price_total(preco_morango, preco_maca)
    preco_total = price_total(preco_morango,preco_maca)

    if peso_total > 8 or preco_total > 25:
        preco_total -= preco_total * (10/100)

    print(f"Voce comprou um total de Kg {peso_morango} de morango e Kg {peso_maca} de maçã Peso total de Kg {peso_total}")
    print(f"O Preço total ficou em R$ {preco_total:.2f}")










