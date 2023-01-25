import tkinter as tk
from classes.Pessoa import Pessoa
from classes.Carro import Carro

select = 1
pessoas = []
while select != 0:
    select = int(input("Deseja continuar sim[0] não[1]"))
    
    if(select == 1):
        aux = Pessoa(input("Nome:"),int(input("Idade:")),float(input("Altura:")))
        pessoas.append(aux)
            
