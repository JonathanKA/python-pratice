#ex022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as Letras maiusculas
#-O nome com todas as minusculas
#-Quantas letras ao todos(sem considerar espacoes)
#-Quantas letras tem o primeiro nome

frase = 'Curso em Video Python'
print('Curso' in frase)
print(frase.find('Video'))

dividido = frase.split()
print(dividido)
print(dividido[2][3])