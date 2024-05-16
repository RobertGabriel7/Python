import re  # Importa o módulo 're' para operações com expressões regulares.

def validate_numero_telefone(phone_number):
    padrao = r"\(\d{2}\) 9\d{4}-\d{4}"  # Define o padrão de expressão regular para validar números de telefone no formato (XX) 9XXXX-XXXX.
    if re.match(padrao, phone_number):  # Verifica se o número de telefone corresponde ao padrão definido.
        return "Número de telefone válido."  # Retorna uma mensagem indicando que o número de telefone é válido.
    else:
        return "Número de telefone inválido."  # Retorna uma mensagem indicando que o número de telefone é inválido.

phone_number = input()  # Solicita ao usuário que insira um número de telefone.
result = validate_numero_telefone(phone_number)  # Chama a função 'validate_numero_telefone' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
print(result)  # Imprime o resultado indicando se o número de telefone é válido ou inválido.
