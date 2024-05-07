import random

a1 = str(input('Primero aluno(a): '))
a2= str(input('Segundo aluno(a): '))
a3 = str(input('Terceiro aluno(a): '))
a4 = str(input('Quarto aluno(a): '))

lista = [a1,a2,a3,a4]

result = random.shuffle(lista)

print('Ordem de apresentação:',lista)




