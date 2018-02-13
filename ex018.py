#ex018
#Faça um programa que leia umângulo qualquer e mostra na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians, degrees
n1 = radians(float(input('Digite um angulo qualquer: ')))
#Calculating the sin, cos and tan

seno = sin(n1)
cose = cos(n1)
tang = tan(n1)

print('O valor do seno em graus é: {:.2f}\nO valor do cosceno em graus é: {:.2f}\nO valor da tangente em graus é: {:.2f}'.format(degrees(seno), degrees(cose), degrees(tang)) )
print('O valor em radianos do seno é {:.2f}, do cosseno é {:.2f} e da tagente é {:.2f}'.format(seno, cose, tang) )