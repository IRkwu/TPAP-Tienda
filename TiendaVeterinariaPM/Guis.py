from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import sys
import csv
from Cliente import *



#Esta es la Ventana Principal (menu)

class ventanaPrincipal(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.resize(250, 150)
        self.setWindowTitle("Tienda")

        texto = qtw.QLabel("Menu")
        texto.setAlignment(qtc.Qt.AlignCenter)
        texto.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto)


        #Cantidad de botones en la ventana

        botonProductos = qtw.QPushButton("Ingresar Productos", clicked = lambda: self.Cambio(ventana2))
        self.layout().addWidget(botonProductos)
        self.show()

        botonClientes = qtw.QPushButton("Ingresar Clientes", clicked = lambda: self.Cambio(ventana3))
        self.layout().addWidget(botonClientes)
        self.show()

        botonSalir = qtw.QPushButton("Salir", clicked=self.close)
        self.layout().addWidget(botonSalir)
        
        #Cantidad de botones en la ventana

    #Funcion que simula el cambio (oculta la ventana)
    def Cambio(self, ventana1):
        ventana1.show()
        self.hide()

#Esta es la ventana para gestionar los Productos


#Esta es la ventana para gestionar los Clientes

class ventanaClientes(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Tienda_3")
        texto2 = qtw.QLabel("Apartado Clientes")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Crear Cliente", clicked = lambda: self.cambioCrear(ventana4))
        self.layout().addWidget(botonCrear)

        botonEditar = qtw.QPushButton("Editar Cliente", clicked = lambda: self.cambioEditar(ventana5))
        self.layout().addWidget(botonEditar)

        botonEliminar = qtw.QPushButton("Eliminar Cliente", clicked = lambda: self.cambioEliminar(ventana6))
        self.layout().addWidget(botonEliminar)

        botonVer = qtw.QPushButton("Ver Cliente", clicked = lambda: self.cambioVer(ventana7))
        self.layout().addWidget(botonVer)

        botonBack = qtw.QPushButton("Volver al Menu", clicked = lambda: self.cambioAtras(ventana1))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

    
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana3):
        ventana3.show()
        self.hide()

    def cambioCrear(self,ventana3):
        ventana4.show()
        self.hide()

    def cambioEditar(self,ventana3):
        ventana5.show()
        self.hide()

    def cambioEliminar(self,ventana3):
        ventana6.show()
        self.hide()
    
    def cambioVer(self,ventana3):
        ventana7.show()
        self.hide()
    
