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
        
    def NotificacionEstadoCritico(self):
        if self.__stock < self.__limite_critico:
            print("El artículo:",self.__nombre,"está en el limite crítico")

    def GuardarCSV(lista_articulos):
        with open('Archivos de Datos\ListaArticulos.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nombre', 'Mascota', 'ID', 'Marca', 'Precio por unidad', 'Stock', 'Descripción', 'Categoría', 'Precio por lote', 'Límite crítico'])
            for articulo in lista_articulos:
                writer.writerow([articulo.get_nombre(), articulo.get_mascota(), articulo.get_id(), articulo.get_marca(), articulo.get_precio_por_unidad(), articulo.get_stock(), articulo.get_descripcion(), articulo.get_categoria(), articulo.get_precio_por_lote(), articulo.get_limite_critico()])

    def CargarCSV(ruta_archivo):
        lista_articulos = []
        with open(ruta_archivo, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico = row
                articulo = Articulos(nombre, mascota, id, marca, int(precio_por_unidad), int(stock), descripcion, categoria, int(precio_por_lote), int(limite_critico))
                lista_articulos.append(articulo)
        return lista_articulos

    def AgregarArticulo(nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico):
        articulo = Articulos(nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico)
        ListaArticulos.append(articulo)
        GuardarCSV(ListaArticulos)
        print("El artículo se agregó correctamente a la lista.")

    def MostrarListaArticulos():
        contador=1
        for articulo in ListaArticulos:
            print("[Art:", contador,"]",
                  "[Nombre]:", articulo.get_nombre(),
                  "[Mascota:]",articulo.get_mascota(),
                  "[ID]:",articulo.get_id(),"[Marca]:",
                  articulo.get_marca(),"[Precio Unidad]:",
                  articulo.get_precio_por_unidad(),"[Stock]:",
                  articulo.get_stock(),"\n[Descripcion]:",
                  articulo.get_descripcion(),"[Categoría]:",articulo.get_categoria(),
                  "[Precio Lote]:",articulo.get_precio_por_lote(),"[Limite Crítico]:",
                  articulo.get_limite_critico())
            contador += 1
            
#Cargar archivo CSV y llenar el arreglo de ListaArticulos
#ListaArticulos = Articulos.CargarCSV('Archivos de Datos\ListaArticulos.csv')

#Ejemplo mostrar articulos
#Articulos.MostrarListaArticulos()

#Ejemplo para guardar la lista de articulos, abajo
#GuardarCSV(ListaArticulos)

#Ejemplo ingresar nuevos articulos
#a1=input("Nombre:")
#a2=input("Mascota:")
#a3=input("ID:")
#a4=input("Marca")
#a5=input("Precio Unidad:")
#a6=input("Stock:")
#a7=input("Descripcion:")
#a8=input("Categoría:")
#a9=input("Precio Lote:")
#a10=input("Limite Crítico:")
#AgregarArticulo(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)