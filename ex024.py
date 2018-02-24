#ex024
#Crie um programa que leia o nome de uma cidade  e diga se  ela comeca ou nao com nome "SANTO"
cidade = str(input('Digite o nome de uma Cidade :')).strip()
lista = cidade.upper().split()

print('SANTO' in lista[0])

#Resolucao do exercicios

print(cidade[:5].upper() == 'SANTO')