'''
Reorganizando uma lista de convidados

Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?

'''
lista_atual_de_convidados = ['Ana', 'Pedro', 'Carlos']

nome_da_pessoa = input('Digite o nome do novo convidado: ')
posicao_do_nome = input('Digite a posição na qual deseja inserir o convidado: ')

lista_atual_de_convidados.insert(int(posicao_do_nome) - 1, nome_da_pessoa)

print(lista_atual_de_convidados)  