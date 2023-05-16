import csv

cargo = [
    "Gerente",
    "Cajero",
    "Asistente de ventas"
]

class Usuario():
    
    def __init__(self, id = None, nombres = None, apellido_paterno = None, apellido_materno = None, genero = None, correo = None, fecha_nacimiento = None, rut = None, cargo = None, contrasena = None):
        self.id = id
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.genero=genero
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.rut = rut
        self.cargo = cargo
        self.contrasena = contrasena

   
    def get_nombres(self):
        return self.nombres

    def set_nombres(self, nombres):
        self.nombres = nombres
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_apellidoPaterno(self):
        return self.apellido_paterno

    def set_apellidoPaterno(self, apellidoPaterno):
        self._apellidopaterno = apellidoPaterno

    def get_apellidoMaterno(self):
        return self.apellido_materno
    
    def set_apellidoMaterno(self, apellidoMaterno):
        self.apellido_materno = apellidoMaterno
    
    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero
        
    def get_correo(self):
        return self.correo

    def set_genero(self, correo):
        self.correo = correo
        
    def get_fechaDeNacimiento(self):
        return self.fecha_nacimiento
    
    def set_fechaDeNacimiento(self, fechaNacimiento):
        self.fecha_nacimiento = fechaNacimiento
        
    def get_rut(self):
        return self.rut
    
    def set_rut(self, rut):
        self.rut = rut
        
    def get_cargo(self):
        return self.cargo
    
    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_contrasena(self):
        return self.contrasena
    
    def set_contrasena(self, contrasena):
        self.contrasena = contrasena
    
    def string(self):
        return f"{self.id},{self.nombres},{self.apellido_paterno},{self.apellido_materno},{self.genero},{self.correo},{self.fecha_nacimiento},{self.rut},{self.cargo},{self.contrasena}"