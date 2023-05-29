import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
import sys
from uiListaProd import uiListaP
import VerificarStock


class listaProd(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventana = uiListaP()
        self.ventana.setupUi(self)
        self.actualizarLista()
        self.lista = self.ventana.listaProductos
        self.ventana.btnRevisarProd.clicked.connect(self.Ingresar)
    
    def actualizarNombre(self):
        self.ventana.labelUsuarioEnLogin.setText(self.usuario[1])
    
    def actualizarLista(self):
        with open('Archivos de Datos/ListaArticulos.csv') as f:
            lector = csv.reader(f)
            next(lector)
            self.productos = [row for row in lector]

        contFilas = len(self.productos)
        self.ventana.listaProductos.setRowCount(contFilas)

        for i, prod in enumerate(self.productos):
            id = qtw.QTableWidgetItem(prod[2])
            self.ventana.listaProductos.setItem(i, 0, id)

            nombreP = qtw.QTableWidgetItem(prod[0])
            self.ventana.listaProductos.setItem(i, 1, nombreP)
            
            categoria = qtw.QTableWidgetItem(prod[7])
            self.ventana.listaProductos.setItem(i, 2, categoria)

            marca = qtw.QTableWidgetItem(prod[3])
            self.ventana.listaProductos.setItem(i, 3, marca)
            
            precio = qtw.QTableWidgetItem("$" + prod[4])
            self.ventana.listaProductos.setItem(i, 4, precio)

        with open('Archivos de Datos/ListaUsuarios.csv', 'r', encoding="utf-8") as r:
            l = csv.reader(r, delimiter=",")
            next(l)

            i = 0
            for lis in l:
                if i == self.cont:
                    self.usuario = lis
                    break
                i += 1
        self.ventana.labelUsuarioEnLogin.setText(self.usuario[1])
        
        
    def Ingresar(self):
        self.VerificarStock = VerificarStock.Verificar(cont=self.cont)
        self.VerificarStock.actualizar()
        self.VerificarStock.show()
        self.hide()    
      
      
  