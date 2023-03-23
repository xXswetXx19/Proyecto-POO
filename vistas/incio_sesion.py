import tkinter as tk
from tkinter import *
from tkinter import messagebox
from vistas.sesiones import Registro
from Functions.centrado_de_ventana import GuiProcess
from Functions.Database import Query
from vistas.registro_usuaio import RegistroUsuario


class Login:
    def __init__(self):
        self.cv = GuiProcess()
        self.Query=Query()
        self.getWindow()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.bindEvents()
        self.ven.resizable(0,0)
        self.ven.mainloop()
    def verificar(self, event = None):
        usu = self.entryuser.get() or None
        passw = self.entrypass.get() or None
        UsersData = self.Query.ejecutar_consulta('SELECT * FROM usuarios WHERE usuario = %s', (usu,))
        UsersData = UsersData[0] if UsersData else None
        if usu and passw:
            if UsersData:
                Id, Usuario, Contraseña = UsersData
                if passw == Contraseña:
                    self.ven.destroy()
                    return Registro()
            return messagebox.showerror(message="Usuario o contraseña incorrecta", title="Mensaje")
        else:
            return messagebox.showerror(message="Debe ingresar un usuario y contraseña", title="Mensaje")
               
    def getWindow(self):
        self.ven = Tk()
        self.cv.center(self.ven,700,500)
        self.ven.geometry("700x500")
        self.ven.title("Libreria")
        self.ven.config(bg="orange")
        self.ven.iconbitmap("Files\icono.ico")
        # frame
        self.frem = Frame(self.ven, width=350, height=450, bg="orange")
        self.frem.place(x=175, y=20)

    def getLabels(self):
        self.imagen = tk.PhotoImage(file="Files\imagen.png")
        Label(self.frem,image=self.imagen,bg="orange").place(x=123,y=30)
        #Label(self.ven, image=self.img, bg="white").place(x=50, y=70)
        signin = Label(self.frem, text="Iniciar sesion", fg="white", bg="orange",
                       font=('ITALIC', 15, 'bold')).place(x=109, y=145)
        self.username = Label(self.frem, fg="black", text="Usuario",
                              bg="orange", font=('ITALIC', 10, 'bold')).place(x=32, y=180)
        self.password = Label(self.frem, fg="black", text="Contraseña",
                              bg="orange", font=('ITALIC', 10, 'bold')).place(x=32, y=240)
        self.registro=Label(self.frem,text="Aun no tienes una cuenta?",fg="black",bg="orange",font=('ITALIC',8,'bold')).place(x=52,y=380)

    def getInputs(self):
        #usuario
        self.entryuser = Entry(self.frem, bg="white")
        self.entryuser.place(x=32, y=200, width=285, height=30)
        #password
        self.entrypass = Entry(self.frem, bg="white", show="*")
        self.entrypass.place(x=32, y=260, width=285, height=30)

    def getButtons(self):
        self.login= Button(self.frem, fg="white", text="Iniciar sesion",bg="#335BFF",font=('ITALIC', 10, 'bold'), cursor="hand2", command=self.verificar, width=30,height=2, bd=0)
        self.login.place(x=52, y=310)
        
        self.registrate=Button(self.frem,fg="white",text="Registrate",bg="#01030B",font=('ITALIC', 10, 'bold'), cursor="hand2", width=10, bd=0,command=RegistroUsuario).place(x=210, y=377)

    def bindEvents(self):
        self.ven.bind("<Return>", self.verificar)
        
    def accion(self):
        self.ven.destroy()
        Registro()


