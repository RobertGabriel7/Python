# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo):    
    # TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 

    if(consumo <= 10): 
        return "Plano Essencial Fibra - 50Mbps"
    elif(consumo <= 19):
        return "Plano Prata Fibra - 100Mbps"
    else: 
        return "Plano Premium Fibra - 300Mbps"

# TODO: Retorne o plano de internet adequado:
print(recomendar_plano(consumo))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado: