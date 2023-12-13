#Esse módulo (biblioteca) eu encontrei no PyPi, instalei e testei. Deu tudo certo, porém todos cpf são false. Por enquanto n sei resolver isso mas valeu a pena aprender a instalar e testar esse módulo de CPF.





import cpf

nu = cpf.gerar(1,1)

print(nu)

print('\nAgora vamos checar o CPF: {}'.format(nu))

print('O CPF: {} é:\n{}'.format(nu,cpf.checar(nu)))

print(cpf.checar('nu',True))



