""" A função dir() em Python é usada para listar os atributos e métodos disponíveis em um objeto ou no escopo atual. """
from ast import If

carro = "camaro"

ano = 2012

print(carro, ano)

""" dir() mostra as bibliotecas que estão no scope local """

dir() 

""" Mostra os metodos inteiros  """

dir(100)

""" Mostra quais argumentos os metodos recebem """

""" help() """

""" help (int) """


""" Para teste se uma variavel tem o mesmo espaço na memoria """

curso = 200
curso1 = 200

print(curso is curso1)

""" ou """

print(curso is not curso1)

""" Operadores de associação """

frutas = ["Banana", "Maça", "Uva", "Laranja"]

print("Laranja" in frutas)

""" O Python usa 4 espaços para um novo bloco de código """

if (curso):
    print("opa")
else:
    print("opaaaaaaaaaa")
    
    
""" String com 3 aspas duplas, o python respeita os espaços """


""" Inverte a ordem do texto """
curso = "Python"                                                     
print(curso[::-1])   