# Lista original com os eventos na ordem incorreta (invertida)
eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']

# Cria uma nova lista pré-preenchida com None do mesmo tamanho da lista original
# Isso reserva os espaços necessários na memória para permitir atribuição direta por índice
nwEventos_registrados = [None] * len(eventos_registrados)

# Loop principal para controlar a interação com o usuário
while True:
    
    # Pergunta ao usuário se deseja ajustar a lista
    # .strip() remove espaços extras nas pontas e .lower() padroniza a resposta para minúscula
    user = input('\nDeseja ajustar a ordem da lista? [s/n]\n').strip().lower()
    
    # Exibe a lista original como referência
    print(eventos_registrados)
    #print(nwEventos_registrados)
    
    # Se o usuário aceitar ajustar a ordem
    if user == 's':
        
        # Percorre cada evento da lista original
        for item in eventos_registrados:
             
            # Solicita a posição desejada (considerando a contagem humana que começa em 1)
            position = int(input(f'Digite o número da posição do item "{item}": '))
            
            # Ajusta para o índice do Python (que começa em 0)
            position = position - 1
            
            # Atribui diretamente o evento na posição escolhida da nova lista
            nwEventos_registrados[position] = item
            
        # Força o 'user' a virar 'n' para que na próxima volta do while o código caia no 'else' e encerre
        user = 'n'
    else:
        # Exibe o cabeçalho do resultado final
        print('Ordem corrigida do Evento:')
        
        # Percorre a nova lista gerando índices a partir do 1 (para exibição amigável ao usuário)
        for indice, item in enumerate(nwEventos_registrados, start=1):
            print(f'{indice}° - {item}')
        
        # Encerra o loop while
        break