# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto

while True:
    ano = int(input("Digite um ano para descobrir se ele e bissexto: "))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
        print(f"O Ano {ano} é Bissexto")
    else:
        print(f"O ano {ano} não é bissexto, Tente outro ano")

