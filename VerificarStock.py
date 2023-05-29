import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
import sys
from UiVerificar import Ui_VerificarProd
import listaProd
from csvArchivo import csvArch
class Verificar(QMainWindow):
        def __init__(self, cont):
           super().__init__()
           self.cont = cont
           contVerificar = 0 #Numero del producto
           self.contVerificar = contVerificar
           self.ventana = Ui_VerificarProd()
           self.ventana.setupUi(self)
           self.ventana.btnAtras.clicked.connect(self.Volver)
           self.ventana.botonAgregar.clicked.connect(self.agregarStock)
           self.ventana.botonGuardar.clicked.connect(self.guardarStock)
           
           
           print(self.contVerificar)

        def actualizar(self):
                   with open('Archivos de Datos/ListaArticulos.csv', "r", encoding="ISO 8859-1") as r:
                    lector = csv.reader(r, delimiter=",")
                    next(lector)
                    i = 0
                    for l in lector:
                        i = (i+1)
                        if i == (self.contVerificar+1):
                            Producto = l

                    
                    self.ventana.labelid.setText(str(Producto[2]))
                    self.ventana.labelNombre.setText(str(Producto[0]))
                    self.ventana.labelMascota.setText(str(Producto[1]))
                    self.ventana.labelMarca.setText(str(Producto[3]))
                    self.ventana.labelCategoria.setText(str(Producto[7]))
                    self.ventana.labelPrecio.setText(str(Producto[4]))
                    self.ventana.labelPrecioLote.setText(str(Producto[8]))
                    self.ventana.inputStock.setText(str(Producto[5]))
                    self.ventana.labelStockEditable.setVisible(True)
                    self.ventana.inputStock.setVisible(False)
                    self.ventana.labelStockEditable.setText(str(Producto[5]))
                    

        def agregarStock(self):
            self.ventana.labelStockEditable.setVisible(False)
            self.ventana.inputStock.setVisible(True)
        
        
        def guardarStock(self):
            nuevo_stock = self.ventana.inputStock.text()
            csvArch.modificar("Archivos de Datos/ListaArticulos.csv")
            self.actualizar()
   
        
           
       
        def Volver(self):
            self.listaProd = listaProd.listaProd(self.cont)
            self.listaProd.show()
            self.hide() 
            
                 
                
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaMain = Verificar()
    ventanaMain.show()
    app.exec_()                