#A variavel vai recber o nome sem os espaços laterais e todos os caracteres em minusculos

nomeCIty = input('Digite o nome de uma cidade: ').strip()

priPala = nomeCIty.split()

nomeTeste = str(priPala[0]).upper()

nomeSolici = 'SANTO'

if nomeTeste == 'SANTO':

    print('O nome da cidade digitada é {} e começa com "{}", sim!'.format(nomeCIty,nomeSolici))

else:

    print('O nome da cidade digitada é {} e não começa com "{}"!'.format(nomeCIty, nomeSolici))


    #FEITO GRAÇAS A DEUS!
