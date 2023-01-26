class Pessoa:
    
    def __init__(self,nome:str,idade:int,cpf:str,sexo:str): #Construtor
        
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.sexo = sexo
    
        
        
    
    def setNome(self,n):
        self.nome = n
    
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade
    
    def setIdade(self,n):
        self.idade = n
    
    def setCPF(self,c):
        self.cpf = c
    
    def getCPF(self):
        return self.cpf
    
    def getSexo(self):
        return self.sexo
    
    def setSexo(self,s):
        self.sexo = s
    
    