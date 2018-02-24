#ex031
#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Cacule o proço da passagem, cobrando R$0.50 por Km para viagens de até 200 km e R$0.45 para viagens mais longas.
dist = int(input('Digite a distância da viagem: '))
if dist <= 200:
    preco = dist * 0.50
    print('O valor de sua viagem de {}Km é R${:.2f}'.format(dist ,preco))
else:
    preco = dist * 0.45
    print('O valor de sua viagem de {}Km é R${:.2f}'.format(dist, preco))
print('--END IF--')
