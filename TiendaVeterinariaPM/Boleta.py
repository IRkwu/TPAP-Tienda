import datetime
import random
import csv
from Cliente import Cliente, ListaClientes
from Carrito import Carrito, Carrito_Cliente
from Envio import Envio
from Usuario import Usuario, Lista_Usuarios

    
class Boleta:
    def __init__(self, id_transaccion, nombre_vendedor, nombre_cliente, fecha, articulos, total, costo_envio):
        self.__id_transaccion = id_transaccion
        self.__nombre_vendedor = nombre_vendedor
        self.__nombre_cliente = nombre_cliente
        self.__fecha = fecha
        self.__articulos = articulos
        self.__total = total
        self.__costo_envio = costo_envio
        
    # Getters
    def get_id_transaccion(self):
        return self.__id_transaccion    
    
    def get_nombre_vendedor(self):
        return self.__nombre_vendedor
    
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def get_fecha(self):
        return self.__fecha
    
    def get_articulos(self):
        return self.__articulos
    
    def get_total(self):
        return self.__total
    
    def get_costo_envio(self):
        return self.__costo_envio
    
    # Setters
    def set_id_transaccion(self, id_transaccion):
        self.__id_transaccion = id_transaccion
    
    def set_nombre_vendedor(self, nombre_vendedor):
        self.__nombre_vendedor = nombre_vendedor
        
    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_articulos(self, articulos):
        self.__articulos = articulos
        
    def set_total(self, total):
        self.__total = total

    # Funcion para guardar los envios en un archivo csv
    def GuardarCSV_Boletas(historial_boletas):
        with open('Archivos de Datos\HistorialBoletas.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['id_transaccion','nombre_vendedor', 'nombre_cliente', 'fecha', 'articulos', 'total', 'costo_envio'])
            for boleta in historial_boletas:
                writer.writerow([boleta.get_id_transaccion(), boleta.get_nombre_vendedor(), boleta.get_nombre_cliente(), boleta.get_fecha(), boleta.get_articulos(), boleta.get_total(), boleta.get_costo_envio()])

    # Funcion para cargar los envios desde un archivo csv
    def CargarCSV_Boletas(ruta_archivo):
        historial_boletas = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id_transaccion, nombre_vendedor, nombre_cliente, fecha, articulos, total, costo_envio = row
                boleta = Boleta(id_transaccion, nombre_vendedor, nombre_cliente, fecha, articulos, total, costo_envio)
                historial_boletas.append(boleta)
        return historial_boletas

    # Funcion para agregar las boletas en un archivo csv
    def AgregarBoleta(id_transaccion, nombre_vendedor, nombre_cliente, fecha, articulos, total, costo_envio):
        boleta = Boleta(id_transaccion, nombre_vendedor, nombre_cliente, fecha, articulos, total, costo_envio)
        HistorialBoletas.append(boleta)
        Boleta.GuardarCSV_Boletas(HistorialBoletas)
        print("La boleta se ha agregado correctamente al Historial de Boletas.")
        
    # Funcion para imprimir la boleta
    def imprimir_boleta(self):
        print("================================")
        print("        BOLETA DE VENTA")
        print("================================")
        print("ID de Transacción:", self.get_id_transaccion())
        print("Vendedor:", self.get_nombre_vendedor())
        print("Cliente:",self.get_nombre_cliente())
        print("Fecha:", self.get_fecha())
        print("\nLista de Articulos:")
        contador = 1
        articulos = self.get_articulos()
        if articulos:
            for articulo in articulos:
                print(articulo)
            print("\n")
        costo_envio = self.get_costo_envio()
        print("Costo de envío: $", costo_envio, sep='')
        total = Carrito_Cliente.CalcularTotal()
        total += costo_envio
        if total:
            print("Total:", total)
        print("================================")

#Inicializar la lista de Boletas por defecto, para que no haya un arreglo vacio, cargar el historial de boletas
HistorialBoletas = Boleta.CargarCSV_Boletas('Archivos de Datos\HistorialBoletas.csv')    

    
        
        
#Ejemplo
#boleta1 = Boleta("Juan", "Maria", "2023-04-04", ["Producto 1, Producto 2"], 28900, 0)
#boleta1.imprimir_boleta()