#Aula 12 - Mundo 2

nome = str(input("Digite o seu nome: "))
if nome == 'Gustavo':
    print("Que nome horrendo!")
elif nome == 'Pedro' or nome == 'Maria' or  nome == 'Paulo':
    print("Seu nome é bem popular  no brasil!")
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia {}'.format(nome))