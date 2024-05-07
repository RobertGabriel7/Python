
nome = str(input('Qual o seu nome: ')).strip()

print('\n"{}" em letras MAIUSCULAS: '.format(nome),nome.upper())

print('\n"{}" em letras minusculas: '.format(nome),nome.lower())

nome1 = nome.replace(' ','')

print('\nQuantidade de caracteres digitados, sem considerar os espaços:',len(nome1))


#Estou separando as palavras em lista para depois selecionar alguma palavra pelo seu indice

nome2 = nome.split()

#Pego a quantidade de caracteres do indice 0

print('\nQuantidade de letras do seu primeiro nome: ', len(nome2[0]))
print('\n')
#FEITO GRAÇAS A DEUS!