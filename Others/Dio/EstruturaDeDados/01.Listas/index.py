""" Uma lista pode armazenar de maneira sequencial qualquer tipo de objeto e dado.

Lista nada mais que arrays

"""
mercado = []
frutas = ['Laranja', 'Uva', 'Banana', 'Manga']

# Para acessar os elementos da esquerda para a direita. Começa a partir do 0

frutas[0]
frutas[2]

# Para acessar os elementos da direita para esquerda. Começa a partir do -1
frutas[-1] # Manga
frutas[-2] # Banana

""" Com essa function/method, a variavel letras receba uma lista/array com as letras separa e armazenadas por indeces da palavra python """
letras = list('python')

print(letras[2])

""" numeros recebe uma lista/array e nessa atribuição tem uma function chamada de range() que conta de 0 até o valor passado para essa function, semelhamente no exemplo abaixo: """
numeros = list(range(10))

print(numeros)

carro = ['Ferrari', 'F8', 422000, 2022, 2900, True]

print(type(carro))


""" Matriz é uma lista/array bidimensional, ou seja, igual uma tabela. """

# Para acessar os elementos da direita para esquerda. Começa a partir do -1
# Para acessar os elementos da esquerda para a direita. Começa a partir do 0

matriz = [ 

          ["Camaro", "ZL1", 2021], 
          ["Ferrari", "458", 2015], 
          ["Porsche", "911", 2018]

]

# Para acessar array, array e string: carroEsportivo = matriz[0][0][2]
carroEsportivo = matriz[0][0]
carroDeLuxo = matriz[2][0]
carroExotico = matriz[1][0]

print(carroEsportivo)
print(carroDeLuxo)
print(carroExotico)


""" Fatiamento """

# Definindo uma lista de exemplo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fatiamento básico: selecionando elementos de determinadas posições
print("Fatiamento básico:")
print(lista[2:5])  # Retorna elementos da posição 2 até a posição 4 (exclusivo)

# Fatiamento com início e fim não especificados
print("\nFatiamento com início e fim não especificados:")
print(lista[:5])   # Retorna elementos do início até a posição 4
print(lista[5:])   # Retorna elementos da posição 5 até o final
print(lista[:])    # Retorna todos os elementos da lista

# Fatiamento com passo
print("\nFatiamento com passo:")
print(lista[::2])  # Retorna todos os elementos com um passo de 2
print(lista[1::2]) # Retorna todos os elementos a partir da posição 1 com um passo de 2

# Fatiamento reverso
print("\nFatiamento reverso:")
print(lista[::-1])  # Retorna todos os elementos em ordem reversa
print(lista[8:3:-1]) # Retorna elementos da posição 8 até a posição 4 (exclusivo) em ordem reversa

# Fatiamento com atribuição
print("\nFatiamento com atribuição:")
lista[1:3] = [11, 12]  # Substitui elementos da posição 1 até a posição 2 pelos novos valores
print(lista)

# Fatiamento com elementos de índices negativos
print("\nFatiamento com índices negativos:")
print(lista[-5:])  # Retorna os últimos 5 elementos da lista

# Fatiamento com índices negativos e passo negativo
print("\nFatiamento com índices negativos e passo negativo:")
print(lista[-2::-1])  # Retorna todos os elementos, exceto o último, em ordem reversa

# Fatiamento para cópia
print("\nFatiamento para cópia:")
copia_lista = lista[:]  # Copia todos os elementos da lista para uma nova lista
print(copia_lista)

""" Para percorrer uma lista/array """

for valores in frutas:
    print(valores)
    
""" for indice( literalmente o indice ), variavel que vai receber os valores da lista/array, enumerate( lista/array que contem os valores ) """
for indice, frutass in enumerate(frutas):
    
    print(f"indice: {indice}: {frutass}")


""" Para atribuir valores de uma lista/array para outra lista/array """
    
""" Filtro Versão 1 """    
    
numbersz = [1, 2, 7, 5, 8, 9, 10]
pares = []
    
for numeros1 in numbersz:
    
    if (numeros1 % 2 == 0):
        # append() é um method para adicionar valores para uma no final do lista/array 
        pares.append(numeros)
        print(f"Filtro versão 1: {pares}")
    
""" Filtro Versão 2 """
#            retorno 
pares = [numero for numero in numbersz if numero % 2 == 0]

print(f"Filtro versão 2: {pares}")

""" Modificando valores """
rootQuadrado = [numero ** 2 for numero in numeros]

print(f"Raiz quadrada: {rootQuadrado}")