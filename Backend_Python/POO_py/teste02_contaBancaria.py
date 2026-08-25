class ContaBancaria:
    def __init__ (self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._StatusConta = False

    def __str__(self):
        return f'\nTitulo: {self.titular} | Saldo da conta: R${self.saldo} | Conta ativa? {self._StatusConta}\n' 

    def ativar_conta(self):
        self._StatusConta = not self._StatusConta

contaMinha = ContaBancaria('Robert', '5000')

contaMinha.ativar_conta()

print(contaMinha._StatusConta)

print(contaMinha.titular)

class ClienteBanco: 
    def __init__(self, nome, idade, profissao, conta, saldo):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.conta = conta
        self.saldo = saldo

    @classmethod
    def apenas_idade(cls, idade):
        idade = idade
        return idade


pessoa1 = ClienteBanco('Robert', 23, 'estag', 'Conta Corrente', 5000)
pessoa2 = ClienteBanco('Maria', 30, 'advogada', 'Conta Poupança', 10000)
pessoa3 = ClienteBanco('João', 45, 'engenheiro', 'Conta Corrente', 2000)        

pessoa4 = ClienteBanco.apenas_idade(idade=25)

print(f'Idade da pessoa 4: {pessoa4}')