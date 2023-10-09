'''34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a ́ tabela abaixo, quando
o aluno tem mais de 20 faltas ocorre uma redução de conceito. '''

nota = float(input('Insira a Nota: '))
faltas = int(input('Insira a quantidade de faltas: '))

if 9 <= nota <= 10:
    if faltas < 20:
        print('Seu conceito é: A')
    elif faltas > 20:
        print('Seu conceito é: B')

elif 7.5 <= nota <= 8.9:
    if faltas < 20:
        print('Seu conceito é: B')
    elif faltas > 20:
        print('Seu conceito é: C')

elif 5 <= nota <= 7.4:
    if faltas < 20:
        print('Seu conceito é: C')
    elif faltas > 20:
        print('Seu conceito é: D')

elif 4 <= nota <= 4.9:
    if faltas < 20:
        print('Seu conceito é: D')
    elif faltas > 20:
        print('Seu conceito é: E')

elif 0 <= nota <= 3.9:
    if faltas < 20:
        print('Seu conceito é: E')
    elif faltas > 20:
        print('Seu conceito é: E')