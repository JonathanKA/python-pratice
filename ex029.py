#ex029
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada km acima do limite

speed = float(input('Digite a velocidade do veiculo :'))
multa = (speed - 80)*7
if speed > 80:
    print('Acima do limite de velocidade!\nVocê foi multado em R${:.2f}(Sete reais por cada km acima do limite!)'.format(multa))
else:
    print('Obrigado por seguir as regras de trânsito!')