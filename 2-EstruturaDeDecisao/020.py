# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota_um = float(input("Insira a primeira nota parcial: "))
nota_dois = float(input("Insira a segunda nota parcial: "))
nota_tres = float(input("Insira a terceira nota parcial: "))

media = (nota_um + nota_dois + nota_tres) / 3
if media > 10 :
    print("Notas Incorretas")
else:
    if media >= 10: print(f"Aluno com media {media:.2f} Aprovado com Distinção") 
    elif media > 7: print(f"Aluno com media {media:.2f} Aprovado") 
    else: print(f"Aluno com media {media:.2f} Reprovado")