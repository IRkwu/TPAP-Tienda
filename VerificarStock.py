import csv
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import PyQt5.QtWidgets as qtw
import sys
from UiVerificar import Ui_VerificarProd
import listaProd
from csvArchivo import csvArch
import uiVentEmer

class Emergente(QMainWindow):
    def __init__(self):
           super().__init__()
           self.vent = uiVentEmer.uiVentEm()
           self.vent.setupUi(self)
           
    def closeEvent(self, event):
        event.ignore()

class Verificar(QMainWindow):
        def __init__(self, cont, usuario):
           super().__init__()
           p = True
           self.cont = cont
           self.usuario = usuario
           self.ventana = Ui_VerificarProd()
           self.ventana.setupUi(self)
           self.vent = listaProd.listaProd(self.usuario)
           self.ventana.btnAtras.clicked.connect(lambda: self.Volver(self.vent))
           self.ventanaEm = Emergente()
           self.ventana.botonAgregar.clicked.connect(lambda: self.agregar())
           self.ventanaEm.vent.btnGuardar.clicked.connect(lambda: self.guardarStock(self.ventanaEm))
           

        def actualizar(self):
                   with open('Archivos de Datos/ListaArticulos.csv', "r", encoding="ISO 8859-1") as r:
                    lector = csv.reader(r, delimiter=",")
                    next(lector)
                    i = 0
                    for l in lector:
                        i = (i+1)
                        if i == (self.cont+1):
                            self.Producto = l

                    
                    self.ventana.labelid.setText(str(self.Producto[2]))
                    self.ventana.labelNombre.setText(str(self.Producto[0]))
                    self.ventana.labelMascota.setText(str(self.Producto[1]))
                    self.ventana.labelMarca.setText(str(self.Producto[3]))
                    self.ventana.labelCategoria.setText(str(self.Producto[7]))
                    self.ventana.labelPrecio.setText(str(self.Producto[4]))
                    self.ventana.labelPrecioLote.setText(str(self.Producto[8]))
                    self.ventana.labelStockEditable.setVisible(True)
                    self.ventana.labelStockEditable.setText(str(self.Producto[5]))
        
        def agregar(self):
            self.setEnabled(False)
            self.ventanaEm.vent.spinBox.setValue(1)
            self.ventanaEm.vent.spinBox.setMinimum(1)
            self.ventanaEm.vent.spinBox.setMaximum(99)
            self.ventanaEm.show()
        
        def guardarStock(self, vent):
            stock = self.ventanaEm.vent.spinBox.value()
            stockFinal = int(self.Producto[5]) + stock
            csvArch.modificar("Archivos de Datos/ListaArticulos.csv", self.cont, 5, stockFinal)
            vent.hide()
            self.actualizar()
            self.setEnabled(True)
   
           
       
        def Volver(self, ventana):
            ventana.actualizarNombre()
            ventana.actualizarLista()
            ventana.show()
            self.hide()