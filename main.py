from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage, StringVar, Scrollbar, Frame, messagebox
from conexion_sqlite1 import Comunicacion
import pandas as pd

class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.nombre = StringVar()
        self.edad = StringVar()
        self.correo = StringVar()
        self.telefono = StringVar()
        self.dias_horarios_pedidos = StringVar()
        self.horarios_reparto = StringVar()
        self.productos_servicios = StringVar()
        self.fecha_ingreso = StringVar()
        self.cantidad_pedidos = StringVar()
        self.precio = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=5)
        self.base_datos1 = Comunicacion()

        self.widgets()

    def widgets(self):
        self.frame_uno = Frame(self.master, bg='white', height=200, width=800)
        self.frame_uno.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg='white',height=300,width=800)
        self.frame_dos.grid(column=0, row=1, sticky='nsew')

        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Label(self.frame_uno, text='Opciones', bg='white', fg='black', font=('Kaufmann BT', 13, 'bold')).grid(column=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font=('Arial', 9, 'bold'), command=self.actualizar_tabla, fg='black', bg='deep sky blue', width=20, bd=3).grid(column=2, row=1, pady=11)
        
        Entry(self.frame_uno, textvariable=self.nombre, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=1)
        Entry(self.frame_uno, textvariable=self.edad, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=2)
        Entry(self.frame_uno, textvariable=self.correo, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=3)
        Entry(self.frame_uno, textvariable=self.telefono, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=4)
        Entry(self.frame_uno, textvariable=self.dias_horarios_pedidos, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=5)
        Entry(self.frame_uno, textvariable=self.horarios_reparto, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=6)
        Entry(self.frame_uno, textvariable=self.productos_servicios, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=7)
        Entry(self.frame_uno, textvariable=self.fecha_ingreso, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=8)
        Entry(self.frame_uno, textvariable=self.cantidad_pedidos, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=9)
        Entry(self.frame_uno, textvariable=self.precio, font=('Comic Sans MS', 12), highlightbackground='deep sky blue', highlightthickness=5).grid(column=1,row=10)
        
        Button(self.frame_uno, text='AÑADIR DATOS', font=('Arial', 9, 'bold'), bg='deep sky blue', width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='LIMPIAR CAMPOS', font=('Arial', 9, 'bold'), bg='deep sky blue', width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text='ACTUALIZAR DATOS', font=('Arial', 9, 'bold'), bg='deep sky blue', width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text='EXPORTAR A EXCEL', font=('Arial', 9, 'bold'), bg='deep sky blue', width=20, bd=3, command=self.guardar_datos).grid(column=2, row=5, pady=5, padx=5)

        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font = ('Helvetica', 10, 'bold'), foreground='black',
                               foreground='white')
        estilo_tabla.map('Treeview', background=[('selected', 'deep sky blue')],
                         foreground=[('selected','black')] )
        estilo_tabla.configure('Heading',background = 'white', foreground='deep sky blue',
                               padding=3, font= ('Arial', 10, 'bold'))

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient ='horizontal', command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky= 'ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient ='vertical', command =self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')
        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

        self.tabla['columns'] = ('Edad', 'Correo', 'Telefono', 'Dias_Horarios_Pedidos', 'Horarios_Reparto', 'Productos_Servicios', 'Fecha_Ingreso', 'Cantidad_Pedidos', 'Precio')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Edad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Correo', minwidth=100, width=120, anchor='center')
        self.tabla.column('Telefono', minwidth=100, width=120, anchor='center')                         
        self.tabla.column('Dias_Horarios_Pedidos', minwidth=100, width=120, anchor='center')
        self.tabla.column('Horarios_Reparto', minwidth=100, width=120, anchor='center')
        self.tabla.column('Productos_Servicios', minwidth=100, width=120, anchor='center')
        self.tabla.column('Fecha_Ingreso', minwidth=100, width=120, anchor='center')
        self.tabla.column('Cantidad_Pedidos', minwidth=100, width=120, anchor='center')
        self.tabla.column('Precio', minwidth=100, width=120, anchor='center')

        self.tabla.heading('#0', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Edad', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Correo', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Telefono', minwidth=100, width=120, anchor='center')                         
        self.tabla.heading('Dias_Horarios_Pedidos', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Horarios_Reparto', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Productos_Servicios', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Fecha_Ingreso', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Cantidad_Pedidos', minwidth=100, width=120, anchor='center')
        self.tabla.heading('Precio', minwidth=100, width=120, anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1", self.eliminar_datos)

    def obtener_fila(self, event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre.set(self.data['text'])
        self.edad.set(self.data['values'][0])
        self.correo.set(self.data['values'][1])
        self.telefono.set(self.data['values'][2])
        self.dias_horarios_pedidos.set(self.data['values'][3])
        self.horarios_reparto.set(self.data['values'][4])
        self.productos_servicios.set(self.data['values'][5])
        self.fecha_ingreso.set(self.data['values'][6])
        self.cantidad_pedidos.set(self.data['values'][7])
        self.precio.set(self.data['values'][9])

    def eliminar_datos(self, event):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', 'Desea eliminar?')
        if x == 'yes' :
             self.tabla.delete(item)
             self.base_datos1.elimina_datos(self.data['text'])

    def agregar_datos(self):
        nombre = self.nombre.get()
        edad = self.edad.get()
        correo = self.correo.get()
        telefono = self.telefono.get()
        dias_horarios_pedidos = self.nombre.get()
        horarios_reparto = self.horarios_reparto.get()
        productos_servicios = self.productos_servicios.get()
        fecha_ingreso = self.fecha_ingreso.get()
        cantidad_pedidos = self.cantidad_pedidos.get()
        precio = self.precio.get()
        datos = (edad, correo, telefono, dias_horarios_pedidos, horarios_reparto,  productos_servicios, fecha_ingreso, cantidad_pedidos, precio)
        if nombre and edad and edad and correo and telefono and dias_horarios_pedidos and productos_servicios and fecha_ingreso and cantidad_pedidos and precio != '':
             self.tabla.insert('', 0, text=nombre, values=datos)
             self.base_datos1.inserta_datos(nombre, edad, correo, telefono, dias_horarios_pedidos, productos_servicios, fecha_ingreso, cantidad_pedidos, precio)
             self.limpiar_campos()

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos1.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = i-1
        for dato in datos:
            i=i+1
            self.tabla.insert('', i, text = datos[I][1:2][0], values=datos[i][2:10])
        

    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        nombre = self.data['text']
        datos = self.base_datos1.mostrar_datos()
        for fila in datos:
            Id = fila[0]
            nombre_bd = fila[1]
            if nombre_bd == nombre:
                if Id != None:
                     nombre = self.nombre.get()
                     edad = self.edad.get()
                     correo = self.correo.get()
                     telefono = self.telefono.get()
                     dias_horarios_pedidos = self.nombre.get()
                     horarios_reparto = self.horarios_reparto.get()
                     productos_servicios = self.productos_servicios.get()
                     fecha_ingreso = self.fecha_ingreso.get()
                     cantidad_pedidos = self.cantidad_pedidos.get()
                     precio = self.precio.get()
                     if nombre and edad and correo and telefono and dias_horarios_pedidos and horarios_reparto and productos_servicios and fecha_ingreso and cantidad_pedidos and precio != '':
                         self.base_datos1.actualiza_datos(Id, nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio)
                         self.tabla.delete(*self.tabla.get_children())
                         datos = self.base_datos1.mostrar_datos()
                         i = -1
                         for dato in datos:
                             i= i+1
                             self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:11])


    def limpiar_campos(self):
        self.nombre.set('')
        self.edad.set('')
        self.correo.set('')
        self.telefono.set('')
        self.dias_horarios_pedidos.set('')
        self.horarios_reparto.set('')
        self.productos_servicios.set('')
        self.fecha_ingreso.set('')
        self.cantidad_pedidos.set('')
        self.precio.set('')


    def guardar_datos(self):
        self.limpiar_campos()
        datos = self.base_datos1.mostrar_datos()
        i = -1
        nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio = [], [], [], [], [], [], [], [], [], []
        for dato in datos:
            nombre.append(datos[i][1])
            edad.append(datos[i][2])
            correo.append(datos[i][3])
            telefono.append(datos[i][4])
            dias_horarios_pedidos.append(datos[i][5])
            horarios_reparto.append(datos[i][6])
            productos_servicios.append(datos[i][7])
            fecha_ingreso.append(datos[i][8])
            cantidad_pedidos.append(datos[i][9])
            precio.append(datos[i][10])
        fecha = str (strftime('%d-%m-%y_%H-%M-%S'))
        datos = {'Nombres': nombre, 'Edad': edad, 'Correo': correo, 'telefono': telefono,
                 'dias_horarios_pedidos': dias_horarios_pedidos, 'horarios_reparto': horarios_reparto,
                 'productos_servicios': productos_servicios, 'fecha_ingreso': fecha_ingreso,
                 'cantidad_pedidos': cantidad_pedidos, 'precio': precio}
        df = pd.DataFrame(datos, columns=['Nombres', 'Edad', 'Correo', 'telefono', 'dias_horarios_pedidos',
                                           'horarios_reparto', 'productos_servicios', 'fecha_ingreso',
                                           'cantidad_pedidos', 'precio'])
        df.to_excel((f'DATOS {fecha}.xlsx'))
        messagebox.showinfo('Informacion', 'Datos guardados')

if __name__ == "__main__":
    ventana = Tk()
    ventana.title('')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500')
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    app.mainloop() 
