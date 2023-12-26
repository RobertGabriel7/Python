primeiroNumero  = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
terceiroNumero = int(input('Digite o terceiro numero: '))

""" Criei uma lista para colocar os valores digitados """
numeros = [primeiroNumero, segundoNumero, terceiroNumero]
""" Coloquei os valores em ordem crescente com a função sorted(varivael) """

""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> """
numeroEmOrdem = sorted(numeros)
""" com [-1]  seleciono o ultimo valor da lista """
print('O maior numero digitado foi "{}".'.format(numeroEmOrdem[-1]))

""" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> """
""" Ou eu posso usar esse jeito """
""" Aqui, eu selecionei o primeiro valor [0], coloquei os numeros em  ordem, mas em ordem decrescente """

numerosEmOrdem1 = sorted(numeros, reverse = True)

print('O maior numero digitado foi "{}".'.format(numerosEmOrdem1[0]))

""" Pode usar o metodo varivael.sort() """