#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

data = input("Infome uma data para verificar se ela e valida utilizando como exemplo dd/mm/aaaa: ")

data = data.split('/')
dia = data[0]
mes = data[1]
ano = data[2]
dia = int(dia)
mes = int(mes)
ano = int(ano)

if  mes < 0 and mes > 12 or ano < 0:
    print("Data Invalida !!!")

elif mes == 2 and dia <= 29:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
        if dia > 0 and dia <= 29 and ano > 0:
            print("Data Valida e o Ano é Bissexto")
    else:
        if dia > 0 and dia <= 28 and ano > 0:
            print("Data Valida")
        else:
            print("Data Invalida !!!")


elif mes in [1,3,5,7,8,10,12]:
    if dia > 0 and dia <= 31 and ano > 0:
        print("Data Valida")
    else:
        print("Data Invalida !!!")

elif mes in [4,6,9,11]:
    if dia > 0 and dia <= 30 and ano > 0:
        print("Data Valida")
    else:
        print("Data Invalida !!!")

else:
    print("Data Invalida !!!")