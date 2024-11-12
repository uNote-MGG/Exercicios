#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
# mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% 
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
        # Salário Bruto: (5 * 220)        : R$ 1100,00
        # (-) IR (5%)                     : R$   55,00  
        # (-) INSS ( 10%)                 : R$  110,00
        # FGTS (11%)                      : R$  121,00
        # Total de descontos              : R$  165,00
        # Salário Liquido                 : R$  935,00


valor_desconto_ate_1500 = 0.05
valor_desconto_ate_2500 = 0.10
valor_desconto_acima_2500 = 0.20
valor_desconto_sindicato = 0.03
valor_desconto_inss = 0.1
valor_FGTS = 0.11

salario_liquido = 0
imposto_ir = 0
porcentagem_desconto = 0
salario_hora = float(input("Informe o valor da hora : "))
hora_trabalhada = float(input("Informe a quantidade de hora trabalhada: "))

salario_bruto = salario_hora * hora_trabalhada

desconto_sindicato = salario_bruto * valor_desconto_sindicato

desconto_inss = salario_bruto * valor_desconto_inss

fgts_empresa = salario_bruto * valor_FGTS

if salario_bruto > 900 and salario_bruto <= 1500:
    desconto_ir_1500 = salario_bruto * valor_desconto_ate_1500
    imposto_ir = desconto_ir_1500
    porcentagem_desconto = 5

elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_ir_2500 = salario_bruto * valor_desconto_ate_2500
    imposto_ir = desconto_ir_2500
    porcentagem_desconto = 10

elif salario_bruto > 2500:
    desconto_acima_2500 = salario_bruto * valor_desconto_acima_2500
    imposto_ir = desconto_acima_2500
    porcentagem_desconto = 20

else :
    imposto_ir = desconto_ir_1500 = 0

total_descontos = desconto_sindicato + desconto_inss + imposto_ir
salario_liquido = salario_bruto - total_descontos

print(
        f"Salário Bruto: ({salario_hora} * {hora_trabalhada})   : R$ {salario_bruto:.2f}\n"
        f"(-) IR ({porcentagem_desconto}%)                     : R$ {imposto_ir:.2f} \n" 
        f"(-) Sindicato (3%)              : R$ {desconto_sindicato:.2f}\n"
        f"(-) INSS (10%)                  : R$ {desconto_inss:.2f}\n"
        f"FGTS (11%)                      : R$ {fgts_empresa:.2f}\n"
        f"Total de descontos              : R$ {total_descontos:.2f}\n"
        f"Salário Liquido                 : R$ {salario_liquido:.2f}\n "
)
