import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
from uiVerUser import Ui_VerUser
import adminUser

class VerUsuario(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventanaUi = Ui_VerUser()
        self.ventanaUi.setupUi(self)
        self.ventanaUi.btnAtras.clicked.connect(self.Volver)
        
        
    def actualizar(self):
        with open('Archivos de Datos/ListaUsuarios.csv', "r", encoding="ISO 8859-1") as r:
            lector = csv.reader(r, delimiter=",")
            next(lector)
            i = 0
            for l in lector:
                i = (i+1)
                if i == (self.cont+1):
                    cliente = l
        
            self.ventanaUi.verNombre.setText(str(cliente[1]))
            self.ventanaUi.verApellidos.setText(str(cliente[2]) + " " + str(cliente[3]))
            self.ventanaUi.verRut.setText(str(cliente[7]))
            self.ventanaUi.verFecha.setText(str(cliente[6]))
            self.ventanaUi.verCorreo.setText(str(cliente[5]))
            self.ventanaUi.verCargo.setText(str(cliente[8]))
            self.ventanaUi.verGenero.setText(str(cliente[4]))
        
                
    def Volver(self):
        adminUser.adminUser().show()
        self.close()
