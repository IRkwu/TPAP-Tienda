import csv

class Usuario():
    
    def __init__(self, id, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, cargo, usuarios):
        self.__nombres = nombres
        self.__id = id
        self.__apellido_paterno = apellido_paterno
        self.__apellido_materno = apellido_materno
        self.__genero=genero
        self.__fecha_nacimiento = fecha_nacimiento
        self.__rut = rut
        self.__cargo = cargo
        self.__usuarios = usuarios
    
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
        
    def get_usuarios(self):
        return self.__usuarios
    
    def set_usuarios(self, usuarios):
        self.__usuarios = usuarios
        
    def CSV_Usuarios(self,usuarios):
        self.__usuarios.append(usuarios)
        with open('Archivos de Datos\Usuarios.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nombre', 'ID', 'Apellido Paterno', 'Apellido Materno', 'Género', 'Fecha de nacimiento', 'RUT', 'Cargo'])
            for Usuario in usuarios:
                writer.writerow([Usuario.get_nombres(), Usuario.get_id(), Usuario.get_apellidoPaterno(), Usuario.get_apellidoMaterno(), Usuario.get_genero(), Usuario.get_fechaDeNacimiento(), Usuario.get_rut(), Usuario.get_cargo()])