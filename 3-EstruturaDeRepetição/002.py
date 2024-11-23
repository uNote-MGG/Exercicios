# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    usuario = input("Digite o nome do usuario: ")
    senha = input("Digite uma senha: ")
    if senha == usuario:
        print("Error senha igual ao usuario tente outra senha!!!")
    else:
        print("Usario logado com sucesso")

usuario = input("Digite o nome de usuario: ")
senha = input("Digite a senha: ")
while usuario == senha:
    print("Nome de usuario nao pode ser igual a senha!")
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")

