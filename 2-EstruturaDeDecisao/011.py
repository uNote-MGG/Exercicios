# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

while True:

    def reajuste_280(salario):
        reajuste_20 = salario * 1.20
        aumento_salario = reajuste_20 - salario
        print(f"o salário antes do reajuste era de R${salario:.2f} \nPercentual de aumento aplicado foi de 20% \no valor do aumento foi de R$ {aumento_salario:.2f}\no novo salário, após o aumento R$ {reajuste_20:.2f}  ")

    def reajuste_700(salario):
        reajuste_15 = salario * 1.15
        aumento_salario = reajuste_15 - salario
        print(f"o salário antes do reajuste era de R${salario:.2f} \nPercentual de aumento aplicado foi de 15% \no valor do aumento foi de R$ {aumento_salario:.2f}\no novo salário, após o aumento R$ {reajuste_15:.2f}  ")

    def reajuste_1500(salario):
        reajuste_10 = salario * 1.10
        aumento_salario = reajuste_10 - salario
        print(f"o salário antes do reajuste era de R${salario:.2f} \nPercentual de aumento aplicado foi de 10% \no valor do aumento foi de R$ {aumento_salario:.2f}\no novo salário, após o aumento R$ {reajuste_10:.2f}  ")

    def reajuste_maior_1500(salario):
        reajuste_05 = salario * 1.05
        aumento_salario = reajuste_05 - salario
        print(f"o salário antes do reajuste era de R${salario:.2f} \nPercentual de aumento aplicado foi de 5% \no valor do aumento foi de R$ {aumento_salario:.2f}\no novo salário, após o aumento R$ {reajuste_05:.2f}  ")

    # colaborador = input("Insira o Nome do Funcionario")
    salario = float(input("Insira o valor do salario: "))
    if salario <= 280:
        reajuste_280(salario)

    elif salario > 280 and salario <= 700:
        reajuste_700(salario)

    elif salario > 700 and salario <= 1500:
        reajuste_1500(salario)
    else:
        reajuste_maior_1500(salario)








        