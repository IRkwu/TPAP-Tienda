from Articulos import Articulos

ListaArticulos = Articulos.CargarCSV('Archivos de Datos\ListaArticulos.csv')

class Carrito():
    
    def __init__(self, ArticulosCarrito, precio_total, cliente_frecuente=False):
        self.__ArticulosCarrito = []
        self.__ArticulosCarrito = [ListaArticulos[indice] for indice in ArticulosCarrito]
        self.__precio_total = precio_total
        self.__cantidad_articulos = len(self.__ArticulosCarrito)
        self.__cliente_frecuente = cliente_frecuente
        
    #Agrega el articulo según la lista de articulos, ej: el primer articulo de la lista es cama iglu, en indice 0 añade cama iglu
    def AgregarArticulo(self, indice):
        if Carrito.VerificarStockArticulos(self, indice) == False:
            print("¡¡¡Error!!! Producto sin Stock")
        else:
            self.__ArticulosCarrito.append(ListaArticulos[indice])
            print("Producto agregado al carrito:", ListaArticulos[indice].get_nombre())

    #Elimina el articulo del carrito según la posición en que fue añadida, ej: para eliminar el primer producto del carrito el indice sería 0
    def EliminarArticulo(self, indice):
        articulo = self.__ArticulosCarrito[indice]
        print("Producto eliminado del carrito:", articulo.get_nombre())
        self.__ArticulosCarrito.pop(indice)
        
    def VerificarStockArticulos(self, indice):
        articulo = ListaArticulos[indice]
        if articulo.get_stock() == 0:
            print("No hay stock del producto:", articulo.get_nombre())
            return False
        else:
            print("El stock disponible es:", articulo.get_stock())
            return True
        
    def CalcularTotal(self):
        self.__precio_total = 0
        for articulo in self.__ArticulosCarrito:
            self.__precio_total += articulo.get_precio_por_unidad()
        if self.__cliente_frecuente == True:
            self.__precio_total = self.__precio_total*0.95
        print("El precio total del carrito es:",self.__precio_total)
        
    def ObtenerCantidadArticulos(self):
        self.__cantidad_articulos = len(self.__ArticulosCarrito)
        print("La cantidad de Artículos es:",self.__cantidad_articulos)
        
    def VerificarClienteFrecuente(self):
        return self.__cliente_frecuente
        #Hay que hacer la verificacion con el historial

    def MostrarArticulosCarrito(self):
        if len(self.__ArticulosCarrito) == 0:
            print("El Carrito está vacio")
        for articulo in self.__ArticulosCarrito:
            print("Nombre: " + articulo.get_nombre())

#Ejemplo de las funciones
#mi_carrito = Carrito([2], 0, True)

#mi_carrito.MostrarArticulosCarrito()
#mi_carrito.EliminarArticulo(0)
#mi_carrito.MostrarArticulosCarrito()