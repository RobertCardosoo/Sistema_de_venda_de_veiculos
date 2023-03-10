import json
import requests

request = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas").json()  


class Fipe():
    
    def buscar_marca_carros(self):
        self.lista = []
        count = 0
        
        for i in request:
            self.lista.append(request[count]['nome'])
            count+=1

        return self.lista
    
    
    