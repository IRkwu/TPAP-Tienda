class Boleta:
    def __init__(self, nombre_vendedor, nombre_cliente, fecha, productos, total, costo_envio):
        self.__nombre_vendedor = nombre_vendedor
        self.__nombre_cliente = nombre_cliente
        self.__fecha = fecha
        self.__productos = productos
        self.__total = total
        self.__costo_envio = costo_envio
        
        # Getters
    def get_nombre_vendedor(self):
        return self.__nombre_vendedor
    
    def get_nombre_cliente(self):
        return self.__nombre_cliente
    
    def get_fecha(self):
        return self.__fecha
    
    def get_productos(self):
        return self.__productos
    
    def get_total(self):
        return self.__total
    
    def get_costo_envio(self):
        return self.__costo_envio
    
    # Setters
    def set_nombre_vendedor(self, nombre_vendedor):
        self.__nombre_vendedor = nombre_vendedor
        
    def set_nombre_cliente(self, nombre_cliente):
        self.__nombre_cliente = nombre_cliente
        
    def set_fecha(self, fecha):
        self.__fecha = fecha
        
    def set_productos(self, productos):
        self.__productos = productos
        
    def set_total(self, total):
        self.__total = total
        
    def set_costo_envio(self, costo_envio):
        self.__costo_envio = costo_envio
        
    def imprimir_boleta(self):
        print("================================")
        print("        BOLETA DE VENTA")
        print("================================")
        print("Cliente:",self.__nombre_cliente)
        print("Productos:",self.__productos)
        print("Costo de envío: $:",self.__costo_envio)
        print("Total: $",self.__total)
        print("================================")
        
        
#Ejemplo
#boleta1 = Boleta("Juan", "Maria", "2023-04-04", ["Producto 1, Producto 2"], 28900, 0)
#boleta1.imprimir_boleta()