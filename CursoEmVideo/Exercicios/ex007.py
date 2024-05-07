print('Seja mutio bem-vindo(a) ao Boletim escolar 2023!')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
print('Antes começar, gostaria de saber o nome do aluno(a), por favor.')
nome = input('Nome: ')
print('Que nome legal, {}, ai simm em !'.format(nome))
print('Certo, agora vamos calcular a nota do(a) {}!'.format(nome))
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

nota1 = int(input('Digite a primeira nota do aluno(a): '))

nota2 = int(input('Digite a segunda nota do aluno(a): '))

print('>>>>>>>>>>>>>>>>> Resultado <<<<<<<<<<<<<<<<<\n')

print('{0}, a média da sua nota é: {1}'.format(nome,(nota1+nota2)/2))