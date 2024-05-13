from numpy import linspace


lista = []

""" Adiciona valores ao ultimo indice de uma lista/array """
lista.append("Python")

""" Para limpar a lista """
lista.clear()

""" Para copiar uma lista  """
""" Quando os valores de uma lista é copiado para outra, esses valores não sofrem alteram mesmo que tenha copiado os valores """

copyList = lista.copy()

""" Por exemplo, os IDs das lista, mesmo tendo os valores, são diferentes """

print(id(copyList), id(lista))

""" extend adiciona/junta valores a uma lista """

linguagens = ["Python", "PHP", "C#"]

print(linguagens)

linguagens.extend(["Javascript", "MySQL"])

print(linguagens)


""" Para retorna o index do elemento """

linguagens.index("PHP") # 0

linguagens.index("C#") # 1

""" pop() remove um elemento """

linguagens.pop(4)

print(linguagens)

""" remove() é a segunda de remover elementos de uma lista """

linguagens.remove("Python")

""" reverse() para inverter a ordem dos elementos da lista """

linguagens.reverse()

""" Para colocar em ordem alfabetica (se for strings) """

linguagens.sort()
linguagens.sort(reverse=True)
""" Para ordenar pela quantidade de letras """
linguagens.sort(key=lambda x: len(x))
linguagens.sort(key=lambda x: len(x), reverse=True)

""" len() serve para saber o tamanho da lista """
len(linguagens)

print("_---------------------------------------------------_")

n = 2

teste = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 

print(teste)