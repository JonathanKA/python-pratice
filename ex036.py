#ex036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Digite o valor do patrimonio: "))
soldo = float(input("Digite o valor so seu sálario: "))
anos_pagar = float(input("Em quantos ano você vai pagar: "))

mensal = casa / (anos_pagar * 12)
trinta_porcento = (0.30 * soldo)

if mensal > trinta_porcento:
    print("Emprestimo negado! A sua prestacao {:.2f} é maior que 30% ({:.2f}) do seu salário de {:.2f}".format(mensal, trinta_porcento, soldo))
else:

    print("Parabéns pela compra, você vai pagar em {} anos, 12 parcelas/ano de {:.2f}".format(anos_pagar, mensal))