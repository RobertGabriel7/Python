salario = int(input('Qual o seu sálario? '))

if salario >= 1250:
    print('Você recebeu um aumento de "10%" sobre o seu salario. O seu salario antigo R${:.3f} e o atual R${:.3f}'.format(salario, salario + (salario * 10/100) ))
else: 
    print('Você recebeu um aumento de "15%" sobre o seu salario. O seu salario antigo R${:.3f} e o atual R${:.3f}'.format(salario, salario + (salario * 15/100) )) #Para fazer porcentagem: valor do salario - (salario * a porcentagem / 100)