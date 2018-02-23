#ex022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as Letras maiusculas
#-O nome com todas as minusculas
#-Quantas letras ao todo(sem considerar espacos)
#-Quantas letras tem o primeiro nome

name = str(input('Digite um nome completo: '))

print(name.upper())
print(name.lower())
print(len(name.replace(' ','')))
name1 = name.split()
print(len(name1[0]))


# frase = 'Curso em Video Python'
# print('Curso' in frase)
# print(frase.find('Video'))
#
# dividido = frase.split()
# print(dividido)
# print(dividido[2][3])