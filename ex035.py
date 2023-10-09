'''35. Leia uma data e determine se ela e válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe
naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.'''

dia = int(input('Insira o dia: '))
mes = int(input('insira o mês: '))
ano = int(input('insira o ano: '))

if ano <= 2023:

    if mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
        print("A data é válida") 

    elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
        print("A data é válida") 

    # ano bissexto
    elif mes == 2:
        if ano%4 == 0:
            if mes == 2 and 1 <= dia <= 29:
                print("A data é válida") 
        else: 
            if mes == 2 and 1 <= dia <= 28:
                print("A data é válida") 

    
    else:
        print("A data é inválida")


else:
    print("A data é inválida")