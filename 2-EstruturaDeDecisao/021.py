# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
while True:
    sacar= int(input("\nDigite um valor para sacar :"))

    def nota_cem (sacar):
        nota_de_cem = sacar // 100
        return nota_de_cem
    
    def nota_cinquenta (sacar):
        nota_de_cinquenta = (sacar % 100) // 50
        return nota_de_cinquenta

    def nota_dez (sacar):   
        nota_de_dez = sacar % 100 // 10
        if nota_de_dez > 5:
            nota_de_dez = nota_de_dez - 5

        return nota_de_dez
    
    def nota_cinco (sacar):
        nota_de_cinco = sacar % 100 % 10 % 10 // 5
        return nota_de_cinco
    
    def nota_um (sacar):
        nota_de_um = sacar % 100  % 10 % 10 % 5
        if nota_de_um >= 5:
            nota_de_um = nota_de_um - 5

        return nota_de_um

    nota_de_cem = nota_cem(sacar)
    nota_de_cinquenta = nota_cinquenta(sacar)
    nota_de_dez = nota_dez(sacar)
    nota_de_cinco = nota_cinco(sacar)
    nota_de_um = nota_um(sacar)
    
    if sacar >= 10 :
        if sacar <= 600:

            texto_nota_cem = "nota" + ("s" if nota_de_cem > 1 else "")
            texto_nota_de_cinquenta = "nota" + ("s" if nota_de_cinquenta > 1 else"")
            texto_nota_de_dez = "nota" + ("s" if nota_de_dez > 1 else "")
            texto_nota_de_cinco = "nota" + ("s" if nota_de_cinco > 1 else "")
            texto_nota_de_um = "nota" + ("s" if nota_de_um > 1 else"") 
            texto_virgula = "," + ("" if nota_de_cem > 1 or nota_de_cinquenta > 1 or nota_de_dez > 1 or nota_de_cinco > 1 or nota_de_um else ",")
            if nota_de_cem > 0:
                print(f"{nota_de_cem} {texto_nota_cem} de cem", end=",")
            if nota_de_cinquenta >0:
                print(f" {nota_de_cinquenta} {texto_nota_de_cinquenta} de cinquenta", end=",")
            if nota_de_dez > 0:
                print(f" {nota_de_dez} {texto_nota_de_dez} de dez", end=",")
            if nota_de_cinco >0:
                print(f" {nota_de_cinco} {texto_nota_de_cinco} de cinco", end=",")
            if nota_de_um > 0:
                print(f" e {nota_de_um} {texto_nota_de_um} de um\n")
        else:
            print("Limite max de R$ 600.00")
    else:
        print("Limite minimo para saque e de R$ 10.00")

# Resolução por IA

# def sacar_dinheiro(valor):
#     """Simula um saque em um caixa eletrônico.

#     Args:
#         valor (int): Valor a ser sacado.

#     Returns:
#         None
#     """

#     notas = [100, 50, 20, 10, 5, 1]
    
#     if valor < 10 or valor > 600:
#         print("Valor inválido. Saque entre R$10 e R$600.")
#         return

#     print("Saque de R$", valor)
    
#     for nota in notas:
#         quantidade_notas = valor // nota
#         valor %= nota
#         if quantidade_notas > 0:
#             print(f"{quantidade_notas} nota(s) de R${nota}")

# # Solicita o valor do saque ao usuário
# valor_saque = int(input("Digite o valor que deseja sacar: "))

# # Chama a função para realizar o saque
# sacar_dinheiro(valor_saque)
            