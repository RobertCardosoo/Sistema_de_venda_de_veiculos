class Carro:
    
    def __init__(self,nome:str,marca:str,ano:int,cor:str,classificacao:str,situacao:str,valor:float,placa:str):
        
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.classificacao = classificacao
        self.situacao = situacao
        self.valor = valor
        self.placa = placa
        
    #-----Métodos----
    
    def getNome(self):
        return self.nome
    
    def setNome(self,n):
        self.nome = n
        
    def getMarca(self):
        return self.marca
    
    def setMarca(self,m):
        self.marca=m
    
    def getAno(self):
        return self.ano
    
    def setAno(self,a):
        self.ano=a
    
    def getCor(self):
        return self.cor
    
    def setCor(self,c):
        self.cor = c
        
    def getClassificacao(self):
        return self.classificacao
    
    def setClassificacao(self,clas):
        self.classificacao = clas
    
    def getSituacao(self):
        return self.situacao
    
    def manutenciar(self):
        self.situacao = "Precisa de Manutenção"
        
    def vistoriar(self):
        self.situacao = "Vistoriado"
    
    def getValor(self):
        self.valor
        
    def setValor(self,v):
        self.valor = v
        
    def getPlaca(self):
        return self.placa
    
    def setPlaca(self,p):
        self.placa = p