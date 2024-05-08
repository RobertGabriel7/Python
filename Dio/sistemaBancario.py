""" 
Módulo 'os' do python serve para modifcar algumas coisas do sistema qual o python está inserido.
O os permite que você execute comandos do sistema, manipule caminhos de arquivos, manipule variáveis de ambiente e muito mais 

"""
import os

desejaContinuar = 'y'
saldo = 100.45
limiteDeSaque = 3
opcao = 0
saquesRealizados = 0


""" Function para limpar o terminal """
def limpar_terminal():
    # Verifica o sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    
limpar_terminal()

while (desejaContinuar == 'y'):
    
    print(saquesRealizados)
    """ Criar um sistema bancario com as operações: sacar, depositar e visualizar o saldo """

    print("\n ------------- Bem-vindo(a) ao Seven ------------- \n")
    print("\nQual das opcoes a seguir vc deseja fazer: \n\n[1].Sacar \n\n[2].Depositar \n\n[3].Consulta de Saldo \n\n[4].Sair\n"
          
          
    )
    
    opcao = int(input("digite apenas um numero: "))
    
    
    if (opcao == 1):
        limpar_terminal()    
        if(saldo == 0):    
        
            print("Sem saldo para retirar.")
            desejaContinuar = str(input("Deseja continuar: (y/n)"))
            limpar_terminal()
            
        else:        
        
            saque = float(input("Quanto voce quer sacar? "))
            saldo -= saque
            
            if(saldo <= 0):
                limpar_terminal()
                print("\nO valor digitado para saque foi maior do que o valor disponivel.\n") 
                desejaContinuar = str(input("Deseja continuar: (y/n)"))
                limpar_terminal()
            
            else:
                
                if(saquesRealizados == limiteDeSaque):
                    limpar_terminal()
                    print("Não pode sacar mais dinheiro, pois o limite diario é de 3 saques por dia.\n")
                    desejaContinuar = str(input("Deseja continuar: (y/n)"))
                    limpar_terminal()
                else:        
                    limpar_terminal()
                    print(f"Saldo atual: R${saldo}")
                    saquesRealizados += 1
                    desejaContinuar = str(input("Deseja continuar: (y/n)"))
                    limpar_terminal()
            
    elif (opcao == 2):
        
        deposito =float(input("Quanto voce deseja depositar: "))
        saldo += deposito
        print(f"Saldo atual: R${saldo}")
        desejaContinuar = str(input("Deseja continuar: (y/n)"))
        limpar_terminal()
    
    elif (opcao == 3):
        limpar_terminal()        
        print(f"Saldo atual: R${saldo}")
        desejaContinuar = str(input("Deseja continuar: (y/n)"))
        limpar_terminal()    
        
    elif (opcao == 4):
        
        print("Saindo...") 
        desejaContinuar = 'n'
        
    else:
        limpar_terminal()
        print("Saindo...") 
        
        
        

""" Graças a Deus consegui. """    

    