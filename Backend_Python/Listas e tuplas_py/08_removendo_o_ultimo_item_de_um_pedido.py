listaFinal = []

pedidosFeitos = input('Pedidos feitos (separe cada por virgula): ').split(',')

for item in pedidosFeitos:
    
    listaFinal.append(item.strip())
    #pedidosFeitos[pedidosFeitos.index(item)] = item.lstrip().rstrip()
    
listaFinal.pop()

print(f'\nPedidos finais: {listaFinal}')