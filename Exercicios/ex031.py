distanciaDaViagemEmKm = int(input('Qual a distancia da viagem em Km: '))

if distanciaDaViagemEmKm <= 200:
    print('A distancia da viagem é {} e será cobrado R$ 0,50 por Km (isso se for abaixo de 200Km de distancia). O valor total é {}'.format(distanciaDaViagemEmKm, 0.50 * distanciaDaViagemEmKm ))
else:
    print('A distancia da viagem é {} e será cobrado R$ 0,45 por Km (isso se for acima de 200Km de distancia). O valor total é {:.2f}'.format(distanciaDaViagemEmKm, 0.45 * distanciaDaViagemEmKm ))
    
    """ Outra maneira """
    """ 
    preco = distanciaDaViagemEmKm * 0.50 if distanciaDaViagemEmKm <= 200 else distanciaDaViagemEmKm * 0.45
 """
    #FEITO GRAÇAS A DEUS!