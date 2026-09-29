itens_em_casa = ["Arroz", "Feijão", "Batata", "Açúcar", "Chocolate"]

item_para_verificar = input("Digite o item que você quer verificar: ")

itens_pra_comprar = []

if item_para_verificar in itens_em_casa:    
    print(f'Você já tem "{item_para_verificar}" em casa.')
else:
    print(f'Você não tem "{item_para_verificar}". Precisa comprar.')

print(itens_em_casa)

