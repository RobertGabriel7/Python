""" 
Dicionários em Python é uma estrutura de dados que consite em ter uma chave e valor, sendo ou não ordenados. O valor está associado a uma chave, e quando precisar obter o valor, é preciso chamar a chave desse valor.

O dicionário é nativo do Python.

A chave no dicionário não pode ser mudada, mas somente o valor.

O dictionary não permite que repita as chaves. 

"""

""" Criando um dicionário """

myDictionary = {"nome1": "Gabriel", "idade": 21, "cidade": "São Paulo"}

""" Atribuindo chave-valor """
# myDictionary = {}
myDictionary["nome2"] = "Robert"
myDictionary["idade2"] = "21"
myDictionary["cidade2"] = "São Paulo"

print(myDictionary["nome1"])

""" Para adicionar chave-valor em um dictionary """
myDictionary = dict(instrument="Drum", color = "Blue")

print(myDictionary)

""" Dicionários aninhados: dicionario dentro de outro dicionario que está dentro de outro dicionario... """

baseDeDadosCadastrais = {
    
    "robertgg2728@gmail.com": {"nome": "Robert", "idade": 21, "e-mail": "robertgg2728@gmail.com" },
    
    "robert629jb@gmail.com": {"nome": "Gabriel", "idade": 21, "e-mail": "robert629jb@gmail.com"}   
    
}

# Mostrando o dicionário 
print(baseDeDadosCadastrais["robert629jb@gmail.com"]["e-mail"])


print(type(baseDeDadosCadastrais))
print("------------------ Percorrendo dictionary ------------------")

""" Para percorrer as chaves e valores de um dictionary """

""" .items() retorna uma tupla com chave e valor de um dictionary """
for chave, valor in baseDeDadosCadastrais.items():
    print(f"chave: {chave}, valor: {valor}")