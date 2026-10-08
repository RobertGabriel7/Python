lista_atualizada = ['Ana', 'Carlos', 'Pedro']

try:
    
    nomeIncorreto = input('Digite o nome incorreto: ').strip().capitalize()

    nomeCorreto = input('\nDigite o nome correto: ').strip().capitalize()

    lista_atualizada[lista_atualizada.index(nomeIncorreto)] = nomeCorreto
    
    print(f'\nO nome "{nomeIncorreto}" foi substituido por "{nomeCorreto}".')
    
    print('\nlista atualizada:', lista_atualizada)

except ValueError:
    
    print(f'Deu algum erro. Você tem certeza que o nome "{nomeIncorreto}" está lista? Verfique!')
    print(f'lista atualizada: {lista_atualizada}\n')
        