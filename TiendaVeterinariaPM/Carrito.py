from Articulos import *

class Carrito():
    
    def __init__(self, ArticulosCarrito, total_precio):
        self._ArticulosCarrito = [ArticulosCarrito]
        self._total_precio = total_precio
        self._cantidad_articulos = len(ArticulosCarrito)
        
    def AgregarArticulo(self, indice):
        if Carrito.VerificarStockArticulos(self, indice) == False:
            print("¡¡¡Error!!! Producto sin Stock")
        else:
            self.ArticulosCarrito.append(ListaArticulos[indice])
            
    def EliminarArticulo(self, indice):
        self._ArticulosCarrito.pop(indice)
        
    def VerificarStockArticulos(self, indice):
        if ListaArticulos[indice].get_stock() == 0:
            return False
        
    def CalcularTotal(self, indice):
        for ArticulosCarritos in self._cantidad_articulos:
            precio_total += ArticulosCarritos.get.total[indice]
        
    def ObtenerCantidadArticulos(self):
        print(self._cantidad_articulos)
        
    def VerificarClienteFrecuente():
        