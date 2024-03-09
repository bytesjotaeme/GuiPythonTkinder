import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect("base_datos1.db")

    def inserta_Datos(self, nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO datos (NOMBRE, EDAD, CORREO, TELEFONO, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio)
                VALUES('{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}')'''.format(nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM datos "
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
            
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd ='''DELETE FROM datos WHERE NOMBRE = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualiza_Datos(self, IDE, nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio):
        cursor = self.conexion.cursor()
        bd = '''UPDATE datos SET NOMBRE = '{}', EDAD = '{}', CORREO = '{}', TELEFONO = '{}', dias_horarios_pedidos = '{}', horarios_reparto = '{}', productos_servicios = '{}', fecha_ingreso = '{}', cantidad_pedidos = '{}', precio = '{}'
                WHERE ID = '{}' '''.format(nombre, edad, correo, telefono, dias_horarios_pedidos, horarios_reparto, productos_servicios, fecha_ingreso, cantidad_pedidos, precio, IDE)  
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato  
