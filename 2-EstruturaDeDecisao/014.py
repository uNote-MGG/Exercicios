# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A A
#   Entre 7.5 e 9.0         B A
#   Entre 6.0 e 7.5         C A
#   Entre 4.0 e 6.0         D R
#   Entre 4.0 e zero        E R
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.


while True:
    nota_um = float(input("Digite a primeira nota: "))
    nota_dois = float(input("Digite a segunda nota: "))
    media_de_aproveitamento = (nota_um + nota_dois) / 2
    aprovacao = ''
    conceito = ''
    aprovacao = "APROVADO !!!" if media_de_aproveitamento > 6 else "REPROVADO !!!"
    
    if media_de_aproveitamento > 10:
        print("Nota Inseria invalida")
        break
    elif media_de_aproveitamento > 9 and media_de_aproveitamento <= 10:
        conceito = 'A'
    elif media_de_aproveitamento >= 7.5 and media_de_aproveitamento < 9:
        conceito = 'B'
    elif media_de_aproveitamento >= 6 and media_de_aproveitamento < 7.5:
        conceito = 'C'
    elif media_de_aproveitamento >= 4 and media_de_aproveitamento < 6:
        conceito = 'D'
    else:
        conceito = 'E'
    

    print(f"Sua primeira nota foi de {nota_um}\n")
    print(f"Sua segunda nota foi de {nota_dois}\n") 
    print(f"Sua media geral foi {media_de_aproveitamento}\n")
    print(f"Seu Conceito foi de {conceito}")
    print(f"Aluno {aprovacao}\n")

    
