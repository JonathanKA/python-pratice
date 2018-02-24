#ex034
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

soldo = float(input('Digite o salário do funcionário:\n'))
if soldo <= 1250:
    aumento = (soldo * 1.15) - soldo
    print('O salário antigo era: R${:.2f}\nTeve um aumento de: R${:.2f}\nO novo salário será de: R${:.2f}'.format(soldo, aumento, soldo + aumento))
else:
    aumento = soldo * 0.10
    print('O salário antigo era: R${:.2f}\nTeve um aumento de: R${:.2f}\nO novo salário será de: R${:.2f}'.format(soldo, aumento, soldo + aumento))