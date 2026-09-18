import sys
sys.stdout.reconfigure(encoding="utf-8")

class Livro:
    
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    def __str__(self):
        return f'\nTitulo: "{self.titulo}" | Autor: "{self.autor}" | Ano de publicação: "{self.ano_publicacao}" | Disponivel: "{self.disponivel}"'
    
    def emprestar(self):
        self.disponivel = not self.disponivel
    
    #Método estático 
    @staticmethod
    def verificar_disponibilidade(ano):
        disponiveis = []
        for book in Livro.livros:
            if ano == book.ano_publicacao and book.disponivel:
                disponiveis.append(book)            
        if len(disponiveis) != 0:
            for livroA in disponiveis:
                print(livroA)
        else:
            print(f'\nNão há livros no ano de {ano}.')    
    

mybook = Livro('Eita gloria', 'Robert', 2026)
otherbook1 = Livro('O chamado', 'Robert', 2026)
otherbook2 = Livro('Odisseia', 'Homero', 700)
'''
mybook.emprestar()
#print(mybook)

mybook.verificar_disponibilidade(2026)
'''