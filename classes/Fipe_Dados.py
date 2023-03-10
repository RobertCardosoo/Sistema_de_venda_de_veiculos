import json
with open("classes/marcas_carros.json",encoding='utf-8') as meu_json:
    marcas = json.load(meu_json)
    
class Fipe():
    
    def buscar_marca_carros(self):
        self.lista = []
        count = 0
        
        for i in marcas:
            self.lista.append(marcas[count]['nome'])
            count+=1

        return self.lista
    
    
    