"""41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a 
tabela abaixo:

IMC             Classificação
< 18,5          Abaixo do Peso
18,6 - 24,9     Saudável
25,0 - 29,9     Peso em excesso
30,0 - 34,9     Obesidade Grau I
35,0 - 39,9     Obesidade Grau II (severa)
≥ 40,0          Obesidade Grau III (mórbida)"""

peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))
imc = peso/(altura)**2

if imc < 18.5:
    print('Abaixo do peso')

elif 18.5 <= imc < 25:
    print('Saudável')

elif 25 <= imc < 30:
    print('Peso em excesso')

elif 30 <= imc < 35:
    print('Obesidade Grau I')

elif 35 <= imc < 40:
    print('Obesidade Grau II (severa)')

elif imc >= 40:
    print('Obesidade grau III (mórbida)')