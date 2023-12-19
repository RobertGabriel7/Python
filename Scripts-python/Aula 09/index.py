frase = 'Curso em Vídeo Python'

print(frase[9])


#len(variavel) diz a quantidade de caracteres em uma variavel

print(len(frase))


print('\n')

print(frase[9:13])

#Nesse exemplo abaixo, será exibido do indice 9 até o 20, mas pulando 2 em 2: frase[9:21:2] 

print(frase[9:21:2])

#Quando não indica o inicio, vai começar do zero.

print(frase[:5])

#Semelhante ao exemplo acima, mas ao contrario. Partir do 15 até o ultimo.

print(frase[15:])

#Partir do 9 até o final pulando 3 em 3

print(frase[9::3])

#count('caractere') vai contar a quantidade de caracteres que foi escrito.

print(frase.count('r'))

#no exemplo abaixo, o método vai contar a quantidade de 'r', a partir do indice 0 até o 14 (é considerado apenas o penultimo numero/indice) 

print(frase.count('r',0,15))

#Vai dizer em qual indice começou o 'em'

print(frase.find('em'))


#Quando é digitado uma string que não tem na variavel, o método vai retornar -1 porque não foi encontrado.

print(frase.find('IOS'))


#Dentro da varivael frase existe a palavra Curso 

print('Curso' in frase)


















