import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qc
from uiListaProd import uiListaP
import VerificarStock
import loginUser


class listaProd(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventana = uiListaP()
        self.ventana.setupUi(self)
        self.actualizarLista()
        self.lista = self.ventana.listaProductos
        self.ventana.btnRevisarProd.setEnabled(False)
        self.ventana.btnRevisarProd.clicked.connect(self.Ingresar)
        self.lista.itemSelectionChanged.connect(self.filaSel)
        self.ventana.btnCerrar.clicked.connect(lambda: self.cerrar())
        self.ventana1 = loginUser.login()
    
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
        
            # Crear etiqueta cuadrada verde
            etiqueta = qtw.QTableWidgetItem()
            if int(prod[9]) >= int(prod[5]):
                etiqueta.setBackground(qtg.QColor('red'))
            else:
                etiqueta.setBackground(qtg.QColor('green'))
            etiqueta.setTextAlignment(qc.Qt.AlignCenter)
            etiqueta.setFlags(qc.Qt.ItemIsEnabled)
            self.ventana.listaProductos.setItem(i, 5, etiqueta)
            

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
        
    def filaSel(self):
        self.fila = self.lista.selectedIndexes()
        if self.fila:
            self.ventana.btnRevisarProd.setEnabled(True)
            self.seleccionItem = self.lista.currentRow()
        else:
            self.ventana.btnRevisarProd.setEnabled(False)
        
    def Ingresar(self):
        self.VerificarStock = VerificarStock.Verificar(self.seleccionItem, self.cont)
        self.VerificarStock.actualizar()
        self.VerificarStock.show()
        self.hide()
    
    def cerrar(self):
        self.ventana1.show()
        self.hide()
      
      
  