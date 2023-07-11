from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import sys
import csv
#import PyQt5.QtWidgets as qtw
from uiCrearProducto import uiCrearProducto
from Articulos import *
from uiListaProductos import uiListaProductos

class crearProducto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiCrearProducto()
        self.ventana.setupUi(self)
        self.ventana.btnRegistrar.clicked.connect(self.agregar_articulos)
        self.ventana.btnAtras.clicked.connect(self.Atras)
    
        regex = QRegExp("[a-zA-Z]+")
        regexNumeros = QRegExp("[0-9]+")
        
        self.validador = QRegExpValidator(regex)
        self.validadorNumeros = QRegExpValidator(regexNumeros)
        
        self.ventana.inputNombre.setValidator(self.validador)
        self.ventana.inputMascota.setValidator(self.validador)
        self.ventana.inputPrecio.setValidator(self.validadorNumeros)
        self.ventana.inputStock.setValidator(self.validadorNumeros)
        self.ventana.inputPrecioLote.setValidator(self.validadorNumeros)
        self.ventana.inputLimCritico.setValidator(self.validadorNumeros)
    
    def agregar_articulos(self):
        nombre = self.ventana.inputNombre.text()
        mascota = self.ventana.inputMascota.text()
        id = self.ventana.inputID.text()
        marca = self.ventana.inputMarca.text()
        precio = self.ventana.inputPrecio.text()
        stock = self.ventana.inputStock.text()
        descripcion = self.ventana.inputDescripcion.toPlainText()
        categoria = self.ventana.comboBoxC.currentText()
        precioLote = self.ventana.inputPrecioLote.text()
        limiteCritico = self.ventana.inputLimCritico.text()
        
        if nombre == '' or id == '' or mascota == '' or id == '' or marca == '' or precio == '' or stock == '' or descripcion == '' or precioLote == '' or limiteCritico == '':
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos requeridos.")
            return

        articulo = Articulos(nombre, mascota, id, marca, precio, stock, descripcion, categoria, precioLote, limiteCritico)
        articulo.AgregarArticulo(nombre, mascota, id, marca, precio, stock, descripcion, categoria, precioLote, limiteCritico)
        
    def verificar_entrada(self, texto):
        pos = 0
        estado = self.validador.validate(texto, pos)

        if estado == QRegExpValidator.Acceptable:
            self.label_error.setText("")

        elif estado == QRegExpValidator.Invalid:
            self.label_error.setText("Valor inválido")
        
    def Atras(self):
        self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
        self.uiVentanaActual.close()
        uiListaProductos().show()
        
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     ventanaMain = crearProducto()
#     ventanaMain.show()
#     app.exec_()