voluntarios_registrados = []

while True:
    
    entrada = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    
    if entrada.lower() != 'sair':
        voluntarios_registrados.append(entrada)
    else:
        break
    
    
print(f'Voluntários registrados: {voluntarios_registrados}')