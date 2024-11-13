# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
while True:
    numero= int(input("Digite um numero menor que 1000 :"))

    if numero < 1000:
        centena = numero // 100
        dezena = numero % 100 // 10
        unidade = dezena % 10
        texto_centena = "Centena" + ("s" if centena > 1 else "")
        texto_dezena = "Dezena" + ("s" if dezena > 1 else "")
        texto_unidade = "Unidade" + ("s" if unidade > 1 else"") 
        if centena > 0:
            print(f"{centena} {texto_centena}", end=",")
        if dezena > 0:
            print(f" {dezena} {texto_dezena}", end=",")
        if unidade > 0:
            print(f" e {unidade} {texto_unidade}")
    else:
        print("Numero Invalido")
