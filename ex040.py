"""
40. O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
"""

'''CUSTO DE FÁBRICA                % DO DISTRIBUIDOR       % DOS IMPOSTOS
até R$12.000,00                         5                   isento
entre R$12.000,00 e 25.000,00           10                    15
acima de R$25.000,00                    15                    20'''

custo_de_fabrica = float(input('Insira o custo da fábrica: '))
porcentagem_distribuidor = 0
porcentagem_imposto = 0

if custo_de_fabrica <= 12000:
    porcentagem_distribuidor = 0.05*custo_de_fabrica
    porcentagem_imposto = 0*custo_de_fabrica

elif 1200 < custo_de_fabrica <= 25000:
    porcentagem_distribuidor = 0.10*custo_de_fabrica
    porcentagem_imposto = 0.15*custo_de_fabrica

elif 2500 < custo_de_fabrica:
    porcentagem_distribuidor = 0.15*custo_de_fabrica
    porcentagem_imposto = 0.20*custo_de_fabrica

print(f"O valor final será R${custo_de_fabrica + porcentagem_distribuidor + porcentagem_imposto:.2f}")


