from Carrito import Carrito
from Boleta import Boleta

class Venta:
    def__init__(self, descuento_stock, descuento_envio):
        self._descuento_stock = descuento_stock
        self._descuento_envio = descuento_envio
        
    def confirmar_venta(self):
        Boleta.imprimir_boleta(self)