class Pessoa:

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property

    def saudacao(self):

        if self.profissao == 'estag': 
            return f'Fala {self.nome}, baita Estag, seja bem-vindo!'
        else:
            return f'Fala {self.nome}, seja bem-vindo!'

new_pessoa = Pessoa('Robert', 23, 'estag')
new_pessoa.aniversario()
print(new_pessoa)  # Exibe as informações da pessoa usando o método __str__