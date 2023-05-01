from PyQt5.QtWidgets import *
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import sys
import csv
from Articulos import *
from Cliente import *
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor





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

        
        botonClientes = qtw.QPushButton("Ingresar Clientes", clicked = lambda: self.Cambio(ventana3))
        self.layout().addWidget(botonClientes)
        self.show()

        botonProductos = qtw.QPushButton("Ingresar Productos", clicked = lambda: self.Cambio(ventana2))
        self.layout().addWidget(botonProductos)
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
        botonCrear.clicked.connect(self.cambioAtras)
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
        QMessageBox.information(None, "Éxito", "El cliente se agregó correctamente a la lista.")

       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana4):
        ventana3.show()
        self.hide()

#Listo
class ventanaEditarCliente(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear widgets
        self.resize(1280,500)
        self.setWindowTitle('Editar Clientes')
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.load_button = QPushButton("Cargar")
        self.load_button.clicked.connect(self.cargar_datos)
        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.guardar_datos)
        self.delete_button = QPushButton("Eliminar")
        self.back_button = QPushButton("Atras")
        self.back_button.clicked.connect(self.cambioAtras)
        self.delete_button.clicked.connect(self.eliminar_datos)
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.buscar_cliente)
        self.search_edit = QLineEdit()
       


        # Crear layout vertical y agregar widgets
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.search_edit)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.back_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(table_layout)
        main_layout.addLayout(button_layout)

        # Crear widget central
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def cargar_datos(self):

        # Limpiar la tabla antes de cargar nuevos datos
        self.table.clear()

        # Abrir el archivo CSV
        with open('Archivos de Datos\ListadeClientes.csv', "r", newline="") as file:
            # Crear un objeto lector CSV
            reader = csv.reader(file)

            # Leer los datos y agregarlos a la tabla
            for i, row in enumerate(reader):
                self.table.insertRow(i)
                for j, value in enumerate(row):
                    item = QTableWidgetItem(value)
                    self.table.setItem(i, j, item)


    def guardar_datos(self):

        # Abrir el archivo CSV en modo escritura
        with open('Archivos de Datos\ListadeClientes.csv', "w", newline="") as file:
            # Crear un objeto escritor CSV
            writer = csv.writer(file)

            # Escribir los datos de la tabla en el archivo
            for i in range(self.table.rowCount()):
                row = []
                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)
                    row.append(item.text())
                writer.writerow(row)


    def eliminar_datos(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()

        # Eliminar la fila seleccionada
        if selected_row != -1:
            self.table.removeRow(selected_row)


    def buscar_cliente(self):

        # Obtener el ID del cliente a buscar
        client_id = self.search_edit.text()

        # Buscar al cliente en la tabla
        for i in range(self.table.rowCount()):
            item = self.table.item(i, 0)  # La columna 0 contiene los ID de los clientes

            if item and item.text() == client_id:

                # Subrayar toda la fila del cliente en azul

                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)

                    if item:
                        item.setBackground(QColor(Qt.blue))
            

                # Desplazar la vista de la tabla hacia la fila correspondiente
                self.table.scrollToItem(item, QAbstractItemView.PositionAtTop)
                break


         #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana):
        ventana3.show()
        self.hide()

