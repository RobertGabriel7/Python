sala = float(input('Quanto o colaborador(a) recebe: R$'))

resul = sala + (sala*15/100)

print('\n O colaborador recebe R${:.2f} de salário e com o aumento de 15%, o salário passou para R${:.2f}. \n'.format(sala,resul))