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

carros1 = ("palio", "gol", "celta", "palio")

for carro in carros1:
    
    print(f"Indice: , Carro: {carro}")
    

""" Métodos da class Set """

""" Para unir coleções: {}.union """

conjuntoA = {1, 2}
conjuntoB = {3, 4}

print(conjuntoA.union(conjuntoB)) # {1, 2, 3, 4}

""" 
Interseguição é a parte do conjunto que são iguais. 

"""

conjuntoA1 = {1, 2, 3}
conjuntoB1 = {2, 3, 4}

print(conjuntoA1.intersection(conjuntoB1)) # {2, 3}

""" difference é a diferença entre os valores do conjunto """

print(conjuntoA1.difference(conjuntoB1)) # {1}
print(conjuntoB1.difference(conjuntoA1)) # {4}

""" symmetric_difference pega todos os elementos que não estão interseguição.  Esse método é melhor do que o diference """

print(conjuntoA1.symmetric_difference(conjuntoB1))

""" issubset serve para saber se um conjunto faz parte de outro conjunto """

conjuntoB1 = {4, 1, 2, 5, 6, 3}

#Todos os elementos de A1 estão em B1? True 
print(conjuntoA1.issubset(conjuntoB1)) # True
# TOdos os elementos de B1 estão em A1? False
print(conjuntoB1.issubset(conjuntoA1)) # False

""" issuperset é o contrario do issubset """

# Todos os elementos de B1 estão em A1? False
conjuntoA1.issuperset(conjuntoB1) # False
# Todos os elementos de A1 estão em B1? True
conjuntoB1.issuperset(conjuntoA1) # True

""" isdisjoint serve para saber se todos ou alguns elementos de outro conjunto estão em outro conjunto """

conjuA = {1,2,3,4,5}
conjuB = {6,7,8,9}
conjuC = {1,0}

# Se acontecer a interseguição, será retornado False
print(conjuA.isdisjoint(conjuB)) # True
print(conjuA.isdisjoint(conjuC)) # False 

""" Para adicionar elementos/valores não existente: {}.add """

