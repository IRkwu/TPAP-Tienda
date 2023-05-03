import csv
from PyQt5.QtWidgets import *


class Cliente:
    def __init__(self, id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio):
        self.__id = id
        self.__nombres = nombres
        self.__apellidoPaterno = apellidoPaterno
        self.__apellidoMaterno = apellidoMaterno
        self.__genero = genero
        self.__fechaNacimiento = fechaNacimiento
        self.__rut = rut
        self.__email = email
        self.__telefono = telefono
        self.__domicilio = domicilio

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombres(self):
        return self.__nombres

    def set_nombres(self, nombres):
        self.__nombres = nombres

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
        
        
        
    def GuardarCSV_Clientes(self, lista_clientes):
        with open('Archivos de Datos\ListadeClientes.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombres', 'Apellido Paterno', 'Apellido Materno', "Genero",
                            'Fecha Nacimiento', 'RUT', "Email", "Telefono", "Domicilio"])
            for Cliente in lista_clientes:
                writer.writerow([Cliente.get_id(), Cliente.get_nombres(), Cliente.get_apellidoPaterno(), Cliente.get_apellidoMaterno(), Cliente.get_genero(), Cliente.get_fechaNacimiento(
                ), Cliente.get_rut(), Cliente.get_email(), Cliente.get_telefono(), Cliente.get_domicilio()])
            
    # Funcion para cargar los clientes desde un archivo csv

    def CargarCSV_Clientes(self, ruta_archivo):
        lista_clientes = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                    id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio = row
                    cliente = Cliente(id, nombres, apellidoPaterno, apellidoMaterno, genero,
                                  fechaNacimiento, rut, email, telefono, domicilio)
                    lista_clientes.append(cliente)
        return lista_clientes

    # Funcion para agregar clientes a un archivo csv

    def AgregarClientes(self, id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio):
        cliente = Cliente(id, nombres, apellidoPaterno, apellidoMaterno, genero,
                          fechaNacimiento, rut, email, telefono, domicilio)
        ListaClientes.append(cliente)
        self.GuardarCSV_Clientes(ListaClientes)
        print("El cliente se agregó correctamente a la lista de Clientes.")
    
ListaClientes = Cliente.CargarCSV_Clientes(None,
                                           'Archivos de Datos\ListadeClientes.csv')


def buscar_cliente(id, clientes):
    for cliente in clientes:
        if cliente.get_id() == id:
            return cliente
    return None


def imprimir_datos_cliente(id_cliente):
    with open('Archivos de Datos\ListadeClientes.csv', mode="r") as archivo:
        reader = csv.reader(archivo)
        encontrado = False
        for row in reader:
            if row[0] == id_cliente:
                print("Datos del cliente:")
                print(f"ID: {row[0]}")
                print(f"Nombres: {row[1]}")
                print(f"Apellido Paterno: {row[2]}")
                print(f"Apellido Materno: {row[3]}")
                print(f"Género: {row[4]}")
                print(f"Fecha de Nacimiento: {row[5]}")
                print(f"RUT: {row[6]}")
                print(f"Email: {row[7]}")
                print(f"Teléfono: {row[8]}")
                print(f"Domicilio: {row[9]}")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró un cliente con el ID {id_cliente}")

# cliente = ingresar_cliente()

# with open("ListaClientes.csv", mode="a", newline="") as archivo_csv:
#    writer = csv.writer(archivo_csv, delimiter=",")
#    writer.writerow([cliente.get_id(), cliente.get_nombres(), cliente.get_apellidoPaterno(), cliente.get_apellidoMaterno(), cliente.get_genero(), cliente.get_fechaNacimiento(), cliente.get_rut(), cliente.get_email(), cliente.get_telefono(), cliente.get_domicilio(), cliente.get_mascotas(), cliente.get_historial()])

#eliminar_cliente("4567")

#imprimir_datos_cliente('1234')

#editar_cliente('1234')