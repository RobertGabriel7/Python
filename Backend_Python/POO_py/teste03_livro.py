# Importa o módulo sys para interagir com recursos do sistema/interpretador Python
import sys
# Configura o terminal para exibir caracteres UTF-8 (acentos, ç, etc.) sem erros de codificação
sys.stdout.reconfigure(encoding="utf-8")

# Define a classe Livro, servindo de modelo/molde para a criação de objetos do tipo livro
class Livro:
    
    # Atributo de classe: lista compartilhada por todas as instâncias para guardar todos os livros criados
    livros = []
    
    # Método construtor: executado automaticamente ao instanciar um novo livro para definir seus valores iniciais
    def __init__(self, titulo, autor, ano_publicacao):
        
        # Atributo de instância: armazena o título específico do livro
        self.titulo = titulo
        # Atributo de instância: armazena o autor específico do livro
        self.autor = autor
        # Atributo de instância: armazena o ano em que o livro foi publicado
        self.ano_publicacao = ano_publicacao
        # Atributo de instância: define que todo livro recém-cadastrado nasce como disponível (True) por padrão
        self.disponivel = True
        # Adiciona o próprio objeto recém-criado (self) na lista geral da classe (Livro.livros)
        Livro.livros.append(self)
    
    # Método especial __str__: converte o objeto em texto formatado ao utilizar a função print()
    def __str__(self):
        return f'\nTitulo: "{self.titulo}" | Autor: "{self.autor}" | Ano de publicação: "{self.ano_publicacao}" | Disponivel: "{self.disponivel}"'
    
    # Método de instância: inverte o status de disponibilidade do livro (se está True vira False, e vice-versa)
    def emprestar(self):
        self.disponivel = not self.disponivel
    
    # Decorador que indica um método estático (não precisa de acesso direto às instâncias via 'self' nem à classe via 'cls')
    #Método estático 
    @staticmethod
    def verificar_disponibilidade(ano):
        # Cria uma lista temporária para guardar apenas os livros que cumprirem os requisitos do filtro
        disponiveis = []
        # Percorre cada livro cadastrado na lista geral da classe
        for book in Livro.livros:
            # Checa se o ano do livro bate com o procurado E se o livro está disponível (disponivel == True)
            if ano == book.ano_publicacao and book.disponivel:
                # Insere o livro aprovado no filtro dentro da lista temporária
                disponiveis.append(book)            
        # Devolve a lista preenchida (ou vazia) para o código que chamou a função
        return disponiveis

# Instancia o primeiro objeto da classe Livro e o adiciona automaticamente na lista 'livros'
mybook = Livro('Eita gloria', 'Robert', 2026)
# Instancia o segundo objeto da classe Livro
otherbook1 = Livro('O chamado', 'Robert', 2026)
# Instancia o terceiro objeto da classe Livro
otherbook2 = Livro('Odisseia', 'Homero', 700)

#mybook.emprestar()

#print(mybook)

# Define uma variável com o valor do ano a ser pesquisado para facilitar o reuso na busca e na mensagem
ano_buscado = 700

# Executa o método estático enviando o ano pesquisado e armazena a lista retornada dentro da variável 'livros_2026'
livros_2026 = Livro.verificar_disponibilidade(ano_buscado)

# Verifica se a quantidade de elementos na lista retornada é igual a zero (nenhum livro encontrado)
if len(livros_2026) == 0:
    # Caso a lista esteja vazia, exibe uma mensagem informando que não há livros para aquele ano
    print(f'\nNão há livros no ano {ano_buscado}.')    
# Caso a lista contenha um ou mais livros encontrados
else:
    # Loop que percorre cada livro da lista de resultados obtidos
    for livross in livros_2026:
        # Imprime cada livro (acionando automaticamente o método __str__ de cada objeto)
        print(livross)