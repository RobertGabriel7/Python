# Desafio: Sacar, depositar e visualizar o histórico

import string


saldo = 100
limiteDeSaques = 1
desejaContinuar = 'y'

# Sacar valores
def sacar(valorDoSaque):

    if (limiteDeSaques > 3):
        return print("Voce somente pode fazer 3 saques por dia!")

    else:
        global saldo 
        saldo -= valorDoSaque        
        return print(f"Saldo atual: R${saldo}")

# Depositar valores
def depositar(deposito):
    global saldo
    saldo += deposito
    return print(f"Saldo atual: R${saldo}")

# Consulta de valores
def extrato():
    print(f"Voce tem R${saldo}.")
while (desejaContinuar == 'y'):
    print("\n ------------- Bem-vindo(a) ao Seven ------------- \n")
    print("\nQual das opcoes a seguir vc deseja fazer: \n\n[1].Sacar \n\n[2].Depositar \n\n[3].Consulta de Saldo \n\n[4].Sair\n")
    
    opcao = int(input("Digite apenas uma opcao: "))
    print(limiteDeSaques)
    
    if (opcao == 1):
        
        valorDoSaque = int(input(f"Quanto voce desejar sacar de R${saldo} ? R$"))
        if (valorDoSaque > saldo):
            print(f"\nO valor diigitado foi superior ao valor disponivel!\n")
            desejaContinuar = str(input("Deseja continuar: (y/n)"))
        else:
            sacar(valorDoSaque)
            limiteDeSaques += 1
            desejaContinuar = str(input("Deseja continuar: (y/n)"))

    elif (opcao == 2):
        deposito = int(input("\nQuando voce deseja depositar? R$"))
        depositar(deposito)
        desejaContinuar = str(input("Deseja continuar: (y/n)"))
    elif(opcao == 3):
        extrato()
        desejaContinuar = str(input("Deseja continuar: (y/n)"))
    else:
        print("Opcao invalida")
        desejaContinuar = str(input("Deseja continuar: (y/n)"))