from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))

#Precisa colocar radians porque o valor precisa ser convertido para radianos

seno = sin(radians(angulo))

cosseno = cos(radians(angulo))

tangente = tan(radians(angulo))

print('Seno em graus: {:.2f}'.format(seno))

print('Cosseno em graus: {:.2f}'.format(cosseno))

print('Tangente em graus: {:.2f}'.format(tangente))

