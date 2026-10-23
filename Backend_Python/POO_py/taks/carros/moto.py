from veiculo import Veiculo

class Moto(Veiculo):
    
    def __init__(self, marca, modelo, tipo_ao_construtor):
        super().__init__(marca, modelo)
        self._tipo_ao_construtor = tipo_ao_construtor # indicando se a moto é Esportiva ou Casual
    
    def __str__(self):
        return f'{super().__str__()} | Tipo: {self._tipo_ao_construtor}'