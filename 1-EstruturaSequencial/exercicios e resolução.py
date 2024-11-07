import math 
   # Faça um Programa que mostre a mensagem "Alo mundo" na tela.
# print("Alou Mundo")

    # # Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
# numero = input("Digite um Numero: ")
# print(f"Numero escolhido foi {numero}")

     # Faça um Programa que peça dois números e imprima a soma.4
# num1 = input("Digite o Primeiro Numero: ")
# num2 = input("Digite o Segundo Numero: ")
# soma = int(num1) + int(num2)
# print(soma)

    # Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# bi1 = input("Digite a Nota do 1 Bimestre: ")
# bi2 = input("Digite a Nota do 2 Bimestre: ")
# bi3 = input("Digite a Nota do 3 Bimestre: ")
# bi4 = input("Digite a Nota do 4 Bimestre: ")
# notatotal = int(bi1) + int(bi2) + int(bi3) + int(bi4)
# media = notatotal / 4
# print(f"Nota da Soma dos 4 Bimetres: {notatotal}")
# print(f"A Media da nota é : {media}")

    # Faça um Programa que converta metros para centímetros.
# metros = input("Digite a quantidade de metros para converter em centímetros: ")
# centrimetros = float(metros) * 100
# print(f"Numero {metros} Metros Corresponde a  : {float(centrimetros)} Centimetros")

    # Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# raio = input ("Informe o Raio desejado: ")
# raio2 = float(raio) ** 2
# a = math.pi * raio2

# print(f"A area do raio {raio} é {a}")


    # Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# q = input("Informe um Lado do quadrado: ")
# a2 = int(q) ** 2
# q2 = a2 * 2
# print(q2)
    # Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
# shora = input("Qual o Valor da Sua Hora Trabalhada: ")
# htrabalhada = input("Quantas Horas trabalhor: ")
# salario_mes = float(shora) * float(htrabalhada)
# print(f"Seu salario esse mes sera de R${float(salario_mes):,.2f}")
    # Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    # C = 5 * ((F-32) / 9).
# tf = input("Qual a temperatura Fahrenheit em : ")
# tc = (float(tf) - 32) / 1.8
# print(f"A Temperatura Referente Fº {tf} é Cº {float(tc)}")

    
    # Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# tc = input("Qual a temperatura Celsius em : ")
# tf = (float(tc) * 1.8) + 32
# print(f"A Temperatura Em Celsius Cº {tc} é Fº {float(tf)}")
    
    # Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.
# num1 = int(input("Insira o Primeiro Numero: "))
# num2 = int(input("Insira o Segundo Numero: "))
# num3 = float(input("Insira um Numero Real: "))
# resul1 = (2 * num1) + (2 / num2)
# resul2 = (3 * num1) + num2
# resul3 = num3 ** 3
# print(f"O produto do dobro do primeiro com metade do segundo é:{resul1}\nA soma do triplo do primeiro com o terceiro é: {resul2} \nO terceiro elevado ao cubo é: {resul3}")


    # Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
# h = float(input("Digite a Sua Altura: "))
# pi = (72.7*h) - 58
# print (f"Seu peso ideal é: {pi:.2f} ")
    # Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7
# h = float(input("Digite a Sua Altura: "))
# pih = (72.7*h) - 58
# pim = (62.1*h) - 44.7
# print (f"Seu peso ideal para a altura de um homem é : {pih:.2f} \nSeu peso ideal para a altura para uma mulher é :{pim:.2f}")
    
    # João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
         #que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça 
         # um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa 
         # o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# pregula = 50
# pfish = float(input("Insira a quantidade de Kg de peixe pescado: "))
# if pfish > pregula:
#     excesso = pfish - pregula
#     multa = excesso * 4
#     print(f"Sera Nescessario pagar R${multa:,.2f} de multa")
# else:
#     print("Limite de peso dentro do regulamento! ")
 
    # Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
    # sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    # salário bruto.
    # quanto pagou ao INSS.
    # quanto pagou ao sindicato.
    # o salário líquido.
    # calcule os descontos e o salário líquido, conforme a tabela abaixo:
    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$
    # Obs.: Salário Bruto - Descontos = Salário Líquido.
# shora = float(input("Qual o Valor da Sua Hora Trabalhada: "))
# htrabalhada = float(input("Quantas Horas trabalhor: "))
# salario_bruto = shora * htrabalhada
# ir = 0.11
# inss = 0.08
# sind = 0.05
# pir = salario_bruto * ir
# pinss = salario_bruto * inss
# psind = salario_bruto * sind
# salario_liquido = salario_bruto - pir - pinss - psind
# print(f"Seu salario Bruto desse mes foi de R${salario_bruto:,.2f}\nFoi descontado o valor de R${pinss:,.2f} para o Inss\nFoi descontado o valor de R${psind:,.2f} para o Sindicato\nFoi descontado o valor de R${pir:,.2f} Imposto de Renda\nSeu salario Liquido esse mes foi de R${salario_liquido:,.2f}")

    # Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
    # de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta 
    # a serem compradas e o preço total.
