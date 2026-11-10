from abc import ABC, abstractclassmethod

class Veiculo:
    
    def __init__(self, marca, modelo):
        
        self._marca = marca
        self._modelo = modelo
        self._ligar = False
    
    @classmethod
    def ligar(self):
        pass