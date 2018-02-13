import math
n1 = float(input('Digite o valor do cateto oposto do triângulo retângulo: '))
n2 = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = math.hypot(n1, n2)
hipo2 = math.sqrt(math.pow(n1, 2) + math.pow(n2, 2))
#quadrado da hipotenusa = soma dos quadrados dos catetos a²+b²=c²

print('O valor da hipotenusa é {}'.format(hipotenusa))
print(hipo2)