#Esta son las funciones para gestionar los clientes



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
        mascotaLabel = qtw.QLabel("Mascota: ")
        hbox.addWidget(mascotaLabel)
        self.mascotaLineEdit = qtw.QLineEdit()
        self.mascotaLineEdit.setPlaceholderText("Ingrese el nombre de la especie")
        hbox.addWidget(self.mascotaLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        idLabel = qtw.QLabel("ID: ")
        hbox.addWidget(idLabel)
        self.idLineEdit = qtw.QLineEdit()
        self.idLineEdit.setPlaceholderText("Ingrese el ID del producto")
        hbox.addWidget(self.idLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        marcaLabel = qtw.QLabel("Marca: ")
        hbox.addWidget(marcaLabel)
        self.marcaLineEdit = qtw.QLineEdit()
        self.marcaLineEdit.setPlaceholderText("Ingrese la marca del producto")
        hbox.addWidget(self.marcaLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        precioLabel = qtw.QLabel("Precio: ")
        hbox.addWidget(precioLabel)
        self.precioLineEdit = qtw.QLineEdit()
        self.precioLineEdit.setPlaceholderText("Ingrese el precio del producto")
        hbox.addWidget(self.precioLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        stockLabel = qtw.QLabel("Stock: ")
        hbox.addWidget(stockLabel)
        self.stockLineEdit = qtw.QLineEdit()
        self.stockLineEdit.setPlaceholderText("Ingrese el stock disponible del producto")
        hbox.addWidget(self.stockLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        descripcionLabel = qtw.QLabel("Descripcion: ")
        hbox.addWidget(descripcionLabel)
        self.descripcionLineEdit = qtw.QLineEdit()
        self.descripcionLineEdit.setPlaceholderText("Ingrese una descripcion del producto")
        hbox.addWidget(self.descripcionLineEdit)
        self.layout().addLayout(hbox)

        hbox = qtw.QHBoxLayout()
        categoriaLabel = qtw.QLabel("Categoria: ")
        hbox.addWidget(categoriaLabel)
        self.layout().addLayout(hbox)
        self.categoriaComboBox = qtw.QComboBox()
        self.categoriaComboBox.addItems(["Artículos de aseo", "Prendas de ropa", "Juguetes de relajación", "Alimento y sumplementos", "Accesorios de paseo", "Juguetes de entretenimiento", "Nidos y muebles", "Cestas"])
        hbox.addWidget(self.categoriaComboBox)
       
        hbox = qtw.QHBoxLayout()
        precioLoteLabel = qtw.QLabel("Precio por lote: ")
        hbox.addWidget(precioLoteLabel)
        self.precioLoteLineEdit = qtw.QLineEdit()
        self.precioLoteLineEdit.setPlaceholderText("Ingrese el precio por lote del producto")
        hbox.addWidget(self.precioLoteLineEdit)
        self.layout().addLayout(hbox)   
        
        hbox = qtw.QHBoxLayout()
        limiteCriticoLabel = qtw.QLabel("Limite Critico: ")
        hbox.addWidget(limiteCriticoLabel)
        self.limiteCriticoLineEdit = qtw.QLineEdit()
        self.limiteCriticoLineEdit.setPlaceholderText("Ingrese el limite critico que tendrá el producto")
        hbox.addWidget(self.limiteCriticoLineEdit)
        self.layout().addLayout(hbox)  
        
        botonCrear = qtw.QPushButton("Crear Producto")
        botonCrear.clicked.connect(self.agregar_articulos)
        botonCrear.clicked.connect(self.cambioAtras)
        self.layout().addWidget(botonCrear)

        botonBack = qtw.QPushButton("Atras", clicked = lambda: self.cambioAtras(ventana2))
        self.layout().addWidget(botonBack)
        
        #Cantidad de botones en la ventana

    def agregar_articulos(self):
        nombre = self.nombreLineEdit.text()
        mascota = self.mascotaLineEdit.text()
        id = self.idLineEdit.text()
        marca = self.marcaLineEdit.text()
        precio = self.precioLineEdit.text()
        stock = self.stockLineEdit.text()
        descripcion = self.descripcionLineEdit.text()
        categoria = self.categoriaComboBox.currentText()
        precioLote = self.precioLoteLineEdit.text()
        limiteCritico = self.limiteCriticoLineEdit.text()

        articulo = Articulos(nombre, mascota, id, marca, precio, stock, descripcion, categoria, precioLote, limiteCritico)
        articulo.AgregarArticulo(nombre, mascota, id, marca, precio, stock, descripcion, categoria, precioLote, limiteCritico)
        QMessageBox.information(None, "Éxito", "El artículo se agregó correctamente a la lista.")

        
       
    #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana8):
        ventana2.show()
        self.hide()

#Listo
class ventanaEditarProducto(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear widgets
        self.resize(1280,500)
        self.setWindowTitle('Editar Productos')
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.load_button = QPushButton("Cargar")
        self.load_button.clicked.connect(self.load_data)
        self.save_button = QPushButton("Guardar")
        self.save_button.clicked.connect(self.save_data)
        self.delete_button = QPushButton("Eliminar")
        self.back_button = QPushButton("Atras")
        self.back_button.clicked.connect(self.cambioAtras)
        self.delete_button.clicked.connect(self.delete_data)
        self.search_button = QPushButton("Buscar")
        self.search_button.clicked.connect(self.search_client)
        self.search_edit = QLineEdit()
       


        # Crear layout vertical y agregar widgets
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.table)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.load_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.delete_button)
        button_layout.addWidget(self.search_edit)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.back_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(table_layout)
        main_layout.addLayout(button_layout)

        # Crear widget central
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def load_data(self):
        # Limpiar la tabla antes de cargar nuevos datos
        self.table.clear()

        # Abrir el archivo CSV
        with open("Archivos de Datos/ListaArticulos.csv", "r", newline="") as file:
            # Crear un objeto lector CSV
            reader = csv.reader(file)

            # Leer los datos y agregarlos a la tabla
            for i, row in enumerate(reader):
                self.table.insertRow(i)
                for j, value in enumerate(row):
                    item = QTableWidgetItem(value)
                    self.table.setItem(i, j, item)


    def save_data(self):
        # Abrir el archivo CSV en modo escritura
        with open("Archivos de Datos/ListaArticulos.csv", "w", newline="") as file:
            # Crear un objeto escritor CSV
            writer = csv.writer(file)

            # Escribir los datos de la tabla en el archivo
            for i in range(self.table.rowCount()):
                row = []
                for j in range(self.table.columnCount()):
                    item = self.table.item(i, j)
                    if item is not None:
                        row.append(item.text())
                    else:
                        row.append('')
                writer.writerow(row)


    def delete_data(self):
        # Obtener la fila seleccionada
        selected_row = self.table.currentRow()

        # Eliminar la fila seleccionada
        if selected_row != -1:
            self.table.removeRow(selected_row)

    def search_client(self):
        # Obtener el ID del cliente a buscar
        client_id = self.search_edit.text()

        # Buscar al cliente en la tabla
        for i in range(self.table.rowCount()):

            item = self.table.item(i, 0)  # La columna 0 contiene los ID de los clientes

            if item and item.text() == client_id:

                # Subrayar toda la fila del cliente en azul
                for j in range(self.table.columnCount()):

                    item = self.table.item(i, j)

                    if item:

                        item.setBackground(QColor(Qt.blue))
            

                # Desplazar la vista de la tabla hacia la fila correspondiente
                self.table.scrollToItem(item, QAbstractItemView.PositionAtTop)
                break

         #Funcion que simula el cambio (oculta la ventana)
    def cambioAtras(self, ventana9):
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

    #Ventanas Productos
    ventana8 = ventanaCrearProducto()
    ventana9 = ventanaEditarProducto()

    sys.exit(app.exec_())
