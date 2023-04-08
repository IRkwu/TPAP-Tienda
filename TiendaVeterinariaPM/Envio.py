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

    def mostrarEnvio(self):
        return f"Descripción: {self.__descripcion}\nNúmero de Seguimiento: {self.__numeroSeguimiento}\nDirección de Envío: {self.__direccionEnvio}"
    
    def CalcularDescuentoEnvio(total):
        if total >= 25000 or total == 0:
            costo_envio = 0
        else:
            costo_envio = 3000
        return costo_envio
        
    #def necesitaEnvio():
    #    while True:
    #        opcion = input("Usted necesita envio: ")
#
    #if opcion == "1":
    #    Articulos.MostrarListaArticulos()
    #elif opcion == "2":
    #    llenadoDeCarrito()