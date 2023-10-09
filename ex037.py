'''37. As tarifas de certo parque de estacionamento são as seguintes: ̃
• 1a e 2a hora - R$ 1,00 cada
• 3a e 4a hora - R$ 1,40 cada
• 5a hora e seguintes - R$ 2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar
durante 61 minutos pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos.
Os momentos de chegada ao parque e partida deste são apresentados na forma de pares de inteiros,
representando horas e minutos. Por exemplo, o par 12 50 representara “dez para a uma da tarde”. Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.'''

tempo_horas = 0


hora_entrada = int(input('Insira a Hora de entrada: ')) 
minuto_entrada = int(input('Insira os minutos da entrada: ')) / 60
entrada_total = hora_entrada + minuto_entrada

hora_saida = int(input('Insira a Hora de saída: '))
minuto_saida = int(input('Insira os minutos da saída: ')) / 60
saida_total = hora_saida + minuto_saida

tempo_total = saida_total - entrada_total
tempo_geral = tempo_total


if tempo_total < 0:
    tempo_total = 24 - entrada_total + saida_total 
    tempo_geral = tempo_total

if tempo_total % 1 != 0:
    tempo_total = tempo_total//1 + 1



# calculando o valor da tarifa
if tempo_total <= 2:
    total_a_pagar = tempo_total * 1

elif 2 < tempo_total <= 4:
    total_a_pagar = tempo_total * 1.4

elif 4 < tempo_total:
    total_a_pagar = tempo_total * 2

print(f'O tempo total foi de {tempo_geral//1}horas e {(tempo_geral%1)*60:.0f} minutos e o total a pagar é R${total_a_pagar:.2f}')
