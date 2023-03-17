import json
import requests

 


class Fipe():
    
    #Consulta sobre Carros
    
    def buscar_marca_carros(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas").json() 
        
        return request
    
    def buscar_modelos_carros(self,codigo_marca):
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos").json()
        
        return request['modelos']
    
    def buscar_anos_modelo_carros(self,codigo_marca,codigo_modelo):
        
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos").json()
          
        return request
    
    def buscar_veiculo(self,tipo_veiculo,codigo_marca,codigo_modelo,codigo_ano_combustivel):
        
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/{tipo_veiculo}/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano_combustivel}").json()
        
        return request
    
    
    #Consulta sobre Motos
    
    def buscar_marca_motos(self):
        request = requests.get("https://parallelum.com.br/fipe/api/v1/motos/marcas").json() 
        
        return request
    
    
    def buscar_modelos_motos(self,codigo_marca):
        request = requests.get(f"https://parallelum.com.br/fipe/api/v1/motos/marcas/{codigo_marca}/modelos").json()
    
        return request
    

        
        
    
    
    


   
    
     
        
    
    
    