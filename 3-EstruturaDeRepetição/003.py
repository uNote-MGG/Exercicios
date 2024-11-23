# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Insira seu Nome: ").lower()
    caracteres_nome = len(nome)
    nome = nome.capitalize()
    if caracteres_nome < 3:
        print("Nome menos de 3 caracteres")
        continue
    idade = int(input("Insira seu Idade: "))
    if 0 < idade > 150:
        print("Idade Incorreta: ")
        continue

    salario = float(input("Insira seu salario: "))
    if salario <=0 :
        print("Salario Informado Incorreto ")
        continue
    sexo = input("Insira seu sexo: M ou F: ").lower()
    if sexo == 'm':
        sexo = 'Masculino'
    elif sexo == 'f':
        sexo = 'Feminino'
    else:
        print("Sexo Informad Incorreto")
        continue
    estado_civil = input("Insira seu estado civil 's' Solteiro, 'c' Casado, 'v' Viuvo(a), 'd' Divorsiado(a): ").lower()
    if estado_civil == 's':
        estado_civil = 'Solteiro(a)'
    elif estado_civil == 'c':
        estado_civil = 'Casado(a)'
    elif estado_civil == 'v':
        estado_civil = 'Viuvo(a)'
    elif estado_civil == 'd':
        estado_civil = 'Divorciado'
    else:
        print("Estado Civil Incorreto")
        continue
    print(f"Seu Nome é {nome}, sua idade é {idade}, Seu Salario é R$ {salario:.2f}, seu Sexo é {sexo}, Seu Estado Civil {estado_civil}")
    break
