import pandas as pd

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
            
articulos = [
    Articulos("Cama Iglu", "Gato", "A12", "Catto", 28900, 30, "Cama para gatos con forma de Iglu", "Camas", 130050, 3),
    Articulos("Cama Dona", "Perro", "A13", "Doggo", 24900, 30, "Cama para perros con forma de dona", "Camas", 112050, 3),
]

def GuardarExcel(articulo):
    # Dataframe para articulo
    df = pd.DataFrame({
        'Nombre': [articulo.get_nombre() for articulo in articulos],
        'Mascota': [articulo.get_mascota() for articulo in articulos],
        'ID': [articulo.get_id() for articulo in articulos],
        'Marca': [articulo.get_marca() for articulo in articulos],
        'Precio por unidad': [articulo.get_precio_por_unidad() for articulo in articulos],
        'Stock': [articulo.get_stock() for articulo in articulos],
        'Descripcion': [articulo.get_descripcion() for articulo in articulos],
        'Categoria': [articulo.get_categoria() for articulo in articulos],
        'Precio por lote': [articulo.get_precio_por_lote() for articulo in articulos],
        'Limite critico': [articulo.get_limite_critico() for articulo in articulos]
    })

    # Guardado del dataframe
    writer = pd.ExcelWriter('Archivos de Datos\ListaArticulos.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Articulo')
    writer._save()
GuardarExcel(articulos)
