import tkinter as tk
from classes.pessoa import Pessoa
from classes.Carro import Carro
from classes.Consultor import Consultor



consul = Consultor("jardel",18,"05744673512","Masculino")

consul.generateMat()
print(consul.getMat())

