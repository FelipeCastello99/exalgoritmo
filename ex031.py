"""31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e
mostra qual a classificação dessa pessoa."""
peso = float(input('Insira seu peso (kg): '))
altura = float(input('Insira sua altura (m): '))

if altura < 1.20:
    if peso <= 60:
        print("Sua classificação é A")
        
    elif 60 < peso <= 90:
        print("Sua classificação é D") 
    
    else:
        print("Sua classificação é G")


elif 1.20 <= altura <= 1.70:
    if peso <= 60:
        print("Sua classificação é B")
        
    elif 60 < peso <= 90:
        print("Sua classificação é E") 
    
    else:
        print("Sua classificação é H")

else:
    if peso <= 60:
        print("Sua classificação é C")
        
    elif 60 < peso <= 90:
        print("Sua classificação é F") 

    else:
        print("Sua classificação é I")
