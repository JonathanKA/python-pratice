preco = float(input('Digite o preco do produto:\n'))
desconto = preco - (preco * 0.05) # ou desconto = preco -( preco * 5 /100)
print('O preço com 5% de desconto é R${:.2f}'.format(desconto))