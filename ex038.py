'''38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mes e Ano.
Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido e um dia válido: dia > 0, dia ≤ 28 para o mês de fevereiro (29 se o ano for bissexto), dia ≤ 30 em abril, junho, setembro e novembro, 6 dia ≤ 31 nos outros meses. Teste a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano ≤ ano atual (use uma constante definida com o valor igual a 2023). Imprimir: “data válida” ou “data inválida” no final da execução do programa.'''

print('Insira sua data de nascimento')
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