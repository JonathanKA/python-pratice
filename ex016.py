#import emoji
#import math
##from math import sqrt #importando assim nao precisa utilizar math.
#num = int(input('Digite um numero: '))
#raiz = math.sqrt(num)
#print('A Raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
#print(emoji.emojize("olá, mundo :earth_americas:", use_aliases=True))

from math import trunc
n1 = float(input('Digit um valor com casas decimáis: '))
inteiro = trunc(n1)
print('O valor {} truncado fica {}'.format(n1, inteiro))