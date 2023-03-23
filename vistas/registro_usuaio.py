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
        self.bindEvents()
    def centrar(self):
        # self.update_idletasks()
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))
        
    def crear_widgets(self):
        self.lbl_titulo = tk.Label(self, text="Registro de usuario", fg="white", bg="orange", font=('ITALIC', 15, 'bold'))
        self.lbl_titulo.place(x=105, y=10)
        self.lbl_usuario = tk.Label(self, text="Usuario",  bg="orange", font=('ITALIC', 10, 'bold'), fg="black")
        self.lbl_usuario.place(x=60, y=50)
        self.txt_usuario = tk.Entry(self, width=30)
        self.txt_usuario.place(x=150, y=50)
        self.lbl_password = tk.Label(self, text="Contraseña",  bg="orange", font=('ITALIC', 10, 'bold'), fg="black")
        self.lbl_password.place(x=60, y=100)
        self.txt_password = tk.Entry(self, width=30, show="*")
        self.txt_password.place(x=150, y=100)
        self.btn_registrar= tk.Button(self, fg="white", text="Registrar",bg="#335BFF",font=('ITALIC', 10, 'bold'), cursor="hand2", command=self.registrar, bd=0)
        self.btn_registrar.place(x=171, y=150)
        
    def registrar(self, event = None):
        usuario = self.txt_usuario.get()
        password = self.txt_password.get()
        if usuario and password:
            check = self.Query.ejecutar_consulta('SELECT * FROM usuarios WHERE usuario = %s', (usuario,))
            check = check[0] if len(check) > 0 else None
            if check:
                messagebox.showerror(message="Ese usuario ya existe en el sistema", title="Mensaje")
                return self.focus()
            self.Query.ejecutar_consulta('INSERT INTO usuarios VALUES(NULL, %s, %s)', (usuario, password))
            messagebox.showinfo(message="Usuario registrado", title="Mensaje")
            self.destroy()
        else:
            messagebox.showerror(message="Debe ingresar un usuario y contraseña para registrar", title="Mensaje")
            self.focus()

    def bindEvents(self):
        self.bind("<Return>", self.registrar)