#Listo
class ventanaCrearCliente(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Clientes")
        texto2 = qtw.QLabel("Crear Cliente")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana
        #Layout horizontal para el label y el cuadro de texto
        hbox = qtw.QHBoxLayout()
        idLabel = qtw.QLabel("ID: ")
        hbox.addWidget(idLabel)
        self.idLineEdit = qtw.QLineEdit()
        self.idLineEdit.setPlaceholderText("Ingrese el rut sin punto ni guión")
        hbox.addWidget(self.idLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        nombresLabel = qtw.QLabel("Nombres: ")
        hbox.addWidget(nombresLabel)
        self.nombresLineEdit = qtw.QLineEdit()
        self.nombresLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombresLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        apellidopLabel = qtw.QLabel("Apellido paterno: ")
        hbox.addWidget(apellidopLabel)
        self.apellidopLineEdit = qtw.QLineEdit()
        self.apellidopLineEdit.setPlaceholderText("Ingrese el apellido paterno")
        hbox.addWidget(self.apellidopLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        apellidomLabel = qtw.QLabel("Apellido materno: ")
        hbox.addWidget(apellidomLabel)
        self.apellidomLineEdit = qtw.QLineEdit()
        self.apellidomLineEdit.setPlaceholderText("Ingrese el apellido materno")
        hbox.addWidget(self.apellidomLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        generoLabel = qtw.QLabel("Género: ")
        hbox.addWidget(generoLabel)
        self.generoLineEdit = qtw.QLineEdit()
        self.generoLineEdit.setPlaceholderText("Ingrese el género")
        hbox.addWidget(self.generoLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        fnacimientoLabel = qtw.QLabel("Fecha de nacimiento: ")
        hbox.addWidget(fnacimientoLabel)
        self.fnacimientoLineEdit = qtw.QLineEdit()
        self.fnacimientoLineEdit.setPlaceholderText("DD/MM/AA")
        hbox.addWidget(self.fnacimientoLineEdit)
        self.layout().addLayout(hbox)
        
        
        hbox = qtw.QHBoxLayout()
        rutLabel = qtw.QLabel("Rut: ")
        hbox.addWidget(rutLabel)
        self.rutLineEdit = qtw.QLineEdit()
        self.rutLineEdit.setPlaceholderText("Ingrese el rut del cliente")
        hbox.addWidget(self.rutLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        emailLabel = qtw.QLabel("Email: ")
        hbox.addWidget(emailLabel)
        self.emailLineEdit = qtw.QLineEdit()
        self.emailLineEdit.setPlaceholderText("Correo electrónico")
        hbox.addWidget(self.emailLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        telefonoLabel = qtw.QLabel("Teléfono: ")
        hbox.addWidget(telefonoLabel)
        self.telefonoLineEdit = qtw.QLineEdit()
        self.telefonoLineEdit.setPlaceholderText("+56 00000000")
        hbox.addWidget(self.telefonoLineEdit)
        self.layout().addLayout(hbox)
        
        hbox = qtw.QHBoxLayout()
        domicilioLabel = qtw.QLabel("Domicilio: ")
        hbox.addWidget(domicilioLabel)
        self.domicilioLineEdit = qtw.QLineEdit()
        self.domicilioLineEdit.setPlaceholderText("Dirección")
        hbox.addWidget(self.domicilioLineEdit)
        self.layout().addLayout(hbox)
        
        botonCrear = qtw.QPushButton("Crear Cliente")
        botonCrear.clicked.connect(self.agregar_cliente)
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana3))
        self.layout().addWidget(botonBack)
        
    def agregar_cliente(self):
        id = self.idLineEdit.text()
        nombres = self.nombresLineEdit.text()
        apellidoPaterno = self.apellidopLineEdit.text()
        apellidoMaterno = self.apellidomLineEdit.text()
        genero = self.generoLineEdit.text()
        fechaNacimiento = self.fnacimientoLineEdit.text()
        rut = self.rutLineEdit.text()
        email = self.emailLineEdit.text()
        telefono = self.telefonoLineEdit.text()
        domicilio = self.domicilioLineEdit.text()

        cliente = Cliente(id, nombres, apellidoPaterno, apellidoMaterno, genero,
                          fechaNacimiento, rut, email, telefono, domicilio)
        cliente.AgregarClientes(id, nombres, apellidoPaterno, apellidoMaterno, genero,
                          fechaNacimiento, rut, email, telefono, domicilio)
        print("El cliente se agregó correctamente a la lista de clientes.")

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana4):
        ventana3.show()
        self.hide()

#Listo
class ventanaEditarCliente(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Clientes")
        texto2 = qtw.QLabel("Editar Cliente")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Listas para crear cliente
        
        #Layout horizontal para el label y el cuadro de texto
        

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Nombre: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Apellido Paterno: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Apellido Materno: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Genero: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Fecha de nacimiento: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Rut: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Email: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Telefono: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Domicilio: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)


        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Editar Cliente") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana3))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana5):
        ventana3.show()
        self.hide()


class ventanaEliminarCliente(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Clientes")
        texto2 = qtw.QLabel("Eliminar Clientes")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)
        
        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("ID: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el ID del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Eliminar Cliente") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana3))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana6):
        ventana3.show()
        self.hide()


class ventanaVerCliente(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Clientes")
        texto2 = qtw.QLabel("Ver Clientes")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana

        #Cuadro de texto para ingresar nombre
       
       
        #Layout horizontal para el label y el cuadro de texto
        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("ID: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el ID del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)


        botonCrear = qtw.QPushButton("Ver Clientes") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana3))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana7):
        ventana3.show()
        self.hide()

#Esta es la ventana para gestionar los Clientes



#Esta es la ventana para gestionar los productos

