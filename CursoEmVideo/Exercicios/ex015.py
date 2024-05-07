print('>>>>>>>>>>>>>>> Aluguel de Carro >>>>>>>>>>>>>>> \n')
print('Para alugar custa R$60 o dia e R$ 0,15 por KM rodado.')
input('Dseja alugar? ')

dia = int(input('Quantos dia ficou com o carro: '))
km = float(input('Quantos Km vai percorre com o carro: '))


soma1 = (km*0.15)+(dia*60)

print(' \n Você rodou {} km e ficou {} dias com o com o carro. Com isso, valor total é de R$ {}'.format(km,dia, soma1))