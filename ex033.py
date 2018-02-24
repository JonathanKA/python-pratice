#ex033
#Faça um programa que leia três números e mostra qual é o maior e qual é o menor

print('Digite 3 números diferentes!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print('O maior número é {} e o menor número é {}'.format(n1, n2))
    else:
        print('O maior número é {} e o menor número é {}'.format(n1, n3))

if n2 > n1 and n2 > n3:
    if n1 > n3:
        print('O maior número é {} e o menor número é {}'.format(n2, n1))
    else:
        print('O maior número é {} e o menor número é {}'.format(n2, n3))

if n3 > n1 and n3 > n2:
    if n1 > n2:
        print('O maior número é {} e o menor número é {}'.format(n3, n1))
    else:
        print('O maior número é {} e o menor número é {}'.format(n3, n2))
print('--END IFs---')
