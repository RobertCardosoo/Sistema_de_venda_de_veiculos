class Pessoa:
    
    def __init__(self,nome:str,idade:int,altura:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        
    
    def setNome(self,n):
        self.nome = n
    
    def getNome(self):
        return self.nome

