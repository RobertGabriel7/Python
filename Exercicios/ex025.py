nome = str(input('Digite o seu nome: ')).strip()
nome1 = nome.lower()

nome2 = ('silva' in nome1)

#print(nome2)

nomeCert = 'SILVA'

#True precisa ser MAIUSCULO

if nome2 == True:

    print('O nome digitado é "{}" e tem o nome "{}", sim!'.format(nome, nomeCert))

else:

    print('O nome digitado é "{}" e não tem o nome "{}".'.format(nome, nomeCert))


#FEITO GRAÇAS A DEUS!