class ventanaProductos(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Tienda_2")
        texto2 = qtw.QLabel("Apartado Productos")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        
        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Crear Productos", clicked = lambda: self.cambioCrear(ventana8))
        self.layout().addWidget(botonCrear)

        botonEditar = qtw.QPushButton("Editar Productos", clicked = lambda: self.cambioEditar(ventana9))
        self.layout().addWidget(botonEditar)

        botonEliminar = qtw.QPushButton("Eliminar Productos", clicked = lambda: self.cambioEliminar(ventana10))
        self.layout().addWidget(botonEliminar)

        botonVer = qtw.QPushButton("Ver Productos", clicked = lambda: self.cambioVer(ventana11))
        self.layout().addWidget(botonVer)

        botonBack = qtw.QPushButton("Volver al Menu", clicked = lambda: self.cambioVolver(ventana1))
        self.layout().addWidget(botonBack)

        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioVolver(self, ventana2):
        ventana1.show()
        self.hide()
    
    def cambioCrear(self,ventana2):
        ventana8.show()
        self.hide()

    def cambioEditar(self,ventana2):
        ventana9.show()
        self.hide()

    def cambioEliminar(self,ventana2):
        ventana10.show()
        self.hide()
    
    def cambioVer(self,ventana2):
        ventana11.show()
        self.hide()
    
#Listo
class ventanaCrearProducto(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Productos")
        texto2 = qtw.QLabel("Crear Producto")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana

        #Layout horizontal para el label y el cuadro de texto
        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Nombre: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Mascota: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre de la especie")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("ID: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el ID del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Marca: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese la marca del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Precio: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el precio del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Stock: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el stock disponible del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Descripcion: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese una descripcion del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Categoria: ")
        hbox.addWidget(nombreLabel)
        self.layout().addLayout(hbox)
        self.categoriaComboBox = qtw.QComboBox()
        self.categoriaComboBox.addItems(["Artículos de aseo", "Prendas de ropa", "Juguetes de relajación", "Alimento y sumplementos", "Accesorios de paseo", "Juguetes de entretenimiento", "Nidos y muebles", "Cestas"])
        hbox.addWidget(self.categoriaComboBox)
       

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Precio por lote: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el precio por lote del producto")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)   
        

        botonCrear = qtw.QPushButton("Crear Producto") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana2))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana8):
        ventana2.show()
        self.hide()

#Listo
class ventanaEditarProducto(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Productos")
        texto2 = qtw.QLabel("Editar Producto")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana
         #Cantidad de las cosas a modificar
        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Nombre: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Mascota: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("ID: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Marca: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Precio: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Stock: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Descripcion: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Categoria: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        nombreLabel = qtw.QLabel("Precio por lote: ")
        hbox.addWidget(nombreLabel)
        self.nombreLineEdit = qtw.QLineEdit()
        self.nombreLineEdit.setPlaceholderText("Ingrese el nombre del cliente")
        hbox.addWidget(self.nombreLineEdit)
        self.layout().addLayout(hbox)



        botonCrear = qtw.QPushButton("Editar Producto") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana2))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana9):
        ventana2.show()
        self.hide()


class ventanaEliminarProducto(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Productos")
        texto2 = qtw.QLabel("Eliminar Producto")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Eliminar Producto") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana2))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana10):
        ventana2.show()
        self.hide()


class ventanaVerProducto(qtw.QWidget):
    
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Productos")
        texto2 = qtw.QLabel("Ver Producto")
        texto2.setAlignment(qtc.Qt.AlignCenter)

        texto2.setFont(qtg.QFont("Helvetica", 32))
        self.layout().addWidget(texto2)

        #Cantidad de botones en la ventana

        botonCrear = qtw.QPushButton("Ver Producto") #clicked = lambda: self.Cambio(ventana1))
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana2))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana11):
        ventana2.show()
        self.hide()





if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    ventana1 = ventanaPrincipal()
    ventana2 = ventanaProductos()
    ventana3 = ventanaClientes()

    #ventanas Clientes
    ventana4 = ventanaCrearCliente()
    ventana5 = ventanaEditarCliente()
    ventana6 = ventanaEliminarCliente()
    ventana7 = ventanaVerCliente()

    #Ventanas Productos
    ventana8 = ventanaCrearProducto()
    ventana9 = ventanaEditarProducto()
    ventana10 = ventanaEliminarProducto()
    ventana11 = ventanaVerProducto()

    sys.exit(app.exec_())

