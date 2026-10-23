from carro import Carro
from moto import Moto

# Carros

carro1 = Carro('Lamborghini', 'Gallardo', 2)
carro2 = Carro('Toyota', 'Corolla', 4)
carro3 = Carro('Volkswagen', 'Golf', 4)

# Motos

moto1 = Moto('Kawasaki', 'Ninja H2R', 'Esportiva')
moto2 = Moto('Honda', 'CG 160', 'Casual')
moto3 = Moto('Yamaha', 'MT-09', 'Esportiva')

# Exibindo as informações
print(carro1)
print(carro2)
print(carro3)
print('\n')
print("-" * 50)
print(moto1)
print(moto2)
print(moto3)