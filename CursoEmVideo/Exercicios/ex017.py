from math import hypot

b = float(input('Digite o valor do cateto adjacente y = '))
c = float(input('Digite o valor do cateto oposto x =  '))

print('Com base no valor do cateto adjacente: {} e o cateto oposto: {}. A hipotenusa é: {:.2f}'.format(b,c,hypot(b,c)))
