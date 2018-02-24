#ex027
#Faca um progrmaa que leia o nome completa de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
#ex:Ana Maria de Souza
#primeiro = Ana
#ultimo = Souza
name = str(input('Digite um nome completo de uma pessoa: '))
check1 = name.split()
print('Primeiro nome: {}'.format(check1[0]))
print('O ultimo nome: {}'.format(check1[-1]))
