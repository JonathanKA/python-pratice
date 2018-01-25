v1 = int(input('Type a value:\n'))

double = v1 * 2  # mutiply by 2
triple = v1 * 3  # mutiply by 3
square = v1 ** (1/2)  # square root(raiz quadrada é aquela que divide nao confuda com numero elevado)
                      # tem um funcao no modulo math tbm ou usando pow( v1, (1/2))
#todos os codigos acima pode ser feitos no print
print('The double of this value is:\n{}'.format(double))
print('The triple of this value is:\n{}'.format(triple))
print('The square root of this value is:\n{:.2f}'.format(square))
