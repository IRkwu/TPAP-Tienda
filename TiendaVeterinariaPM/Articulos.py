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
        
        
# Ejemplo
#articulo1 = Articulos("Cama Iglu", "Gato", "A12", "Catto", 28900, 30, "Cama para gatos con forma de Iglu", "Camas", 130000, 3)
#print(articulo1.get_stock())
#articulo1.NotificacionEstadoCritico()
#articulo1.AgregarStock(10)
#print(articulo1.get_stock())
#articulo1.NotificacionEstadoCritico()
#articulo1.RetirarStock(5)
#print(articulo1.get_stock())
#articulo1.NotificacionEstadoCritico()
#articulo1.set_stock(2)
#print(articulo1.get_stock())
#articulo1.NotificacionEstadoCritico()
