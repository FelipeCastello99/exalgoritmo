'''33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço
novo, e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).'''
preco_novo = None
preco_antigo = float(input('Insira o preço antigo: '))

if preco_antigo <= 50:
    preco_novo = preco_antigo * 1.05

elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.1

elif 100 < preco_antigo:
    preco_novo = preco_antigo * 1.15

if preco_novo <= 80:
    print('Barato')

elif 80 < preco_novo <= 120:
    print('Normal')

elif 120 < preco_novo <= 200:
    print('Caro')

else:
    print('Muito caro')