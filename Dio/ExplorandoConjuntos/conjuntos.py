""" 

Conjuntos é uma estrutura de dados

Criando sets: Um set é uma coleção que não possui elementos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um 

Iteravel = É aquilo que se repete ou é feito outra vez.

"""

numeros = [1, 2, 3, 4, 5, 5, 7, 1, 1]

""" Remove elementos repetidos de uma lista e devolve em uma class """
print(set(numeros)) # {1, 2, 3, 4, 5, 7}

print(set("abacaxi")) # {'a', 'i', 'x', 'b', 'c'}

carros = set(("palio", "gol", "celta", "palio"))

print(carros) # ('palio', 'gol', 'celta', 'palio')


""" Para acessar os elementos do set, precisa converte para uma lista """

opa = list(set(numeros))

print(opa[0])


""" Para percorrer os elementos de uma coleção (set) """


for elementos in carros:
    print(elementos)


""" Para saber o indice que for utilizado o "for" """
#for variavel para receber o indice, variavel para receber os valores da list, object, set carros
for indice, carro in carros:
    print(f"Indice: {indice}, Carro: {carro}")
    

""" Métodos da class Set """

""" Para unir coleções: {}.union """

conjuntoA = {1, 2}
conjuntoB = {3, 4}

print(conjuntoA.union(conjuntoB)) # 