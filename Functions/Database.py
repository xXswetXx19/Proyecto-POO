import mysql.connector
from vistass.sesiones import *

class Query:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'S@muel312',
            'host': 'localhost',
            'database': 'biblioteca',
        }
        
    def Iniciar_BaseDatos(self):
        with mysql.connector.connect(**self.config) as conn:
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTO_INCREMENT, codigo VARCHAR(4), nombre VARCHAR(50), autor VARCHAR(50), precio FLOAT, categoria VARCHAR(50), activo VARCHAR(2))')
            cursor.execute('CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTO_INCREMENT, usuario VARCHAR(50), contraseña VARCHAR(50))')
            conn.commit()
            
    def ejecutar_consulta(self, consulta, parametros = ()):
        with mysql.connector.connect(**self.config) as conn:
            cursor = conn.cursor()
            cursor.execute(consulta, parametros)
            result = cursor.fetchall()
            conn.commit()
        return result



    def guardar(self, codigo, nombre, autor, precio, categoria):
        sql = 'INSERT INTO libros(codigo, nombre, autor, precio, categoria) VALUES(%s, %s, %s, %s, %s)'
        parametros = (codigo, nombre, autor, precio, categoria)
        self.ejecutar_consulta(sql, parametros)

    def borrar(self, codigo):
        sql = 'UPDATE libros SET activo="no" WHERE codigo=%s'
        parametros = (codigo,)
        self.ejecutar_consulta(sql, parametros)

    def editar (self, codigo, nombre, autor, precio, categoria):
        sql = 'UPDATE libros SET nombre=%s, autor=%s, precio=%s, categoria=%s WHERE codigo=%s'
        parametros = (nombre, autor, precio, categoria, codigo)
        self.ejecutar_consulta(sql, parametros)
