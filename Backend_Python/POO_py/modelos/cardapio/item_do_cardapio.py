from abc import ABC, abstractclassmethod
class ItemCardapio(ABC):
    
    def __init__(self, nome, preco):
        
        self._nome = nome
        self._preco = preco
        
    def __str__(self):
        
        return self._nome
    
    @classmethod
    def aplicar_desconto():
        pass