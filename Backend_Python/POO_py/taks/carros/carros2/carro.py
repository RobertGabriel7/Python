from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, cor):
        
        super().__init__(marca, modelo)
        
        self._cor = cor
        
    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Cor: {self._cor}'
    
    