
nome = str(input('Qual o seu nome: '))

print(' \n "{}" em letras MAIUSCULAS: '.format(nome),nome.upper())

print(' \n "{}" em letras minusculas: '.format(nome),nome.lower())

nome1 = nome.replace(' ','')

print('Quantidade de caracteres digitados, sem considerar os espaços:',len(nome1))


#Estou separando as palavras em lista para depois selecionar alguma palavra pelo seu indice

nome2 = nome.split()

#Pego a quantidade de caracteres do indice 0

print('Quantidade de letras do seu primeiro nome: ', len(nome2[0]))

#FEITO GRAÇAS A DEUS!