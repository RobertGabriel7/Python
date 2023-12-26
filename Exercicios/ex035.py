reta1 = int(input('Digite o comprimento da primeiro reta (A - B): '))
reta2 = int(input('Digite o comprimento da segunda reta (B - C): '))
reta3  = int(input('Digite o comprimento da terceira reta (C - A): '))

if reta1 >= 10 and reta2 >= 12 and reta3 >= 10:
    print('Valor A - B {}, Valor B - C {}, Valor C - A {}, com base nesses valores é possivel fazer um triângulo!'.format(reta1, reta2, reta3 ))
else:
    print('Com base nos valores digitados, não é possivel fazer um triângulo.')