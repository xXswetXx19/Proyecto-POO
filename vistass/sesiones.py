from tkinter import messagebox
from tkinter import *
from Functions.centrado_de_ventana import *
from tkinter import ttk
from Functions.Database import *
from vistass.buscador import Buscador, Query

class Registro:
    def __init__(self):
        self.cv= GuiProcess()
        self.query= Query()
        self.buscar = Buscador()
        #self.categorias = ['Cientificos', 'Literatura y linguisticos', 'De viajes', 'Biografias', 'Referencia o consulta', 'Monografias', 'Recreativos', 'Poéticos', 'Juveniles', 'Ficción','Comedia']
        self.getWindow3()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.tabla()
        self.ajustarFrame()

    def getWindow3(self):
        self.wind = Tk()
        self.wind.title('Aplicación libreria')
        self.wind.geometry('1000x425')
        self.wind.iconbitmap("Files\icono.ico")
        self.wind.resizable(0, 0)
        # Creating a Frame Container
        self.frame = LabelFrame(self.wind, text='Registrar nuevo libro')
        self.frame.pack()

    def tabla(self):
        self.tree = ttk.Treeview(self.frame,height=10, columns=[f"{n}" for n in range(1, 5)])
        self.tree.place(x=0, y=157, width=997)
        self.tree.heading('#0', text='Codigo', anchor=CENTER)
        self.tree.heading('#1', text='Nombre', anchor=CENTER)
        self.tree.heading('#2', text='Autor', anchor=CENTER)
        self.tree.heading('#3', text="Precio", anchor=CENTER)
        self.tree.heading('#4', text="Categoria", anchor=CENTER)
        
        self.tree.column('#0', width=200, minwidth=100, stretch=NO, anchor=CENTER)
        self.tree.column('#1', width=200, minwidth=100, stretch=NO, anchor=CENTER)
        self.tree.column('#2', width=200, minwidth=100, stretch=NO, anchor=CENTER)
        self.tree.column('#3', width=200, minwidth=100, stretch=NO, anchor=CENTER)
        self.tree.column('#4', width=200, minwidth=100, stretch=NO, anchor=CENTER)
        
        #mostrando datos en la tabla
        self.get_libro()
        
    def ajustarFrame(self):
        # Obtener el tamaño total necesario
        total_width = max(widget.winfo_reqwidth() for widget in self.frame.winfo_children())
        total_height = sum(widget.winfo_reqheight() for widget in self.frame.winfo_children())
        # Establecer el tamaño total necesario en el frame
        self.frame.place_configure(width=total_width, height=total_height)

    def getLabels(self):
        Label(self.frame, text='Codigo:').place(x=450, y=10)
        Label(self.frame, text='Nombre: ').place(x=450, y=30)
        Label(self.frame, text='Autor: ').place(x=450, y=50)
        Label(self.frame, text='Precio: ').place(x=450, y=70)
        Label(self.frame, text='Categoria:').place(x=450, y=90)
        Label(self.frame, text='Buscar:').place(x=10,y=50)
    
    def getInputs(self):
        #input codigo
        self.codigo=Entry(self.frame,width=30)
        self.codigo.place(x=525,y=10, width=400)
        #input nombre
        self.nombre = Entry(self.frame,width=30)
        self.nombre.place(x=525, y=30, width=400)
        #input autor
        self.autor = Entry(self.frame,width=30)
        self.autor.place(x=525, y=50, width=400)
        #input precio
        self.precio = Entry(self.frame,width=30)
        self.precio.place(x=525, y=70, width=400)
        #input categorias
        self.entrycategorias =Entry(self.frame,width=30)
        self.entrycategorias.place(x=525, y=90, width=400)
        #input buscar
        self.buscar_li = Entry(self.frame,width=30)
        self.buscar_li.place(x=60, y=50, width=200)
        self.buscar_li.focus()
        
    def getButtons(self):
        style = ttk.Style()
        style.configure('TButton', background='red',fg='blue')
        ttk.Button(self.frame, text='Guardar libro',command=self.add_libro,style='TButton', width=165).place(x=0, y=133)
        Button(self.frame, text="Eliminar", command=self.eliminar_libro, width=79).place(x=0, y=382)
        Button(self.frame, text="Editar",command=self.editar_libro, width=79).place(x=500, y=382)
        Button(self.frame,text="Buscar",command=self.buscar_libro,bg="blue",fg="white").place(x=275,y=50)
        
    def get_libro(self,resultado=None):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        if resultado:
            self.tree.insert('', 0, text=resultado[1], values=(resultado[2], resultado[3], resultado[4], resultado[5]))
        else:
            query = 'SELECT * FROM libros ORDER BY codigo DESC'
            db_rows = self.query.ejecutar_consulta(query)
            for row in db_rows:
                self.tree.insert('', 0, text=row[1], values=(row[2], row[3], row[4], row[5]))
                
    def validacion(self):
        if len(self.codigo.get()) == 0 or len(self.nombre.get()) == 0 or len(self.autor.get()) == 0 or len(self.precio.get()) == 0 or len(self.entrycategorias.get()) == 0:
            return [False, 'Debe llenar todos los campos para registrar el libro']
        if not self.codigo.get().isdigit():
            return [False, 'El codigo debe ser un numero']
        if not self.precio.get().isdigit():
            return {False, 'El precio debe ser un numero'}
        return [True]
    
    def add_libro(self):
        validar = self.validacion()
        if validar[0]:
            # check if the code already exists
            codeinuse = self.query.ejecutar_consulta('SELECT * FROM libros WHERE codigo = ?', (self.codigo.get(),))
            codeinuse = codeinuse.fetchone()
            if codeinuse:
                return messagebox.showinfo(message="Ese codigo ya esta en uso", title="Error")
            consulta = 'INSERT INTO libros VALUES(NULL, ?,?,?,?,?, "si")'
            parametros = (self.codigo.get(), self.nombre.get(), self.autor.get(), self.precio.get(), self.entrycategorias.get())
            self.query.ejecutar_consulta(consulta, parametros)
            messagebox.showinfo(message="Datos guardados")
            self.codigo.delete(0, END)
            self.nombre.delete(0, END)
            self.autor.delete(0, END)
            self.precio.delete(0, END)
            self.entrycategorias.delete(0, END)
        else:
            messagebox.showinfo(message=validar[1], title="Error")
        self.get_libro()  # actualizar la tabla
        
    def eliminar_libro(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except:
            return messagebox.showinfo(message="Seleccione el registro que desea borrar", title="Error")

        ask = messagebox.askyesno(message="¿Estas seguro de eliminar este registro?", title="Eliminar")
        if ask:
            consulta = 'UPDATE libros SET estado="no" WHERE codigo=?'
            codigo=self.tree.item(self.tree.selection())['text']
            self.query.ejecutar_consulta(consulta,(codigo, ))
            self.get_libro()
            messagebox.showinfo(message="Datos eliminados")
            
    def editar_libro(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except:
            return messagebox.showinfo(message="Seleccione el registro que desea editar", title="Error")
        
        self.o_codigo=self.tree.item(self.tree.selection())['text']
        self.o_nombre=self.tree.item(self.tree.selection())['values'][0]
        self.o_autor=self.tree.item(self.tree.selection())['values'][1]
        self.o_precio=self.tree.item(self.tree.selection())['values'][2]
        self.o_categoria=self.tree.item(self.tree.selection())['values'][3]
        self.window_editar = Toplevel()
        self.window_editar.title = "Editar información del libro"
        self.window_editar.iconbitmap("Files/Icono.ico")

        # labels Nuevos datos
        Label(self.window_editar,text="Codigo").grid(row=0,column=0)
        Label(self.window_editar,text="Nombre").grid(row=1,column=0)
        Label(self.window_editar,text="Autor").grid(row=2,column=0)
        Label(self.window_editar,text="Precio").grid(row=3,column=0)
        Label(self.window_editar,text="Categoria").grid(row=4,column=0)
        #input nuevos datos
        self.nuevo_codigo = Entry(self.window_editar,textvariable=StringVar(self.window_editar,value=self.o_codigo))
        self.nuevo_codigo.grid(row=0, column=1)
        self.nuevo_nombre = Entry(self.window_editar,textvariable=StringVar(self.window_editar,value=self.o_nombre))
        self.nuevo_nombre.grid(row=1,column=1)
        self.nuevo_autor = Entry(self.window_editar,textvariable=StringVar(self.window_editar,value=self.o_autor))
        self.nuevo_autor.grid(row=2,column=1)
        self.nuevo_precio = Entry(self.window_editar,textvariable=StringVar(self.window_editar,value=self.o_precio))
        self.nuevo_precio.grid(row=3,column=1)
        self.nueva_categoria = Entry(self.window_editar,textvariable=StringVar(self.window_editar,value=self.o_categoria))
        self.nueva_categoria.grid(row=4,column=1)
        self.actualizarbutton = Button(self.window_editar, text="Actualizar",command=self.actualizar).grid(row=5, columnspan=2, sticky=W + E)
        
    def validacion_actualizar(self):
        return len(self.nuevo_codigo.get()) != 0 and len(self.nuevo_nombre.get()) != 0 and len(self.nuevo_autor.get()) != 0 and len(self.nuevo_precio.get()) != 0 and len(self.nueva_categoria.get()) != 0
    
    def actualizar(self):
        if len(self.tree.selection()) == 1 and self.validacion_actualizar():
            # First check if the new code is already in the database
            codigo = self.tree.item(self.tree.selection())['text']
            codeinuse = self.query.ejecutar_consulta('SELECT * FROM libros WHERE codigo=?', (self.nuevo_codigo.get(),))
            codeinuse = codeinuse.fetchone()
            if codeinuse:
                return messagebox.showinfo(message="Ese codigo ya esta en uso", title="Error")
            consulta = 'UPDATE libros SET codigo=?, nombre=?, autor=?, precio=?, categoria=? WHERE codigo=?'
            parametros = (
            self.nuevo_codigo.get(), self.nuevo_nombre.get(), self.nuevo_autor.get(), self.nuevo_precio.get(),
            self.nueva_categoria.get(), codigo)
            self.query.ejecutar_consulta(consulta, parametros)
            self.get_libro()
            messagebox.showinfo(message="Datos actualizados")
        else:
            return messagebox.showinfo(message="Por favor, llene todos los campos", title="Error")
        
    def buscar_libro(self):
        codigo=str(self.buscar_li.get())
        if not codigo:
            self.get_libro()
            return messagebox.showinfo(message="Por favor ingrese un codigo", title="Error")
        parametros=(codigo,)
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        consulta='SELECT * FROM libros WHERE codigo=?'
        resultado= self.query.ejecutar_consulta(consulta,parametros).fetchone()
        if resultado:
            self.get_libro(resultado)









