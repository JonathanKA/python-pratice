lar = float(input('Digite a largura da parede:\n'))
alt = float(input('Digite a altura da parede\n'))
area = lar * alt

quantreal = area / 2

print('Serao necessarios {:.2f} litros de tinta'.format(quantreal))