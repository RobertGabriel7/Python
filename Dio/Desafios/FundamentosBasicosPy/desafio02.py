# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

itens = []
item = ""
# TODO: Crie um loop para solicita os itens ao usuário:
for n in range(1, 4):
    equi = input(f"Equipamento {n}: ")
    itens.append(equi)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")