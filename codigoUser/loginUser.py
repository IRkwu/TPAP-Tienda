import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys
from uiLoginUser import uiLogin

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiLogin()
        self.ventana.setupUi(self)
        
        self.ventana.btnIngresar.clicked.connect(self.metodoEjemplo)
        
    def metodoEjemplo(self):
        print("ola")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ventanaMain = login()
    ventanaMain.show()
    app.exec_()