# 1. Leitura e processamento do Estoque 1 em uma única linha
#
# Como funciona a expressão interna (List Comprehension):
# a) input(...): Lê a frase digitada (ex: "Arroz, Feijão, Macarrão") -> String
# b) .split(","): Divide a string nas vírgulas -> Lista: ['Arroz', ' Feijão', ' Macarrão']
# c) (p.strip() for p in ...): O laço 'for' percorre cada item 'p' da lista individualmente,
#    aplicando o método de STRING .strip() em cada um para remover os espaços das pontas.
# d) tuple(...): Converte o resultado final (limpo) de volta para uma Tupla.
produtos_do_estoque_1 = tuple(
    p.strip() for p in input("Produtos do estoque 1 (separados por vírgula): ").split(",")
)

# 2. Mesmo processo aplicado para o Estoque 2
produtos_do_estoque_2 = tuple(
    p.strip() for p in input("Produtos do estoque 2 (separados por vírgula): ").split(",")
)

# 3. Relatório unificado: concatena as duas tuplas usando o operador '+'
# O resultado é uma nova tupla contendo todos os produtos juntos.
print("\nEstoque combinado:")
print(produtos_do_estoque_1 + produtos_do_estoque_2)