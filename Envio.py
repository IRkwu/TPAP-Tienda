import csv
from Usuario import Usuario, Lista_Usuarios
from Cliente import Cliente, ListaClientes
import random
import time


class Envio:
    def __init__(self, descripcion, numeroSeguimiento, direccionEnvio):
        self.__descripcion = descripcion
        self.__numeroSeguimiento = numeroSeguimiento
        self.__direccionEnvio = direccionEnvio

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_numeroSeguimiento(self):
        return self.__numeroSeguimiento

    def set_numeroSeguimiento(self, numeroSeguimiento):
        self.__numeroSeguimiento = numeroSeguimiento

    def get_direccionEnvio(self):
        return self.__direccionEnvio

    def set_direccionEnvio(self, direccionEnvio):
        self.__direccionEnvio = direccionEnvio

    # Funcion para ver el envio, se compara el id, que es el mismo para el cliente, boleta y envio
    def mostrarEnvio(id_transaccion):
        # Se carga la Lista de Envios para poder comprobar si el envio ya existe
        ListaEnvios = Envio.CargarCSV_Envios(
            'Archivos de Datos\ListaEnvios.csv')
        for envio in ListaEnvios:
            if envio.get_numeroSeguimiento() == id_transaccion:
                print("\nDescripción:", envio.get_descripcion())
                print("Número de seguimiento:", envio.get_numeroSeguimiento())
                print("Dirección de envío:", envio.get_direccionEnvio())
                return
        print("No se encontró el envío con número de seguimiento", id_transaccion)

    # Funcion para calcular el descuento de envio, si los productos superan los $25000 el envio es gratis, sino cuesta $3000
    def CalcularDescuentoEnvio(total):
        if total >= 25000 or total == 0:
            costo_envio = 0
        else:
            costo_envio = 3000
        return costo_envio

    # Funcion para guardar los envios en un archivo csv

    def GuardarCSV_Envios(lista_envios):
        with open('Archivos de Datos\ListaEnvios.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Descripcion", "Numero de Seguimiento", "Envio"])
            for Envio in lista_envios:
                writer.writerow([Envio.get_descripcion(
                ), Envio.get_numeroSeguimiento(), Envio.get_direccionEnvio()])

    # Funcion para cargar los envios desde un archivo csv
    def CargarCSV_Envios(ruta_archivo):
        lista_envios = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                descripcion, numeroSeguimiento, direccionEnvio = row
                envio = Envio(descripcion, numeroSeguimiento, direccionEnvio)
                lista_envios.append(envio)
        return lista_envios

    # Funcion para agregar nuevos envios al archivo csv
    def AgregarEnvios(self, descripcion, numeroSeguimiento, direccionEnvio):
        envio = Envio(descripcion, numeroSeguimiento, direccionEnvio)
        ListaEnvios.append(envio)
        Envio.GuardarCSV_Envios(ListaEnvios)
        print("El envio se agregó correctamente a la lista de Envios.")


# Inicializar la Lista de Envios por defecto, para que no haya un arreglo vacio, cargar la lista de envios
ListaEnvios = Envio.CargarCSV_Envios('Archivos de Datos\ListaEnvios.csv')


# PRUEBAS
# print(ListaEnvios[0].get_descripcion())

# ListaEnvios = [
#    Envio("Productos de la tienda TPAP", "37891267398213", "Direccion de envio")
# ]
# Envio.GuardarCSV_Envios(ListaEnvios)
