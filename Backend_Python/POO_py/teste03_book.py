class Livro:

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = False

    def __str__(self):
        return f'\nTitulo: {self._titulo.ljust(10)} | Autor: {self._autor.ljust(10)} | Ano de publicacao: {str(self._ano_publicado).ljust(10)}'

    def emprestar(self):
        if (self._disponivel == False):
            self._disponivel = True
        else:
            self._disponivel = False     


first_instance = Livro('Olha Gol', 'Nobody', 2026)
print(first_instance)
two_instance = Livro('Outros', 'Jeff Jobs', 2017)
print(two_instance.emprestar())

