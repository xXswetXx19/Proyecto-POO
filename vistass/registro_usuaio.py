# Tkinter Toplevel for user registration
import tkinter as tk
from tkinter import messagebox
from Functions.Database import Query

class RegistroUsuario(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.Query=Query()
        self.title("Registro")
        self.geometry("400x200")
        self.resizable(0, 0)
        self.config(bg="orange")
        self.iconbitmap("Files\icono.ico")
        self.centrar()
        self.crear_widgets()
    def centrar(self):
        # self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        
    def crear_widgets(self):
        self.lbl_titulo = tk.Label(self, text="Registro de usuario", bg="orange", fg="black")
        self.lbl_titulo.place(x=150, y=10)
        self.lbl_usuario = tk.Label(self, text="Usuario", bg="orange", fg="black")
        self.lbl_usuario.place(x=50, y=50)
        self.txt_usuario = tk.Entry(self, width=30)
        self.txt_usuario.place(x=150, y=50)
        self.lbl_password = tk.Label(self, text="Contraseña", bg="orange", fg="black")
        self.lbl_password.place(x=50, y=100)
        self.txt_password = tk.Entry(self, width=30, show="*")
        self.txt_password.place(x=150, y=100)
        self.btn_registrar = tk.Button(self, text="Registrar", command=self.registrar)
        self.btn_registrar.place(x=200, y=150)
        
    def registrar(self):
        usuario = self.txt_usuario.get()
        password = self.txt_password.get()
        if usuario and password:
            check = self.Query.ejecutar_consulta('SELECT * FROM usuarios WHERE usuario = ?', (usuario,))
            check = check.fetchone()
            if check:
                return messagebox.showerror(message="Ese usuario ya existe en el sistema", title="Mensaje")
            self.Query.ejecutar_consulta('INSERT INTO usuarios VALUES(NULL, ?, ?)', (usuario, password))
            messagebox.showinfo(message="Usuario registrado", title="Mensaje")
            self.destroy()
        else:
            messagebox.showerror(message="Debe ingresar un usuario y contraseña", title="Mensaje")
            self.destroy()
