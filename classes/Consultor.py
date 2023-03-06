from classes.Pessoa import Pessoa
import random

class Consultor(Pessoa):
    
    def __init__(self,nome:str,idade:int,cpf:str,sexo:str):
        super().__init__(nome,idade,cpf,sexo) #Herdando atributos e métodos da classe Pessoa
        
        self.matricula = 0
        
        
    def generateMat(self):
        gen = [random.randint(0,9),random.randint(0,9),random.randint(0,9)]
        self.matricula = (f'{gen[0]}{gen[1]}{gen[2]}')
    
    def getMat(self):
        return self.matricula
    
        
        