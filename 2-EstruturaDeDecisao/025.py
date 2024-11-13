# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
possivel_crime = 0
respostas_validas = {'sim', 'nao', 's', 'n', 'y', 'n'}

while True:
    print ("Responda as 5 perguntas somente com Sim ou Nao ")

    questao_um = input("Telefonou para a vítima? : ").lower()
    if questao_um not in respostas_validas:
        print("Resposta um invalida")
        break 
    else:
        possivel_crime += 1

    questao_dois = input("Esteve no local do crime ? :").lower()
    if questao_dois not in respostas_validas:
        print("Resposta dois invalida")
        break 
    else:
        possivel_crime += 1

    questao_tres = input("Mora perto da vítima? : " ).lower()
    if questao_tres not in respostas_validas:
        print("Resposta tres invalida")
        break 
    else:
        possivel_crime += 1

    questao_quatro = input("Devia para a vítima? : ").lower()
    if questao_quatro not in respostas_validas:
        print("Resposta quatro invalida")
        break 
    else:
        possivel_crime += 1

    questao_cinco = input("Já trabalhou com a vítima? : ").lower()
    if questao_cinco not in respostas_validas:
        print("Resposta cinco invalida")
        break 
    else:
        possivel_crime += 1

    if possivel_crime == 0:
        criminalidade = 'Inocente'
    elif possivel_crime == 2:
        criminalidade = 'Suspeitp(a)'
    elif possivel_crime == 5:
        criminalidade = 'Assassino(a)'
    else:
        criminalidade = 'Cúmplice'

    print(f"Voce Foi Considerado {criminalidade}")

