
velocidade = int(input('Qual foi a velocidade do carro?  ')) 

if velocidade > 80:
    print('Você foi multado porque excedeu o limite de 80km/h, você estava a {}km/k'.format(velocidade))
    print('>>>> POR ISSO <<<<')
    print('O valor da multa é R${}'.format( 7 * (velocidade - 80)))

else:
    print('Tá de boas, você não tomou multa porque estava andando a {}km/h.'.format(velocidade))
    print('Toma cuidado, se não já sabe né...')

    #FEITO GRAÇAS A DEUS!