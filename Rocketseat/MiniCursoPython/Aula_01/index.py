from flask import Flask

app = Flask(__name__)

""" Para definir uma rota raiz da pagina inicial e a function que será executada quando requisitada """
@app.route('/') 

def  helloWorld ():
    """ se usa o def (de definição) para criar uma function """
    return 'Hello World'

""" Para API fique disponivel para aplicações, precisa fazer isso: """
""" debug=True serve para ativar o modo depuração para ter mais informações do servidor """
""" Esse modo é somente para o desenvolvimento """

""" Para saber se executado diretamente ou se está sendo importado por outro arquivo, e para não criar um servidor novo a cada importação, é utilizada essa condição """
if __name__ == "__main__":
    app.run(debug=True) 
    
    
""" Apos ser ativado o servidor, ele fica esperando uma requisão de algum rota para executar a condição que está aqui no código. """

""" O servido quando solicitado, procura a rota que foi passada e verifica se existe, se não tiver, erro 404 """