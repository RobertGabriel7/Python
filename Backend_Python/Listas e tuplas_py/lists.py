"""
Operações Comuns (aplicáveis a Listas e Tuplas):

Acesso por índice: Permite acessar um elemento específico da coleção usando sua posição numérica (índice), que começa em 0.
Exemplo: minha_colecao[1]

Slicing: Utilizado para extrair uma parte (sub-coleção) de uma lista ou tupla, especificando um intervalo de índices. O índice final do intervalo não é incluído.
Exemplo: minha_colecao[0:2]

Operador in: Verifica se um determinado elemento está presente na coleção, retornando True se sim e False se não.
Exemplo: 20 in minha_colecao

Métodos / Funções para Leitura e Tratamento de Strings:

input(): Função interna usada para ler/receber dados digitados pelo usuário no terminal (retorna uma string).
Exemplo: texto = input("Digite algo: ")

.split(): Método de string que divide um texto em uma lista de pedaços, usando um separador especificado (como vírgula ou espaço).
Exemplo: lista_palavras = "a, b, c".split(",")

.strip(): Método de string que remove espaços em branco extras (e quebras de linha) do início e do fim de um texto.
Exemplo: item_limpo = "  Arroz  ".strip()

tuple(): Construtor / Função que converte um objeto iterável (como uma lista ou string) em uma tupla.
Exemplo: minha_tupla = tuple([1, 2, 3])

Métodos Específicos para Listas (devido à sua mutabilidade):

.append(): Adiciona um novo elemento ao final da lista.
Exemplo: lista.append(4)

.insert(): Insere um elemento em uma posição específica da lista.
Exemplo: lista.insert(1, 5)

.remove(): Remove a primeira ocorrência do valor especificado na lista.
Exemplo: lista.remove(2)

.sort(): Ordena os elementos da lista em ordem crescente.
Exemplo: lista.sort()

.reverse(): Inverte a ordem dos elementos da lista.
Exemplo: lista.reverse()

.pop(): Remove um elemento da lista em uma posição específica (pelo índice) e retorna o elemento removido.
Exemplo: lista.pop(1)

Além desses, também foi mencionada a concatenação de tuplas (usando o operador +) para criar uma nova tupla a partir de tuplas existentes, e a iteração sobre elementos (com for loops) e o desempacotamento (atribuir elementos a variáveis) como formas de trabalhar com ambas as coleções.
"""

# As listas são coleções de elementos mutáveis (pode ser alterada depois de declarar)

lista = [0,1,3]

lista = [1, "texto", 3.14, False, [1,2,3]]

# As tuplas são coleções de elementos imutáveis (não pode ser alterado depois de declarar)

tupla = (1,2,3)

tupla_mista = (1, "texto", 3.14, False, [1,2,3])