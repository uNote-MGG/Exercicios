# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

while True:

    def media(nota_um,nota_dois):
        media_nota = (nota_um + nota_dois) / 2
        return media_nota
   
    nota_um = int(input("Insira a primeira nota: "))
    nota_dois = int(input("Insira a segunda nota: "))
    media_nota = media(nota_um,nota_dois)

    if media(nota_um,nota_dois) == 10:
        print(f"Aluno APROVADO COM DISTINÇAO!!! com media de {media_nota}")

    elif media(nota_um,nota_dois):
        print(f"Aluno APROVADO!!! com media de {media_nota}")
        
    else:
       print(f"Aluno REPROVADO!!! com media de {media_nota}") 
    

