import sqlite3
from vistass.sesiones import *

class Query:
    def __init__(self):
        self.db='database.db' # Base de datos libros
        
    def Iniciar_BaseDatos(self):
        self.ejecutar_consulta('CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT, codigo INTEGER, nombre VARCHAR(50),autor VARCHAR(50),precio FLOAT,categoria VARCHAR(50), activo VARCHAR(2))')
        self.ejecutar_consulta('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,usuario VARCHAR(50),contraseña VARCHAR(50))')

    def ejecutar_consulta(self,consulta,parametros = ()):
        with sqlite3.connect(self.db) as conn:
            cursor=conn.cursor()
            result=cursor.execute(consulta,parametros)
            conn.commit()
        return result

    def guardar(self,codigo,nombre,autor,precio,categoria):
        sql='INSERT INTO libros(codigo,nombre,autor,precio,categoria) VALUES(?,?,?,?,?)'
        parametros=(codigo,nombre,autor,precio,categoria)
        self.ejecutar_consulta(sql,parametros)
        
    def borrar(self,codigo):
        sql='UPDATE libros SET activo="no" WHERE codigo=?'
        parametros=(codigo,)
        self.ejecutar_consulta(sql,parametros)
    
    def editar (self,codigo,nombre,autor,precio,categoria):
        sql='UPDATE libros SET nombre=?,autor=?,precio=?,categoria=? WHERE codigo=?'
        parametros=(nombre,autor,precio,categoria,codigo)
        self.ejecutar_consulta(sql,parametros)
        
