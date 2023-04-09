import csv

cargo = [
    "Gerente",
    "Cajero",
    "Asistente de ventas"
]

class Usuario():
    
    def __init__(self, id, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, cargo):
        self.__id = id
        self.__nombres = nombres
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__genero=genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__rut = rut
        self.__cargo = cargo
    
    def get_nombres(self):
        return self.__nombres

    def set_nombres(self, nombres):
        self.__nombres = nombres
    
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_apellidoPaterno(self):
        return self.__apellido_paterno

    def set_apellidoPaterno(self, apellidoPaterno):
        self.__apellido_paterno = apellidoPaterno

    def get_apellidoMaterno(self):
        return self.__apellido_materno
    
    def set_apellidoMaterno(self, apellidoMaterno):
        self.__apellido_materno = apellidoMaterno
    
    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero
        
    def get_fechaDeNacimiento(self):
        return self.__fecha_nacimiento
    
    def set_fechaDeNacimiento(self, fechaNacimiento):
        self.__fecha_nacimiento = fechaNacimiento
        
    def get_rut(self):
        return self.__rut
    
    def set_rut(self, rut):
        self.__rut = rut
        
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, cargo):
        self.__cargo = cargo
        
    # Funcion para guardar los usuarios en un archivo csv
    def GuadarCSV_Usuarios(lista_usuarios):
        with open('Archivos de Datos\ListaUsuarios.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['ID', 'Nombre', 'Apellido Paterno', 'Apellido Materno', 'Género', 'Fecha de nacimiento', 'RUT', 'Cargo'])
            for Usuario in lista_usuarios:
                writer.writerow([Usuario.get_id(), Usuario.get_nombres(), Usuario.get_apellidoPaterno(), Usuario.get_apellidoMaterno(), Usuario.get_genero(), Usuario.get_fechaDeNacimiento(), Usuario.get_rut(), Usuario.get_cargo()])

    # Funcion para cargar los usuarios desde un archivo csv
    def CargarCSV_Usuarios(ruta_archivo):
        lista_usuarios = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                id, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, cargo = row
                usuario = Usuario(id, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, cargo)
                lista_usuarios.append(usuario)
        return lista_usuarios
    
    
#Inicializar la lista de Usuarios por defecto, para que no haya un arreglo vacio, cargar la lista de usuarios
Lista_Usuarios = Usuario.CargarCSV_Usuarios('Archivos de Datos\ListaUsuarios.csv')


#PRUEBAS
#Ejemplo mostrar los cargos de los usuarios
#print(Lista_Usuarios[0].get_cargo())
#print(Lista_Usuarios[1].get_cargo())
#print(Lista_Usuarios[2].get_cargo())

#Ejemplo para guardar la lista de usuarios
#Usuarios=[
#    Usuario(3982, "Clay", "Hernández", "Torres", "Femeneno", "17/06/1992", "18732493-K", cargo[0]),
#    Usuario(8644, "Hector", "Martínez", "García", "Masculino", "08/03/1995", "19132392-2", cargo[1]),
#    Usuario(9454, "Carlos", "Morales", "Ramírez", "Masculino", "29/09/2000", "20892423-6", cargo[2]),
#]
#Usuario.GuadarCSV_Usuarios(Usuarios)
