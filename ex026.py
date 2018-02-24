#ex026
#Faca um programa que leia um frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posicao ela aparece a primeira vez.
#Em que posicao ela aparece a ultima vez.

frase = str(input('Digite uma frase qualquer: '))

check1 = frase.count('a')
print('Quantas vezes aparece a letra "a": {}'.format(check1))

check2 = frase.find('a')
print('Ela aparece a primeira vez na casa: {}'.format(check2))

check3 = frase.rfind('a')
print('Ela aparece a ultima vez na casa: {}'.format(check3))
