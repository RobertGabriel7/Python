# Desafio: Sacar, depositar e visualizar o histórico

saldo = 100
limiteDeSaques = 0
desejaContinuar = 'y'

# Function para sacar valores
def sacar(valorDoSaque):

    if (limiteDeSaques > 3):
        print("Voce somente pode fazer 3 saques por dia!")

    else:
        resultado = saldo - valorDoSaque        
        return print(f"Saldo atual: R${resultado}")
limiteDeSaques += 1


# Depositar valores
def depositar(deposito):
    resultado = saldo + deposito
    return (resultado)

while (desejaContinuar == 'y'):

    opcao = int(input("Digite uma opcao: "))
    
    if (opcao == 1):
        
        valorDoSaque = int(input(f"Quanto voce desejar sacar de R${saldo} ? R$"))
        if (valorDoSaque > saldo):
            print(f"O valor diigitado foi superior ao valor disponivel!")
            desejaContinuar = str(input("Deseja continuar: (y/n)"))
        else:
            sacar(valorDoSaque)
            desejaContinuar = str(input("Deseja continuar: (y/n)"))

    elif (opcao == 2):
        deposito = int(input("Quando voce deseja depositar? R$"))
        depositar(deposito)
        desejaContinuar = str(input("Deseja continuar: (y/n)"))
    
    
