import csv

class Articulos:
    def __init__(self, nombre, mascota, id, marca, precio_por_unidad:int, stock:int, descripcion, categoria, precio_por_lote:int, limite_critico:int):
        self.__nombre = nombre
        self.__mascota = mascota
        self.__id = id
        self.__marca = marca
        self.__precio_por_unidad = precio_por_unidad
        self.__stock = stock
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__precio_por_lote = precio_por_lote
        self.__limite_critico = limite_critico
        
        
    # Getters
    def get_nombre(self):
        return self.__nombre
    
    def get_mascota(self):
        return self.__mascota
    
    def get_id(self):
        return self.__id
    
    def get_marca(self):
        return self.__marca
    
    def get_precio_por_unidad(self):
        return self.__precio_por_unidad
    
    def get_stock(self):
        return self.__stock
    
    def get_descripcion(self):
        return self.__descripcion
    
    def get_categoria(self):
        return self.__categoria
    
    def get_precio_por_lote(self):
        return self.__precio_por_lote
    
    def get_limite_critico(self):
        return self.__limite_critico
    
    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_mascota(self, mascota):
        self.__mascota = mascota
    
    def set_id(self, id):
        self.__id = id
    
    def set_marca(self, marca):
        self.__marca = marca
    
    def set_precio_por_unidad(self, precio_por_unidad):
        self.__precio_por_unidad = precio_por_unidad
    
    def set_stock(self, stock):
        self.__stock = stock
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def set_categoria(self, categoria):
        self.__categoria = categoria
    
    def set_precio_por_lote(self, precio_por_lote):
        self.__precio_por_lote = precio_por_lote
        
    def set_limite_critico(self, limite_critico):
        self.__limite_critico = limite_critico
        
    def AgregarStock(self, cantidad):
        self.__stock = self.__stock + cantidad
        
    def RetirarStock(self, cantidad):
        self.__stock = self.__stock - cantidad


    def GuardarCSV(self, lista_articulos):
        with open('Archivos de Datos\ListaArticulos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nombre', 'Mascota', 'ID', 'Marca', 'Precio por unidad', 'Stock', 'Descripción', 'Categoría', 'Precio por lote', 'Límite Crítico'])
            for Articulo in lista_articulos:
                writer.writerow([Articulo.get_nombre(), Articulo.get_mascota(), Articulo.get_id(), Articulo.get_marca(), Articulo.get_precio_por_unidad(), Articulo.get_stock(), Articulo.get_descripcion(), Articulo.get_categoria(), Articulo.get_precio_por_lote(), Articulo.get_limite_critico()])

    def CargarCSV(self, ruta_archivo):
        lista_articulos = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            try:
                header = next(reader)
            except StopIteration:
                return lista_articulos
            for row in reader:
                if len(row) > 0:
                    nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico= row
                    articulo = Articulos(nombre, mascota, id, marca, int(precio_por_unidad), int(stock), descripcion, categoria, int(precio_por_lote), int(limite_critico))
                    lista_articulos.append(articulo)
        return lista_articulos

    def AgregarArticulo(self, nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico):
        articulo = Articulos(nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico)
        ListaArticulos.append(articulo)
        self.GuardarCSV(ListaArticulos)

#Cargar archivo CSV y llenar el arreglo de Articulos
ListaArticulos = Articulos.CargarCSV(None,
                                     'Archivos de Datos\ListaArticulos.csv')

def MostrarListaArticulos():
    contador=1
    for articulo in ListaArticulos:
        print("Articulo:", contador,"\n[Nombre]:", articulo.get_nombre(),"[Mascota:]",articulo.get_mascota(),"[ID]:",articulo.get_id(),"[Marca]:",articulo.get_marca(),"[Precio Unidad]:",int(articulo.get_precio_por_unidad()),"[Stock]:",int(articulo.get_stock()),"[Descripcion]:",articulo.get_descripcion(),"[Categoría]:",articulo.get_categoria(),"[Precio Lote]:",int(articulo.get_precio_por_lote()), int(articulo.get_limite_critico()))
        contador += 1

