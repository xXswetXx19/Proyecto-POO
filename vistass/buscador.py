import tkinter
from tkinter import *
from Functions.Database import *

class Buscador:
    def __init__(self):
        self.query=Query()
    def buscar(self,codigo):
        consulta='SELECT * FROM libros WHERE codigo'
        parametro=(codigo)
        self.query.ejecutar_consulta(consulta,parametro)


