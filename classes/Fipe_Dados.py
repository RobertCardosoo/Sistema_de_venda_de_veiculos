import json
import requests

 


class Fipe():
    
    def buscar_marca_carros(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas").json() 
        self.lista_marca_carros = []
        count = 0
        
        for i in request:
            self.lista_marca_carros.append(i[count]['nome'])
            count+=1

        return self.lista_marca_carros
    
    def buscar_marca_motos(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/motos/marcas").json() 
        self.lista_marca_motos = []
        count = 0
        
        for i in request:
            self.lista_marca_motos.append(i[count]['nome'])
            count+=1

        return self.lista_marca_motos
    
    def buscar_modelos_carros(self,codigo):
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo}/modelos").json()
        self.lista_modelos_carros = []
        for i in request['modelos']:
            self.lista_modelos_carros.append(i)   
        return self.lista_modelos_carros
    
    
    
    
    
   
    
     
        
    
    
    