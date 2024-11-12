# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.


while True:
    dia_semana = int(input("Escolha um Numero correspondente ao dia da semana: "))
    
    if dia_semana == 1:
        print("1 - DOMINGO")
    elif dia_semana == 2 :
        print("2 - SEGUNDA FEIRA")
    elif dia_semana == 3:
        print("3 - TERÇA FEIRA")
    elif dia_semana == 4:
        print("4 - QUARTA FEIRA")
    elif dia_semana == 5:
        print("5 - QUINTA FEIRA")
    elif dia_semana == 6:
        print("6 - SEXTA FEIRA")
    elif dia_semana == 7:
        print("7 - SABADO")
    else:
        print("Valor Invalido")