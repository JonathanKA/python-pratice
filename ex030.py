#ex030
#Criei um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR

num = int(input('Digite um numero inteiro: '))
if num % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é impár.'.format(num))
#print('--end if--')