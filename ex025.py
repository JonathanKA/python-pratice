#ex025
#Crie um programa que leia o nome d euma pessoa e diga se ela tem "SILVA no nome.

nome = str(input('Digite o nome completo de uma pessoa: '))

#Esse nao trata se existe diferenca de upper ou lowercase
print('Existe o nome silva no caractere {}'.format(nome.find('Silva')))
# checagem = 'Silva' in nome
print('Existe Silva no nome? ', 'SILVA' in nome.upper())
