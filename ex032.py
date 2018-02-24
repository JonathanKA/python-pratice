#ex032
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input('Digite um ano qualquer:\n'))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é Bissexto!')
else:
    print('Esse ano não é Bissexto!')