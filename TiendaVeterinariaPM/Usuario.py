class Usuario():
    
    def __init__(self, id, nombres, apellido_paterno, apellido_materno, genero, fecha_nacimiento, rut, cargo):
        self._nombres = nombres
        self._id = id
        self._apellido_paterno = apellido_paterno
        self._apellidomaterno = apellido_materno
        self._genero=genero
        self._fecha_nacimiento = fecha_nacimiento
        self._rut = rut
        self._cargo = cargo
    cargo = []