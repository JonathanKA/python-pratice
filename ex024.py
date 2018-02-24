#ex024
#Crie um programa que leia o nome de uma cidade  e diga se  ela comeca ou nao com nome "SANTO"
cidade = str(input('Digite o nome de uma Cidade :'))
lista = cidade.split()

print('Santo' in lista[0])
