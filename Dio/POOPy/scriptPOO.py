class Bike:
    
    andando = False
    # Metodo construtor
    def __init__(self, cor, modelo, ano, valor, andando):
        # Self é a referência explicita dos elementos: self.valor
        # No php é utilizado a referência implicita: this.valor
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.andando = andando
    # Metodos
    # Metodos, por conveção, precisa de um argumento, e é colocado o "self"
    def buzinar(self):
        print("Biiiiiii")
        
    def parar(self):
        if(self.andando):
            print("Parando...")
        else:
            print("Bike parada.")    
    
    def correr(self):
         if (self.andando):
             print("Bike correndo...")
        else:
            print("")
    
caloi = Bike("Black", "caloi pro", "2024", "999")
caloi.buzinar()