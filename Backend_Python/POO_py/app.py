from restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
#from modelos.cardapio.item_do_cardapio import ItemCardapio


#pontoPraMais = Restaurante('Carro chefe', 'Classic')

bebida_suco = Bebida('Suco de Manga', 10.00, 'grande')
prato_italiano = Prato('Pizaa Marguerita', 35.00, 'Pizza com queijo, tomate e oregano')

'''
pontoPraMais.receber_avaliacao('Robert', 10)
pontoPraMais.receber_avaliacao('Valentina', 5)
pontoPraMais.receber_avaliacao('Alice', 10)
pontoPraMais.listar_restaurantes()
'''

def main():
    print(bebida_suco)
    print(prato_italiano)
if __name__ == '__main__':
        main()


