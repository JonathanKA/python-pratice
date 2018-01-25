n1 = float(input('Digite sua 1 nota:\n'))
n2 = float(input('Digite sua 2 nota:\n'))
n3 = float(input('Digite sua 3 nota:\n'))
n4 = float(input('Digite sua 4 nota:\n'))

med = (n1 + n2 + n3 + n4)/4
print('Sua notas foram: {:.1f}, {:.1f}, {:.1f}, {:.1f}.\nSua media é {}'.format(n1, n2, n3, n4, med))