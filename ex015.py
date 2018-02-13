n1 = float(input('Quantos km foram percorridos:\n'))
n2 = float(input('Digite a quantidade de dias que o carro ficou alugado:\n'))
#sabendo que o carro custa R$60 por dia e R$0.15 por km rodado

pagar = (0.15*n1) + (60*n2)

print('A tarifa custa R$60 por dia e R$0.15 por km rodado.\nVoce utilizou o veiculo por {} dias e andou por {}Km.\nO Valor total a pagar é R${:.2f}'.format(n2, n1, pagar))