'''35. Leia uma data e determine se ela e válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe
naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.'''

data = input('Insira a data no formato dd/mm/aaaa: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if mes == 1 and 1 <= dia <= 31:
    print("A data é válida") 

# ano bissexto
elif mes == 2:
    if ano%4 == 0:
        if mes == 2 and 1 <= dia <= 29:
            print("A data é válida") 
    else: 
        if mes == 2 and 1 <= dia <= 28:
            print("A data é válida") 



elif mes == 3 and 1 <= dia <= 31:
    print("A data é válida") 

elif mes == 4 and 1 <= dia <= 30:
    print("A data é válida") 

elif mes == 5 and 1 <= dia <= 31:
    print("A data é válida") 

elif mes == 6 and 1 <= dia <= 30:
    print("A data é válida") 

elif mes == 7 and 1 <= dia <= 31:
    print("A data é válida") 

elif mes == 8 and 1 <= dia <= 31:
    print("A data é válida") 

elif mes == 9 and 1 <= dia <= 30:
    print("A data é válida") 

elif mes == 10 and 1 <= dia <= 31:
    print("A data é válida") 

elif mes == 11 and 1 <= dia <= 30:
    print("A data é válida") 

elif mes == 12 and 1 <= dia <= 31:
    print("A data é válida") 
else:
    print("A data é inválida")