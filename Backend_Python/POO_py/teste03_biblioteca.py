from teste03_livro import Livro

# Importação (from teste03_livro import Livro):
# When Python executa o arquivo biblioteca.py e encontra o import, 
# ele lê e executa todo o arquivo teste03_livro.py do início ao fim.

otherbook = Livro("1984", "George Orwell", 1949)

#otherbook.emprestar()

Livro.verificar_disponibilidade(1949)