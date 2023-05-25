import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
from uiLoginUser import uiLogin
import listaProd
import csv
import PyQt5.QtWidgets as qtw
import adminUser


class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiLogin()
        self.ventana.setupUi(self)
        self.ventana.btnIngresar.clicked.connect(self.IngresarUsuario)
        self.ventana.btnAdmin.clicked.connect(self.IngresarAdminUsuario)
        
        
    def IngresarUsuario(self):
        bandera = False
        nombreaux = self.ventana.nomUser.text()
        contraseña = self.ventana.cntUser.text()
        with open("Archivos de Datos/ListaUsuarios.csv","r",encoding="utf-8") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i=0 
            for l in lector:
                if l[1] == nombreaux and l[9] == contraseña:
                    bandera = True
                    break
                i+= 1             
        if bandera == False:
            qtw.QMessageBox.warning(self,"ERROR Datos Incorrectos","El usuario o contraseña son erroneos")
        elif bandera == True:    
            self.id = i
            self.ventana2 = listaProd.listaProd(self.id)        
            self.ventana2.actualizarNombre()
            self.ventana2.show()
            self.hide()   
           
    def IngresarAdminUsuario(self):
        adminUser.adminUser().show()
        self.hide()
    
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaMain = login()
    ventanaMain.show()
    app.exec_()