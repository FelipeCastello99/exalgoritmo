'''
39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o
salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
• o valor do salário atual do funcionário;
• o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum aumento.
'''

salario_inicial = float(input('Salário atual do funcionário: '))
tempo_de_servico = float(input('Tempo de serviço em anos: '))
reajuste = 1
bonus = 0

if salario_inicial < 500 and tempo_de_servico <1:
    reajuste = 1.25
    bonus = 0

elif (500 < salario_inicial <= 1000) and (1 <= tempo_de_servico <= 3):
    reajuste = 1.20
    bonus = 100

elif (1000 < salario_inicial <= 1500) and (4 <= tempo_de_servico <= 6):
    reajuste = 1.15
    bonus = 200

elif (1500 < salario_inicial <= 2000) and (7<= tempo_de_servico <= 10):
    reajuste = 1.10
    bonus = 300

elif 2000 < salario_inicial and tempo_de_servico > 10:
    reajuste = 1
    bonus = 500

print(f'O salário final é R${salario_inicial*reajuste + bonus :.2f}')
