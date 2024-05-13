"""

clear(): Remove todos os elementos do dicionário.
copy(): Retorna uma cópia rasa (shallow copy) do dicionário.
fromkeys(iterable, value=None): Retorna um novo dicionário com chaves do iterable e valores definidos para o valor especificado.
get(key, default=None): Retorna o valor associado à chave especificada, ou o valor padrão se a chave não existir.
items(): Retorna uma visualização de todos os pares chave-valor do dicionário.
keys(): Retorna uma visualização de todas as chaves do dicionário.
pop(key, default=None): Remove e retorna o valor associado à chave especificada, ou o valor padrão se a chave não existir.
popitem(): Remove e retorna um par chave-valor arbitrário do dicionário.
setdefault(key, default=None): Retorna o valor associado à chave especificada. Se a chave não existir, insere a chave com o valor padrão especificado.
update(iterable): Atualiza o dicionário com os pares chave-valor do iterable fornecido.
values(): Retorna uma visualização de todos os valores do dicionário.

"""
# Métodos importantes do dicionário em Python

# Método clear()
# Remove todos os elementos do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
dicionario.clear()
print("Após clear():", dicionario)

# Método copy()
# Retorna uma cópia rasa (shallow copy) do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
copia = dicionario.copy()
print("Cópia:", copia)

# Método fromkeys(iterable, value=None)
# Retorna um novo dicionário com chaves do iterable e valores definidos para o valor especificado.
# Serve para criar novas chaves: dict.fromkeys()
# Para criar chaves com valores padrões: dict.fromkeys(["nome", "telefone", "vazio"])

chaves = ["a", "b", "c"]
valor_padrao = 0
novo_dicionario = dict.fromkeys(chaves, valor_padrao)
print("Novo dicionário:", novo_dicionario)

# Método get(key, default=None)
# Retorna o valor associado à chave especificada, ou o valor padrão se a chave não existir.

dicionario = {"a": 1, "b": 2, "c": 3}

# o segundo argumento "0", é passado para retornar como valor padrão caso não tenha valor associado a chave especificada.

valor = dicionario.get("b", 0)
print("Valor de 'b':", valor)

# Método items()
# Retorna uma visualização de todos os pares chave-valor do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
pares = dicionario.items()
print("Pares chave-valor:", pares)

# Método keys()
# Retorna uma visualização de todas as chaves do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = dicionario.keys()
print("Chaves:", chaves)

# Método pop(key, default=None)
# Remove e retorna o valor associado à chave especificada, ou o valor padrão se a chave não existir.

dicionario = {"a": 1, "b": 2, "c": 3}
valor = dicionario.pop("b", 0)
print("Valor removido de 'b':", valor)

# Método popitem()
# Remove e retorna um par chave-valor arbitrário do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
par = dicionario.popitem()
print("Par chave-valor removido:", par)

# Método setdefault(key, default=None)
# Retorna o valor associado à chave especificada. Se a chave não existir, insere a chave com o valor padrão especificado.

dicionario = {"a": 1, "b": 2, "c": 3}
valor = dicionario.setdefault("d", 0)
print("Valor de 'd' após setdefault:", valor)

# Método update(iterable)
# Atualiza o dicionário com os pares chave-valor do iterable fornecido.

dicionario = {"a": 1, "b": 2}
dicionario.update({"b": 3, "c": 4})
print("Após update:", dicionario)

# Método values()
# Retorna uma visualização de todos os valores do dicionário.

dicionario = {"a": 1, "b": 2, "c": 3}
valores = dicionario.values()
print("Valores:", valores)
