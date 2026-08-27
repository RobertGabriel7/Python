class Livro:

    livros = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = False
        Livro.livros.append(self)

    def __str__(self):
        return f'\nTitulo: {self._titulo.ljust(7)} | Autor: {self._autor.ljust(7)} | Ano de publicacao: {str(self._ano_publicado).ljust(7)} | Livro disponivel? {self._disponivel}'

    def emprestar(self):
        self._disponivel = not self._disponivel     

    @staticmethod
    def verificar_disponibilidade(ano):
        resultado = []

    def mostrar_livros(self):
        for livro in self.livros:
            print(livro._ano_publicado)

first_instance = Livro('Olha Gol', 'Nobody', 2026)
two_instance = Livro('Outros', 'Jeff Jobs', 2017)
tree_instance = Livro('Oloco', 'Não lembro', 2026)

#two_instance.mostrar_livros()
#print(Livro.livros[0]._ano_publicado)
two_instance.verificar_disponibilidade(2026)