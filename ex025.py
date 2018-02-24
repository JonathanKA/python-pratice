#ex025
#Crie um programa que leia o nome d euma pessoa e diga se ela tem "SILVA no nome.

nome = str(input('Digite o nome completo de uma pessoa: '))
print('Existe o nome silva no caractere {}'.format(nome.find('Silva')))
# checagem = 'Silva' in nome
print('Existe Silva no nome? ', 'Silva' in nome)
