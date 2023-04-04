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
