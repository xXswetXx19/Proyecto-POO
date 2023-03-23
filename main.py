from vistas.incio_sesion import Login
from Functions.Database import Query

if __name__ == "__main__":
    DB_Config = Query()
    Query.Iniciar_BaseDatos(DB_Config)
    Login()

    
    