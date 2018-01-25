metros = float(input('Digite o valor em metros a ser convertido:\n'))

km = metros / 1000
hm = metros / 100
dam = metros / 10
m = 1
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('{} metros equivale a {} centimetros e {} milimetros.'.format(metros, cm, mm))
print('Km igual a {}\nHm igual a {}\nDam igual a {}\nMetro igual a {}\nDm igual a {}\nCm igual a {}\nMm igual a {}'.format(km, hm, dam, metros, dm, cm, mm))
