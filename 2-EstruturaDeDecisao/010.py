# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
menu = """
Escolha o Turno que voce estuda\n\n
======MENU======
= M-Matutino   =
= V-Vespertino =
= N- Noturno   =

"""
while True:

    print(menu)
    opcao = input("Digite a opção: ")
    if opcao.lower() == 'm':
        limpar_tela()
        print ("Bom Dia! \n")
    elif opcao.lower() == 'v':
        limpar_tela()
        print("Boa Tarde! \n")
    elif opcao.lower() == 'n':
        limpar_tela()
        print("Boa Noite! \n")
        
    else:
        limpar_tela()
        print("Valor Inválido!!!\n")
    
    