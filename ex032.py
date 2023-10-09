"""Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente ser
a calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:"""
preco = 0

cardapio = {'Cachorro Quente': [100, 1.20],
            'Bauru Simples': [101, 1.30],
            'Bauru com Ovo': [102, 1.50],
            'Hamburguer': [103, 1.20],
            'Cheeseburguer': [104, 1.70],
            'Suco': [105, 2.20],
            'Refrigerante': [106, 1.00]}

print(f'N°  -    Prato              -   preço')
for item in cardapio.keys():
    print(f'{cardapio[item][0]} -    {item:<18} -   {cardapio[item][1]:.2f}')

pedido = int(input('Insira o número do seu pedido (0 para fechar pedido): '))
qt = int(input('Insira a quantidade de itens: '))

for item in cardapio.keys():
    if pedido == cardapio[item][0]:
        print(f'O pedido é {item}\n'
              f'a quantidade é {qt}\n'
              f'O preço total foi {qt*cardapio[item][1]:.2f}')


