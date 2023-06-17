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
        self.p = False
        
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
            if int(prod[9]) >= int(prod[5]):
                etiqueta = qtw.QTableWidgetItem("Stock es igual o por debajo de: " + prod[9])
                etiqueta.setBackground(qtg.QColor('red'))
                self.p = True
            else:
                etiqueta = qtw.QTableWidgetItem()
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
    
    def ventWarning(self):
        if self.p == True:
            qtw.QMessageBox.warning(self,"¡Atención! Hay articulos con bajo Stock.","Algunos articulos tienen bajo stock, porfavor, revise los colores de las casillas, si están en rojo, significa que tienen bajo stock.")
        
    def Ingresar(self):
        self.VerificarStock = VerificarStock.Verificar(self.seleccionItem, self.cont)
        self.VerificarStock.actualizar()
        self.VerificarStock.show()
        self.hide()
    
    def cerrar(self):
        self.ventana1.show()
        self.hide()
      
      
  