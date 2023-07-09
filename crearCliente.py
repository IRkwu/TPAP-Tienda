import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
from uiLoginUser import uiLogin
import csv
import PyQt5.QtWidgets as qtw
from uiCrearCliente import uiCrearCliente
import Cliente

class crearCliente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiCrearCliente()
        self.ventana.setupUi(self)
        self.ventana.btnRegistrar.clicked.connect(Cliente.Cliente.AgregarClientes)