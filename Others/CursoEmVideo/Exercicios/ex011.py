lar = float(input('Lagura da parede: '))
altu = float(input('Altura da parede: '))

area = lar * altu

print('\n A dimensão da sua parede {}x{} e sua área é {}m². \n'.format(lar,altu,area))

print('Para pintar a parede você precisa de {:.3f} litros de tinta. \n'.format(area/2))