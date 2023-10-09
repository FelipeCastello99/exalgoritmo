"""30. Faça um programa que receba três números e mostre-os em ordem crescente."""
lista = []
for c in range(3):
    valor = int(input('Insira um numero: '))
    lista.append(valor)

print(f"Em ordem crescente fica: {sorted(lista)}")