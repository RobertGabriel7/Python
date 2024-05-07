print('Conversão de graus Celsius (C°) para graus Fahrenheit (F°)!')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

valor = float(input('Digite um valor em graus Celsius (C°): '))

conv = 32 + (valor*9/5)

print('\n A temperatura de {} graus C° (Clesius), corresponde a {} graus F° (Fahrenheit). \n'.format(valor,conv))