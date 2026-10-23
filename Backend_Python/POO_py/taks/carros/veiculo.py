class Veiculo:
    
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._protegido_ligado = False
    
    def __str__(self):
        return f'\nMarca: {self._marca} | Modelo: {self._modelo} | Estado (Ligado/Desligado): {self._protegido_ligado}'
    