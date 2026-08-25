"""

Functions é um bloco de código que pode realizar alguma funcção, por exemplo, calcular dois valores, trocar valores de listas e objetos. É possível fazer muitas coisas com functions.

A function retorna por padrão "none"

"""
# Para declarar uma function
# def é um nome reversado no python para definir uma funciton 

# Parâmetros especiais: para uma melhor legibilidade e desempenho é legal restrigir quais argumentos serão passados em uma function, por exemplo por posição, por posição E nome, ou somente pelo nome.

# Parâmetros com nome: chave-valor * valor
# Parâmetros por posição: valor / saldo=valor

# Antes da barra, os valores são passados por posição, após a barra, os valores são passados por chave-valor 

print(10*"-", "Position and Keyword", 10*"-")
def criarCarro(modelo, ano, placa, /, marca, motor, combustivel):
     print(modelo, ano, placa, marca, motor, combustivel)

# Aqui os valores foram passados por posição
criarCarro("Veluster", 2024, "A1B2", "chevroleti", "V12", "uranio")

# Ou, dessa maneira mais correta:
# Aqui os valores foram passados por posição e por nome (chave-valor), mas antes da barra NÃO PODE passar os valores utilizando chave-valor, mas somente o valor.

criarCarro("Ferari", "Ferrai 458", "A7B7", marca="Mustangui", motor="V9", combustivel="uranio")

# Keyword only: chave-valor
print(10*"-", "Keyword only: chave-valor", 10*"-")


def criarCarinhos(*, modelo, ano, placa,  marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criarCarinhos(modelo="Porsche", ano=2023, placa="R7T7", marca="Porsche", motor="V12", combustivel="Uranio")  

print(10*"-", "Keyword and position", 10*"-")

def criarCarinhos1( modelo, ano, placa, /, *,  marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criarCarinhos1("Ferari", "Ferrai 458", "A7B7", marca="Mustangui", motor="V9", combustivel="uranio")

print(10*"-", "Object first Class", 10*"-")

# Em Python tudo é objeto, dessa forma funções são tambèm objects o que as tornam objetos de primeira classe. Com isso é possível atribuir funções a uma variavel, passá-las como parâmetro para funções, usá-las como valores em uma estrtura de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures)

# Function para somar valores
def somar(a, b):
    return a + b

# Function para subtrair
def subtrair (a, c):
    return a - c

# Essa function pega a
def exibirResultado(a, b, function1):
    # Aqui a function pasasda como parêmtro recebe o valor de a e b. com isso a function somar(), soma os valores, retorna os valores que serão atribuidos para a variavel resultado.
    resultado = function1(a, b)
    print(f"Resultado: {resultado}")
    
# Chama a function exibirResultado(), passa os valores de a e b e passa uma function como parâmetro 
exibirResultado(3, 4, somar) # 3 + 4 = 7

exibirResultado(10, 10, subtrair) # 10 - 10 = 0

# Function atribuida para uma variavel 
# Não precisa colocar parênteses
oloco = somar

print(f"Function soma() atribuida a variavel oloco, resultado dessa operação: {oloco(10,10)}")

print(10*"-", "Escopo local e Global", 10*"-")

# Para usar variaveis do escopo global em escopo local

salario = 2500

def salarioBonus(bonus, lista):
    # Aqui a variavel global salaria é acessada dentro desse bloco da function 
    global salario
    salario += bonus
    
    # Trabalhar com uma lista global e não modificar o seu valor em uma function
    
    listaAux = lista.copy()
    listaAux.append(8)
    return print(salario, listaAux)

lista = [1]
salarioBonus(777, lista)
print(f"Lista global: {lista}")
