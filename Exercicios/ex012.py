valor = float(input('Digite o valor do produto: R$'))

resul = valor - (valor*5/100)

print('Valor do produto antes do disconto era de R${}. Agora com 5% de desconto, ficou R${:.5}! \n'.format(valor,resul))

#feito