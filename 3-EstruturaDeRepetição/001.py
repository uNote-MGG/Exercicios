# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    nota = float(input("Insira a Nota de 0 a 10: \n"))
    if 0 <= nota <= 10:
        print(f"Nota Valida: {nota}")
        break
    else:
        print(f"Nota Invaldia: {nota}")