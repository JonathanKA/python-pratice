#ex033
#Faça um programa que leia três números e mostra qual é o maior e qual é o menor

print('Digite 3 números diferentes!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#Verificando o menor
a = n1
b = n2
c = n3
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('===' * 10)
print('maior é ', maior)
print('menor é ', menor)
