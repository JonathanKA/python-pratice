v1 = float(input('Digite o valor em Reais para descobrir o mesmo em Dollar:\n'))

dollar = 3.27

total = v1 / dollar

print('Com R${:.2f} reais, você pode comprar ${:.2f} dolares!!'.format(v1, total))