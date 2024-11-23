# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse 
# ou iguale a população do país B, mantidas as taxas de crescimento.

pais_a = 80000
pais_b = 200000
taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015
anos = 0

while True:

    resultado_por_ano = pais_a * taxa_crescimento_a
    pais_a += resultado_por_ano
    print(f"População Pais A {int(pais_a)}")

    resultado_por_ano_b = pais_b * taxa_crescimento_b
    pais_b += resultado_por_ano_b
    print(f"População Pais B {int(pais_b)}")


    anos += 1
    if pais_a >= pais_b:
        print(f"Sera Nescessario {anos} Anos para o pais A alcançar a população do pais B")
        break
    