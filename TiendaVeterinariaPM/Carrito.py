from Articulos import Articulos
from Articulos import ListaArticulos
from Envio import Envio


class Carrito():

    def __init__(self, ArticulosCarrito, precio_total, cliente_frecuente=False):
        self.__ArticulosCarrito = []
        self.__ArticulosCarrito = [ListaArticulos[indice]
                                   for indice in ArticulosCarrito]
        self.__precio_total = precio_total
        self.__cantidad_articulos = len(self.__ArticulosCarrito)
        self.__cliente_frecuente = cliente_frecuente

    # Agrega el articulo según la lista de articulos, ej: el primer articulo de la lista es cama iglu, en indice 0 añade cama iglu
    def AgregarArticuloUnidad(self, indice):
        if Carrito.VerificarStockArticulos(self, indice) == False:
            print("¡¡¡Error!!! Producto sin Stock")
        else:
            self.__ArticulosCarrito.append(ListaArticulos[indice])
            self.__ArticulosCarrito[-1].set_precio_por_lote(0)
            ListaArticulos[indice].RetirarStock(1)
            print("Producto agregado al carrito:",
                  ListaArticulos[indice].get_nombre())
            print("El precio del producto es:",ListaArticulos[indice].get_precio_por_unidad())

    def AgregarArticuloLote(self, indice):
        if Carrito.VerificarStockArticulosLote(self, indice) == False:
            print("¡¡¡Error!!! Producto sin Stock")
        else:
            self.__ArticulosCarrito.append(ListaArticulos[indice])
            self.__ArticulosCarrito[-1].set_precio_por_unidad(0)
            ListaArticulos[indice].RetirarStock(5)
            print("Producto agregado al carrito:",
                  ListaArticulos[indice].get_nombre())
            print("El precio del producto es:",ListaArticulos[indice].get_precio_por_lote())
    # Elimina el articulo del carrito según la posición en que fue añadida, ej: para eliminar el primer producto del carrito el indice sería 0

    def EliminarArticulo(self, indice):
        articulo = self.__ArticulosCarrito[indice]
        print("Producto eliminado del carrito:", articulo.get_nombre())
        self.__ArticulosCarrito.pop(indice)

    # Verifica que el stock de articulos no sea 0, ya que si el stock es 0 no se puede agregar al carrito
    def VerificarStockArticulos(self, indice):
        articulo = ListaArticulos[indice]
        if articulo.get_stock() == 0:
            print("No hay stock del producto:", articulo.get_nombre())
            return False
        
    def VerificarStockArticulosLote(self, indice):
        articulo = ListaArticulos[indice]
        if articulo.get_stock() <= 4:
            print("No hay stock del producto:", articulo.get_nombre())
            return False
        
        

    # Calcula el precio total y verifica si se aplica o no el costo de envio
    def CalcularTotal(self):

        self.__precio_total = 0
        for articulo in self.__ArticulosCarrito:
            self.__precio_total += (articulo.get_precio_por_unidad() +
                                    articulo.get_precio_por_lote())

        if self.__cliente_frecuente:
            self.__precio_total = self.__precio_total*0.95

        costo_envio = Envio.CalcularDescuentoEnvio(self.__precio_total)

        return int(self.__precio_total)

    # Funcion para obtener la cantidad de articulos
    def ObtenerCantidadArticulos(self):
        self.__cantidad_articulos = len(self.__ArticulosCarrito)
        print("La cantidad de Artículos es:", self.__cantidad_articulos)

    # Verificacion de cliente frecuente
    def VerificarClienteFrecuente(self):
        return self.__cliente_frecuente
        # Hay que hacer la verificacion con el historial

    # Funcion poder imprimir los articulos en la Boleta
    def MostrarArticulosBoleta(self):
        contador = 1
        articulos = []
        if len(self.__ArticulosCarrito) == 0:
            print("El Carrito está vacio")
        for articulo in self.__ArticulosCarrito:
            articulos.append("[Art:" + str(contador) + "] " + articulo.get_nombre() +
                             " --- [Precio:" + str(articulo.get_precio_por_unidad()+articulo.get_precio_por_lote()) + "]")
            contador += 1
        return articulos

    # Funcion para imprimir los articulos en el Carrito
    def MostrarArticulosCarrito(self):
        contador = 1
        if len(self.__ArticulosCarrito) == 0:
            print("El Carrito está vacio")
        else:
            print("Lista de articulos del Carrito: ")
            for articulo in self.__ArticulosCarrito:
                # sep='' se usa para que no haya espacio despues de la ,
                print("[Art:", contador, "] ", articulo.get_nombre(),
                      " --- [Precio:", articulo.get_precio_por_unidad()+articulo.get_precio_por_lote(), "]", sep='')
                contador += 1

     # Vaciar el carrito para poder volver a agregar productos de un nuevo cliente

    def VaciarCarrito(self):
        self.__ArticulosCarrito = []
        self.__precio_total = 0
        self.__cantidad_articulos = 0
        print("El carrito ha sido vaciado")


# Inicializa el carrito del cliente vacio, sin productos y precio 0
Carrito_Cliente = Carrito([], 0)


# PRUEBAS
# mi_carrito = Carrito([2], 0, True)

# mi_carrito.MostrarArticulosCarrito()
# mi_carrito.EliminarArticulo(0)
# mi_carrito.MostrarArticulosCarrito()
# mi_carrito.AgregarArticulo(2)
# mi_carrito.CalcularTotal()
