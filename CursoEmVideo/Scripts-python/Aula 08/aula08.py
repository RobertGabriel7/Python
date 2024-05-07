from math import sqrt, ceil, floor
#ctrl + espaço mostra todas as opções


num = int(input('Digite um número: '))

#Quando for importar apenas uma função da biblioteca, não precisa usar math. apenas a função sqrt 
#raiz = math.sqrt(num)

raiz = sqrt(num)

#math.ceil(raiz) vai arredondar o número pra cima

print('A raiz quadrada de {} é igual a {:.2f}.'.format(num,floor(raiz)))