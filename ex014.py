cel = float(input('Type the value in Celsius:\n'))
faren = (cel * 1.8) + 32 #sintaxe da internet que tbm funciona
#faren = ((9*cel)/5)+32 #formula correta
print('The temperature in Celsius was {:.2f}°c in Farenheit is {:.2f}°f'.format(cel, faren))