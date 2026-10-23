# Objetivo do exercicio:

# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

# Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

# Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.

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