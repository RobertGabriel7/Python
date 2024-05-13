"""

Functions é um bloco de código que pode realizar alguma funcção, por exemplo, calcular dois valores, trocar valores de listas e objetos. É possível fazer muitas coisas com functions.

A function retorna por padrão "none"

"""
# Para declarar uma function
# def é um nome reversado no python para definir uma funciton 
def teste():
    print("Aula de function")
    
    
teste()

def nome(nome):
    print(f"Nome: {nome}")
    
    
nome("Robert")

def soma(n1, n2):
    return print(f"{n1} + {n2} = {n1+n2}")


soma(3,4)

# No python é possível retornar dois valores em uma function

def retornaAntecessor_e_Sucessor(numero):
    
    antecessor = numero - 1
    sucessor = numero + 1
    
    # Retornando dois valores 
    return antecessor, sucessor

print(retornaAntecessor_e_Sucessor(8))
       
# Uma function pode ser chamada usando argumentos nomeados da forma chave-valor.

def carroNovo(marca, modelo, ano, placa):
    print(f"Marca: {marca}, Carro: {modelo}, Ano: {ano}, Placa: {placa}")
    
carroNovo("Chevrolet", "Camaro ZL1", 2012, "777ABC")

# Para não ter problema no momento de passar os valores para os parâmetros, é legal passar uma biblioteca, por exemplo:


# Passa uma biblioteca como parâmetro para a function 
carroNovo(**{"marca": "Ferrai", "modelo": "Ferrari 458 spider", "ano": 2015, "placa": "77RT7"})


# Quando *Args e **Kwargs são definidos, o método recebe valores como tuplas e dicionários respectivamente.

# *Args = os valores vem em um tupla
# **Kwargs = os valores vem em um dictionary

def exibir_poema(data_extenso, *args, **kwargs):
    # Define uma função chamada exibir_poema que recebe como argumentos obrigatórios uma data por extenso (data_extenso)
    # e argumentos opcionais (args) e argumentos nomeados opcionais (kwargs).

    texto = "\n".join(args)
    # Une os argumentos opcionais em uma única string, separando-os por quebras de linha ("\n").

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    # Cria uma string contendo os argumentos nomeados opcionais (kwargs) formatados como chave: valor, 
    # onde chave é convertida para título (title()), e os elementos são separados por quebras de linha ("\n").

    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    # Cria a mensagem final concatenando a data_extenso, o texto dos argumentos e os meta_dados,
    # separados por duas quebras de linha ("\n\n").

    print(mensagem)
    # Imprime a mensagem final na saída padrão.
