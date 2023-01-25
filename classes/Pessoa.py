class Pessoa:
    
    def __init__(self,nome:str,idade:int,altura:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    
    def setNome(self,n):
        self.nome = n
    
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def setIdade(self,n):
        self.idade = n
    
    def setAltura(self,a):
        self.altura = a
    
    def getAltura(self):
        return self.altura
    
    