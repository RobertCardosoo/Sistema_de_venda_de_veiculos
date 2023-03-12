import json
import requests

 


class Fipe():
    
    def buscar_marca_carros(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas").json() 
        self.lista_marca_carros = []
        count = 0
        
        for i in request:
            self.lista_marca_carros.append(request[count]['nome'])
            count+=1

        return self.lista_marca_carros
    
    def buscar_marca_motos(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/motos/marcas").json() 
        self.lista_marca_motos = []
        count = 0
        
        for i in request:
            self.lista_marca_motos.append(request[count]['nome'])
            count+=1

        return self.lista_marca_motos
    
    def buscar_modelos_carros(self,codigo_marca):
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos").json()
        self.lista_modelos_carros = []
        for i in request['modelos']:
            self.lista_modelos_carros.append(i)   
        return self.lista_modelos_carros
    
    def buscar_anos_modelo_carros(self,codigo_marca,codigo_modelo):
        
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos").json()
        
        self.lista_anos_modelo = []
        for i in request:
            self.lista_anos_modelo.append(i)   
        return self.lista_anos_modelo
    
    def buscar_veículo(self,tipo_veiculo,codigo_marca,codigo_modelo,codigo_ano_combustivel):
        
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano_combustivel}").json()
        
        return request
    


   
    
     
        
    
    
    