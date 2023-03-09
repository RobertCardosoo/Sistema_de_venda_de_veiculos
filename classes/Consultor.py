from classes.Pessoa import Pessoa
import random

class Consultor(Pessoa):
    
    def __init__(self,nome:str,idade:int,cpf:str,sexo:str,mat:int):
        super().__init__(nome,idade,cpf,sexo) #Herdando atributos e métodos da classe Pessoa
        
        self.matricula = mat
        
        
    def getMat(self):
        return self.matricula
    
        
        