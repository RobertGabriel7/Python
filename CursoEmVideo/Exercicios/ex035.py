reta1 = float(input('Digite o comprimento da primeiro reta (A - B): '))
reta2 = float(input('Digite o comprimento da segunda reta (B - C): '))
reta3  = float(input('Digite o comprimento da terceira reta (C - A): '))
""" o valor de reta1 não pode ser maior que a soma de reta2 e reta3 """
""" Se reta1 = 15 , reta2 + reta3 precisa ser = 16 (no minino) """
if reta1 <= reta2 + reta3 and reta2 <= reta1 + reta3 and reta3 <= reta1 + reta2:
    print('Valor A - B {}, Valor B - C {}, Valor C - A {}, com base nesses valores é possivel fazer um triângulo!'.format(reta1, reta2, reta3 ))
else:
    print('Com base nos valores digitados, não é possivel fazer um triângulo.')