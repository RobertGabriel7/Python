print('Graças a Deus, consegui!')

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        # Atributos de instancia: cada restaurante tera seus proprios valores
        self._nome = nome.title()  # Converte o nome para formato de título (primeira letra maiúscula)
        self._categoria = categoria.upper()  # Converte a categoria para maiúsculas
        # Comeca como inativo por padrao
        self._ativo = False
        # Adiciona o objeto atual (self) na lista compartilhada da classe
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        # Define como o objeto aparece quando usamos print(objeto) ou str(objeto)
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Status".ljust(20)}')
        # Percorre todos os restaurantes cadastrados na lista da classe
        for restaurante in Restaurante.restaurantes:
            # Mostra os dados principais de cada restaurante
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante._ativo).ljust(20)}')

    @property
    def ativo(self):
        # Retorna o valor do atributo privado _ativo
        return "Verdadeiro" if self._ativo else "Falso"

    def alterar_status(self):
        # Alterna o status do restaurante entre ativo e inativo
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alterar_status()  # Ativa o restaurante 'Praça'
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()