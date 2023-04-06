from Articulos import *

class Carrito():
    
    def __init__(self, ArticulosCarrito, total_precio):
        self._ArticulosCarrito = [ArticulosCarrito]
        self._total_precio = total_precio
        self._cant_articulos = len(ArticulosCarrito)
    
    
    def AgregarArticulo(self, indice):
        if Carrito.VerificarStockArticulos(self, indice) == False:
            print("Error!!! Producto sin stock")
        else: 
            self.ArticulosCarrito.append(ListaArticulos[indice])
        
    def EliminarArticulo(self):
        self._ArticulosCarrito.pop(indice)
        
    def VerificarStockArticulos(self, indice):
        if ListaArticulos[indice].get_stock == 0:
            return False
        
    def CalcularTotal(self):
        for ArticulosCarrito in self._cant_articulos:
            precio_total += ArticulosCarrito.get.total[indice]
            
        
    def ObtenerCantidadArticulos(self):
        print(self._cant_articulos)
        
    def VerificarClienteFrecuente(self):