# litros18 = 18
# preco_lata_18 = float(80)
# metros = float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))
# cobertura_por_lata = litros18 * 3
# total_de_latas = metros / cobertura_por_lata
# arredondado = math.ceil(total_de_latas)
# preco_total = preco_lata_18 * arredondado
# print(f"A quantiade de latas sera de {arredondado} Latas de 18 Litros\nTotal a pagar R${preco_total:,.2f}")

# def calc_tinta(area):
#     cober_litro = 3
#     tamanho_lata = 18
#     preco_lata = 80
#     litros_nescessario =  area / cober_litro
#     latas_nescessaria = math.ceil(litros_nescessario / tamanho_lata)
#     preco_total = latas_nescessaria * preco_lata
#     return latas_nescessaria, preco_total
# area = float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))
# latas, preco = calc_tinta(area)
# print(f"Você precisará de {latas} latas de tinta.")
# print(f"O preço total será de R$ {preco:.2f}.")

    # Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é 
    # de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    # Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    # comprar apenas latas de 18 litros;
    # comprar apenas galões de 3,6 litros;
    # misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# cobertura_por_litro = 6
# preco_lata36 = 25
# preco_lata18 = 80
# tamanho_lata36 = 3.6
# tamanho_lata18 = 18

# def calcular_tinta18 (area) :
#     litros_nescessario =  area / cobertura_por_litro
#     latas_nescessaria = math.ceil(litros_nescessario / tamanho_lata18)
#     preco_total = latas_nescessaria * preco_lata18
#     return latas_nescessaria, preco_total

# def calcular_tinta36 (area) :
#     litros_nescessario =  area / cobertura_por_litro
#     latas_nescessaria = math.ceil(litros_nescessario / tamanho_lata36)
#     preco_total = latas_nescessaria * preco_lata36
#     return latas_nescessaria, preco_total

# def calcular_menos_disperdicio (area):
#     litros_nescessario = area / cobertura_por_litro
#     litros_nescessario = litros_nescessario * 1.10
#     latas_18 = litros_nescessario // 18
#     restante = litros_nescessario % 18 
#     lata_36 = restante // 3.6
#     preco_total = (latas_18 * preco_lata18) + (lata_36 * preco_lata18)
#     latas_nescessaria18 = int(latas_18)
#     latas_nescessaria36 = int(lata_36)
#     return latas_nescessaria18,latas_nescessaria36, preco_total
    

# area = float(input("Insira o tamanho em metros quadrados da área a ser pintada: "))
# latas18, preco18 = calcular_tinta18(area)
# latas36, preco36 = calcular_tinta36(area)
# latas_nescessaria18,latas_nescessaria36, preco_total = calcular_menos_disperdicio(area)

# apenas_lata = float(input("Digite 1 se voce gostaria de comprar apenas lata de 18 litros \nDigite 2 se voce gostaria de comprar apenas lata de 3.6 litros\nDigite 3 se voce gostaria de de ter o menor disperdicio  "))

# if apenas_lata == 1 :
#     print(f"Você precisará de {latas18} latas de tinta de 18 litros.")
#     print(f"O preço total será de R$ {preco18:.2f}.")
# elif apenas_lata == 2:
#     print(f"Você precisará de {latas36} latas de tinta de 3.6 Litros.")
#     print(f"O preço total será de R$ {preco36:.2f}.")
# elif apenas_lata == 3:
#     print(f"Você precisará de {latas_nescessaria18} latas de tinta de 18 Litros.\nVocê precisará de {latas_nescessaria36} latas de tinta de 3.6 Litros.")
#     print(f"O preço total será de R$ {preco_total:.2f}.")


    
    # Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
    # aproximado de download do arquivo usando este link (em minutos).


def conversao_velocidade_internet (velocidade_internet_mbps):
    conversao_velocidade = velocidade_internet_mbps / 8
    return conversao_velocidade


def tempo_downalod_arquivo (tamanho_arquivo,conversao_velocidade):
    tempo_aproximado = tamanho_arquivo / conversao_velocidade
    return tempo_aproximado


tamanho_arquivo = int(input("Insira o tamanho o tamanho do aqruivo em MB: "))
velocidade_internet_mbps = int(input("Insira a velocidade do link de internet em Mbps: "))

conversao_velocidade = conversao_velocidade_internet(velocidade_internet_mbps)
tempo_aproximado = tempo_downalod_arquivo (tamanho_arquivo,conversao_velocidade)

if tempo_aproximado > 60:
    tempo_em_minutos = tempo_aproximado // 60
    tempo_sobra_minutos = tempo_aproximado % 60
    if tempo_em_minutos > 1 :
        print(f"O tempo Aproximado sera de {int(tempo_em_minutos)} Minutos e {int(tempo_sobra_minutos)} Segundos")
    else:
        print(f"O tempo Aproximado sera de {int(tempo_em_minutos)} Minuto e {int(tempo_sobra_minutos)} Segundos")
else:
    tempo_em_segundos = tempo_aproximado
    print(f"O tempo Aproximado sera de {int(tempo_em_segundos)} segundos")

