'''36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:'''

comissao = None
venda = float(input('Insira o valor da venda: '))



if venda < 20000:
    comissao = 400 + 0.14 * venda

elif 20000 <= venda < 40000:
    comissao = 500 + 0.14 * venda

elif 40000 <= venda < 60000:
    comissao = 550 + 0.14 * venda

elif 60000 <= venda < 80000:
    comissao = 600 + 0.14 * venda

elif 80000 <= venda < 100000:
    comissao = 650 + 0.14 * venda

elif venda >= 100000:
    comissao = 700 + 0.16 * venda

print(f"A comissão será R${comissao:.2f}".replace('.', ','))