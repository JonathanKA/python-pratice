#ex023

#Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separadaos.
#ex: Digite um numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

numero = input('Digite um numero inteiro de 0 a 9999: ')

print('Milhar: {}'.format(numero[0]))
print('Centena: {}'.format(numero[1]))
print('Dezena: {}'.format(numero[2]))
print('Unidade: {}'.format(numero[3]))