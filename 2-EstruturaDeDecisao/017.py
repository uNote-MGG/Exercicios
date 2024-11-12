# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

while True:
    ano = int(input("Digite um ano para descobrir se ele e bissexto: "))
    anobissexto = ano % 4 
    anobissexto2 = ano % 400
    
    if anobissexto2 == 0 or anobissexto == 0:
        print(f"Ano {ano} digitado e Bissexto")
    else:
        print("Tente outro ano")
