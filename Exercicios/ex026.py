frase = input("Escreva uma frase... ")


#Vai contar quantas vezes apareceu a letra a na frase 
print('A letra "a" apareceu na frase escrita.', frase.count('a'))

#Vai mostrar a posição que a primeira letra "a" apareceu
print('A posição que a letra "a" apareceu primeira vez foi na: {}°'.format(frase.find('a',0,)))

#Vai mostrar a posição que a ultima da letra "a", da direita para esquerda 
print('A posição que a letra "a" apareceu a ultima vez: {}°'.format(frase.rfind('a')))

#FEITO GRAÇAS A DEUS!