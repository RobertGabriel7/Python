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


#Dentro da varivael frase existe a palavra Curso ?

print('Curso' in frase)

#Com o replace é possivel alterar os elementos a partir desse método. Primeiro selecione a palavra antiga e depois coloque a palavra nova.

print(frase.replace('Python','PYTHON'))

#Para deixar em MAIUSCULO

print(frase.upper())

#Para deixar em minusculo

print(frase.lower())

#A primeira letra será MAIUSCULA e todas as outras serão minusculas

print(frase.capitalize())

#A primeira letra de todas as palavras serão MAIUSCULA, apenas a primeira.

print(frase.title())

#Remove todos os espaços desnecessarios. Deixa apenas o espaço do meio. Espaços antes e no fim da palavra é retirado.

frase2 = '   Aprenda Python  '


print(frase2.strip())


#* A letra r no python trata de algo a direita (right) *

#Remover espaços da direita e manter da esquerda

print(frase2.rstrip())

#Remover espaços da esquerda e manter da direita

print(frase2.lstrip())


#variavel.split() Ao inves de considerar os espaços e conta-los, o split() só considera as strings e sepera elas por listas. Por exemplo:

# C u r s o   e m  V i d e o 
# 0 1 2 3 4   0 1  0 1 2 3 4 


#Cada palavra recebe indexação nova 

#Cada uma dessas palavras é colocada dentro de uma lista, o split regera uma lista e coloca essas frases em indices 


frase3 = 'Curso de Python é top'


print(frase3.split())

#' '.join(frase3) junta as string separadas por listas. 

print(' '.join(frase3))


#Para textos longos que precisa pular linha, só precisa colocar 3 parenteses. Por exemplo:

print(""" Portanto, a principal diferença está na associação a objetos: uma função é independente, enquanto um método está associado a um objeto específico. Ambos são usados para realizar operações e modularizar o código, promovendo a reutilização. """)


#Joga a frase em letra MAIUSCULA e conta a quantidade de letra O

print(frase3.upper().count('O'))

frase4 = 'Curso em video Python'

dividido = frase4.split()

#Acessando o indice 2 da lista e a 3 palavra

print(dividido [2] [3])

