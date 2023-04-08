import csv
from datetime import datetime


class Cliente:
    def __init__(self, id, nombre, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial):
        self.__id = id
        self.__nombre = nombre
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__genero = genero
        self.__fechaNacimiento = fechaNacimiento
        self.__rut = rut
        self.__email = email
        self.__telefono = telefono
        self.__domicilio = domicilio
        self.__mascotas = mascotas
        self.__historial = historial

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellidoPaterno(self):
        return self.__apellidoPaterno

    def set_apellidoPaterno(self, apellidoPaterno):
        self.__apellidoPaterno = apellidoPaterno

    def get_apellidoMaterno(self):
        return self.__apellidoMaterno

    def set_apellidoMaterno(self, apellidoMaterno):
        self.__apellidoMaterno = apellidoMaterno

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_fechaNacimiento(self):
        return self.__fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def get_rut(self):
        return self.__rut

    def set_rut(self, rut):
        self.__rut = rut

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_domicilio(self):
        return self.__domicilio

    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def get_mascotas(self):
        return self.__mascotas

    def set_mascotas(self, mascotas):
        self.__mascotas = mascotas

    def agregar_mascota(self, mascota):
        self.__mascotas.append(mascota)

    def get_historial(self):
        return self.__historial

    def set_historial(self, historial):
        self.__historial = historial

    def agregar_servicio_historial(self, servicio, historial_cliente):
        self.__historial.append(servicio)
        with open('Archivos de Datos\HistorialCliente.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nombre Vendedor', 'Nombre Cliente', 'Fecha', 'Productos', 'Total', 'Costo Envío', 'Fecha de última compra'])
            for cliente in historial_cliente:
                writer.writerow([cliente.get_nombre(), articulo.get_mascota(), articulo.get_id(), articulo.get_marca(), articulo.get_precio_por_unidad(), articulo.get_stock(), articulo.get_descripcion(), articulo.get_categoria(), articulo.get_precio_por_lote(), articulo.get_limite_critico()])