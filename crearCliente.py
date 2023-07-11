import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
import csv
import PyQt5.QtWidgets as qtw
from uiCrearCliente import uiCrearCliente
import Cliente
import uiMenu

class crearCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiCrearCliente()
        self.ventana.setupUi(self)
        self.ventana.btnRegistrar.clicked.connect(self.Guardar)
        
    def Guardar(self):
        Cliente.Cliente.AgregarClientes
        uiMenu.uiMenu().show()
        self.close()
        self.ventana.btnAtras.clicked.connect(self.Atras)
        
    def Atras(self):
        uiMenu.uiMenu().show()
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaMain = crearCliente()
    ventanaMain.show()
    app.exec_()