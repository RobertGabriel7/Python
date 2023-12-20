frase = input("Escreva uma frase... ").strip()


#Vai contar quantas vezes apareceu a letra a na frase 
print('A letra "a" apareceu {} vezes na frase escrita.'.format(frase.count('a') + 1))

#Vai mostrar a posição que a primeira letra "a" apareceu. +1 porque começa a partir do 0
print('A posição que a letra "a" apareceu primeira vez foi na: {}°'.format(frase.find('a',0) + 1))

#Vai mostrar a posição que a ultima da letra "a", da direita para esquerda. +1 porque começa a partir do 0
print('A posição que a letra "a" apareceu a ultima vez: {}°'.format(frase.rfind('a') + 1))

#FEITO GRAÇAS A DEUS!