from .item_do_cardapio import ItemCardapio

# POO: Herança em python

# Para indicar essa relação, utilizamos a sintaxe class NomeDaClasse(ClasseMae):, 
# onde o nome entre parênteses identifica a origem dos atributos.
# Agora a class Prato vai herdar métodos e atributos da class ItemCardapio

class Prato(ItemCardapio):
    
    def __init__(self, nome, preco, descricao):
        # Para utilizar os métodos e atributos de outra class, é usado o método super()
        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self):
        return self._nome 
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)