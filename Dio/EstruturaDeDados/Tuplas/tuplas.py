""" 
Tuplas são semelhante as listas, porém os seus valores não podem ser mudados.

tipo assim:

var, let = listas/array
const = tuplas

"""

""" Para criar uma tuple é usado a class tuple ou não """

#Exemplo de uma tuple
#Sempre colocar uma virgula no final
frutas = ("Laranja", "Manga", "Banana",)

#Coloca as letras em indices separados
linguagem = tuple("python")

#Passando uma lista para uma tuple 
numeros = tuple([1,2,3,4,5])

#
pais = ("Brasil",)

print(linguagem)


""" Para acessar os elementos em uma tuple """

print(frutas[0])


""" Tuplas bidimensionais """

#Quando tem somente um elemento de uma tuple dentro de outra tuple, para selecionar basta dizer o indice da primeira tuple
carros = ("ferrari", ("camaro"), "Porsche")

print(carros[1])

""" É possivel fazer o fatiamento da tuple igual a listas """

""" 
Posso usar a maioria metodos da lista/araay nas tuples também.

E posso usar algumas coisas da estutura de dados.
"""

