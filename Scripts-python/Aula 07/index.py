
# Elevado ao Quadrado: **
# Divisão inteira: //
# Resto da divisão: %
# 10 elevado a 7: 10*10*10*10*10*10*10
# 5 elevado a 2: 5*5

#Ordem de Precedência

#1 - ()
#2 - **
#3 - * / // %
#4 - + -

# '-'*10 o resuktado é: '----------'

#Aumenta o resultado em 20 caracteres

nome = input('Qual o seu nome ? ')
print('Seja bem-vindo {:-^20}!'.format(nome))

#Qual o seu nome ? Robert
#Seja bem-vindo -------Robert-------!

nome = input('Qual o seu nome ? ')
print('Seja bem-vindo {:^20}!'.format(nome))

nome = input('Qual o seu nome ? ')
print('Seja bem-vindo {:>20}!'.format(nome))

nome = input('Qual o seu nome ? ')
print('Seja bem-vindo {:<20}!'.format(nome))

#Continuação...

n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))

print('Soma vale {}'.format(n1+n1))

#Sem criar uma variavel para armazenar os dados, todos eles serão perdidos

#end='' não quebra a linha

print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {}, '.format(n1+n2, n1-n2, n1*n2, n1/n2), end=' ')

print('A potenciação é {}, a divisão inteira é {}, resto da divisão é {}'.format(n1**n2,n1//n2,n1%n2))


# \n quebra linha
# end=' >>>>>>>>>>>>> '


