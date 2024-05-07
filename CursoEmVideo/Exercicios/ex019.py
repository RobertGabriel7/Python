import random

a1 = input('Digite o nome do primeiro aluno(a): ') 
a2 = input('Digite o nome do segundo aluno(a): ')
a3 = input('Digite o nome do terceiro aluno(a): ')
a4 = input('Digite o nome do quarto aluno(a): ')

sele = [a1,a2,a3,a4]

print('O aluno(a) que vai apagar o quadro é: {}'.format(random.choice(sele)))


#