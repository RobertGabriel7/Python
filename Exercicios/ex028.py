import random
import time

numeroAleatorio = random.randint(0,5)

numeroDigitado = int(input('O computador pensou em um numero de 0 a 5.\nAgora tente adivinhar esse numero: ' ))

print('\nPROCESSANDO...\n')

time.sleep(2)


if numeroDigitado == numeroAleatorio:
    print('Oloco, vc adivinhou o numero que o computador pensou que é o nuemro "{}".'.format(numeroAleatorio))
else:
    print('Poxa -_-, vc não adivinhou o nuemro que o computador pensou.')
    print('O numero digitado foi "{}" e o computador pensou no numero "{}"'.format(numeroDigitado, numeroAleatorio))

#FEITO GRAÇAS A DEUS!