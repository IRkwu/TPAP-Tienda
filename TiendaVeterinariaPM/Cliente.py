import csv
from datetime import datetime


class Cliente:
    def __init__(self, id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial):
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
        self.__mascotas = mascotas
        self.__historial = historial

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

    def agregar_servicio_historial(self, servicio):
        self.__historial.append(servicio)


    # Funcion para guardar los clientes en un archivo csv
    def GuardarCSV_Clientes(lista_clientes):
        with open('Archivos de Datos\ListaClientes.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombres', 'Apellido Paterno', 'Apellido Materno', "Genero", 'Fecha Nacimiento', 'RUT', "Email", "Telefono", "Domicilio", "Mascotas", "Historial"])
            for Cliente in lista_clientes:
                writer.writerow([Cliente.get_id(), Cliente.get_nombres(), Cliente.get_apellidoPaterno(), Cliente.get_apellidoMaterno(), Cliente.get_genero(), Cliente.get_fechaNacimiento(), Cliente.get_rut(), Cliente.get_email(), Cliente.get_telefono(), Cliente.get_domicilio(), Cliente.get_mascotas(), Cliente.get_historial()])
              
    # Funcion para cargar los clientes desde un archivo csv
    def CargarCSV_Clientes(ruta_archivo):
        lista_clientes = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial = row
                cliente = Cliente(id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial)
                lista_clientes.append(cliente)
        return lista_clientes
    
    # Funcion para agregar clientes a un archivo csv
    def AgregarClientes(id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial):
        cliente = Cliente(id, nombres, apellidoPaterno, apellidoMaterno, genero, fechaNacimiento, rut, email, telefono, domicilio, mascotas, historial)
        ListaClientes.append(cliente)
        Cliente.GuardarCSV_Clientes(ListaClientes)
        print("El cliente se agregó correctamente a la lista de Clientes.")
    
#Inicializar la lista de Clientes por defecto, para que no haya un arreglo vacio, cargar la lista de clientes
ListaClientes = Cliente.CargarCSV_Clientes('Archivos de Datos\ListaClientes.csv') 




#PRUEBAS   
#Cliente.AgregarClientes(42685, "Fernando Juan", "Perez", "Sepulveda", "Masculino", "30/02/2001", "20459135-1", "fernando.perez@gmail.com", 154265942, "Calle B", "Periquito", "Historial")

#print(ListaClientes[0].get_apellidoMaterno())

#ListaClientes = [
#    Cliente(54103, "Federico Gonzalo", "Fernandez", "Inostroza", "Masculino", "17/06/2001", "20435942-5", "federico.fernandez@gmail.com", 513469426, "Calle A", "Perrito y Gatito", "Historial")
#]
#
#Cliente.GuadarCSV_Clientes(ListaClientes)