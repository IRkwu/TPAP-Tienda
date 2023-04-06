from Carrito import Carrito
from Boleta import Boleta

class Venta:
    def __init__(self, descuento_stock, descuento_envio,):
        self.__descuento_stock = descuento_stock
        self.__descuento_envio = descuento_envio
        
    def confirmar_venta(self):
        Boleta.imprimir_boleta(self)
        