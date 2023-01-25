import tkinter as tk
from classes.Pessoa import Pessoa
from classes.Carro import Carro

select = 1
count = 0
pessoas = []


while select == 1:
    
    if(select == 1):
        aux = Pessoa(input("Nome:"),int(input("Idade:")),float(input("Altura:")))
        pessoas.append(aux)
            
        print("-----------------------------------------------")
        print("Nome: "+pessoas[int(count)].getNome())
        print("Idade: "+str(pessoas[int(count)].getIdade()))
        print("Altura: "+str(pessoas[int(count)].getAltura()))
        select = int(input("Deseja continuar sim[1] não[0]"))
        count=+1
        
    if(select == 0):
        print("Finalizando")
        print("Total de  pessoas criadas = "+str(len(pessoas)))
        
c = 0

while c < len(pessoas):
    print("-----------------------------------------------")
    print("Nome: "+pessoas[int(c)].getNome())
    print("Idade: "+str(pessoas[int(c)].getIdade()))
    print("Altura: "+str(pessoas[int(c)].getAltura()))
    c+=1

print("teste")

