salario = float(input('Digite o seu salario:\n'))

aumento = salario * 1.15 # ou aumento = salario + ( salario * 15 / 100 )

print('Seu salario com um aumento de 15% é R${:.2f}'.format(aumento))