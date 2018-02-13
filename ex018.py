from math import sin, cos, tan, radians, degrees
n1 = radians(float(input('Digite um angulo qualquer: ')))
#Calculating the sin, cos and tan

seno = degrees(sin(n1))
cose = degrees(cos(n1))
tang = degrees(tan(n1))

print('O valor do seno é: {:.2f}\nO valor do cosceno é: {:.2f}\nO valor da tangente é: {:.2f}'.format(seno, cose, tang))
