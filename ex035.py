#ex035
# Desenvolva um progrmaa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
print('-='*20)
print('Analisador de Triângulos')
print('=-'*20)
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('Os Segmentos PODEM formar um triângulo')
else:
    print('Os Segmentos acima NÃO PODEM formar um triângulo')