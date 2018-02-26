#ex033
#Faça um programa que leia três números e mostra qual é o maior e qual é o menor

print('Digite 3 números diferentes!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
#verificando o menor
menor = n1
if n2 < n1 and n3 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))

#Solution 2
print(min(n1, n2, n3))
print(max(n1, n2, n3))

#Solution 3
print('Digite 3 números diferentes!')

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))

list1 = [n1,n2,n3]

list1.sort(reverse=True)
print('o menor é:',min(list1),'o maior é:', max(list1))