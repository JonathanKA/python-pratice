#ex023

#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separadaos.
#ex: Digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

#Resolucao usando matematica
num = int(input('Digite um numero inteiro de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))

#Resolucao com string
valor = str(num).zfill(4)
print('O numero inteiro é: ',valor)
print('Milhar: {}'.format(valor[0]))
print('Centena: {}'.format(valor[1]))
print('Dezena: {}'.format(valor[2]))
print('Unidade: {}'.format(valor[3]))
