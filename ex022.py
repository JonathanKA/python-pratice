#ex022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as Letras maiusculas
#-O nome com todas as minusculas
#-Quantas letras ao todo(sem considerar espacos)
#-Quantas letras tem o primeiro nome

name = str(input('Digite um nome completo: ')).strip()

print('Analisando o eu nome...')
print('O seu nome em maiusculas e {}'.format(name.upper()) )
print('O seu nome em minusculas e {}'.format(name.lower()))

#Forma que eu utilizei para resolver
print('Seu nome tem ao todo {} letras'.format(len(name.replace(' ',''))) )
#Rsolução do exercicio
print('O seu nome tem {} letras'.format(len(name) - name.count(' ')))

name1 = name.split()
print('O seu primeiro nome possui {} letras'.format(len(name1[0])) )
#Rsolução do exercicio, ele encontra o index do primeiro espaco da frase
print('O seu primeiro nome tem {} letras'.format(name.find(' ')))
