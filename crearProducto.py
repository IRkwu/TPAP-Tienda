import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
import csv
import PyQt5.QtWidgets as qtw
from uiCrearProducto import uiCrearProducto
import Articulos
import uiListaProductos

class crearProducto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiCrearProducto()
        self.ventana.setupUi(self)
        self.ventana.btnRegistrar.clicked.connect(self.Guardar)
    #   self.ventana.btnAtras.clicked.connect(self.Atras)
    
    def Guardar(self):
        Articulos.Articulos.AgregarArticulo
        uiListaProductos.uiListaProductos.show()
        self.close()
        
    #def Atras(self):
    #    ventana.show()
    #    self.close()