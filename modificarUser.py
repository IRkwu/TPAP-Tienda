import csv
import random
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from uiModificarUser import uiModificar
import adminUser
from csvArchivo import csvArch

class modificarUser(QMainWindow):
    def __init__(self, cont):
        super().__init__()
        self.cont = cont
        self.ventana = uiModificar()
        self.ventana.setupUi(self)
        self.ventana.botonGuardarN.setVisible(False)
        self.ventana.botonGuardarN.setEnabled(False)
        self.ventana.botonGuardarApP.setVisible(False)
        self.ventana.botonGuardarApP.setEnabled(False)
        self.ventana.botonGuardarApM.setVisible(False)
        self.ventana.botonGuardarApM.setEnabled(False)
        self.ventana.botonGuardarCorreo.setVisible(False)
        self.ventana.botonGuardarCorreo.setEnabled(False)
        self.ventana.botonGuardarCargo.setVisible(False)
        self.ventana.botonGuardarCargo.setEnabled(False)
        self.ventana.botonGuardarPass.setVisible(False)
        self.ventana.botonGuardarPass.setEnabled(False)
        self.ventana.inputNombre.setEnabled(False)
        self.ventana.inputApellidoP.setEnabled(False)
        self.ventana.inputApellidoM.setEnabled(False)
        self.ventana.inputCorreo.setEnabled(False)
        self.ventana.comboBoxC.setEnabled(False)
        self.ventana.inputContra.setEnabled(False)
        self.ventana.btnOcultar.setVisible(False)
        self.ventana.btnOcultar.setEnabled(False)
        self.ventana.btnMostrar.setEnabled(False)
        self.ventana.inputCorreo.setEnabled(False)
        self.ventana.labelArroba.setVisible(False)
        self.ventana.inputDominio.setEnabled(False)
        self.ventana.inputDominio.setVisible(False)
        self.ventana.btnAtras.clicked.connect(self.atras)
        self.ventana.botonModificarN.clicked.connect(lambda: self.activar(1))
        self.ventana.botonModificarApP.clicked.connect(lambda: self.activar(2))
        self.ventana.botonModificarApM.clicked.connect(lambda: self.activar(3))
        self.ventana.botonModificarCorreo.clicked.connect(lambda: self.activar(4))
        self.ventana.botonRegistrarCargo.clicked.connect(lambda: self.activar(5))
        self.ventana.botonRegistrarPass.clicked.connect(lambda: self.activar(6))
        self.ventana.botonGuardarN.clicked.connect(lambda: self.modificar(1))
        self.ventana.botonGuardarApP.clicked.connect(lambda: self.modificar(2))
        self.ventana.botonGuardarApM.clicked.connect(lambda: self.modificar(3))
        self.ventana.botonGuardarCorreo.clicked.connect(lambda: self.modificar(4))
        self.ventana.botonGuardarCargo.clicked.connect(lambda: self.modificar(5))
        self.ventana.botonGuardarPass.clicked.connect(lambda: self.modificar(6))
        self.ventana.btnMostrar.clicked.connect(lambda: self.cambioContraseña())
        self.ventana.btnOcultar.clicked.connect(lambda: self.cambioContraseña())
        
        
    def atras(self):
        adminUser.adminUser().show()
        self.close()
        
    def actualizar(self):
        with open('Archivos de Datos/ListaUsuarios.csv', 'r', encoding="utf-8") as r:
            l = csv.reader(r, delimiter=",")
            next(l)

            i = 0
            for lis in l:
                if i == self.cont:
                    self.usuario = lis
                    break
                i += 1

        self.ventana.inputNombre.setText(self.usuario[1])
        self.ventana.inputApellidoP.setText(self.usuario[2])
        self.ventana.inputApellidoM.setText(self.usuario[3])
        self.ventana.labelGeneroNoEditar.setText(self.usuario[4])
        self.ventana.labelCorreoNoEditar.setText(self.usuario[5])
        self.ventana.labelFechaNoEditar.setText(self.usuario[6])
        self.ventana.labelRutNoEditar.setText(self.usuario[7])
        if self.usuario[8] == "Cajero/a":
            self.ventana.comboBoxC.setCurrentIndex(1)
        elif self.usuario[8] == "Gerente":
            self.ventana.comboBoxC.setCurrentIndex(2)
        elif self.usuario[8] == "Asistente de Ventas":
            self.ventana.comboBoxC.setCurrentIndex(3)
        self.ventana.inputContra.setText(self.usuario[9])
    
    def cambioContraseña(self):
        if self.ventana.btnMostrar.isVisible():
            self.ventana.btnMostrar.setVisible(False)
            self.ventana.btnMostrar.setEnabled(False)
            self.ventana.btnOcultar.setVisible(True)
            self.ventana.btnOcultar.setEnabled(True)
            self.ventana.inputContra.setEchoMode(qtw.QLineEdit.Normal)
        else:
            self.ventana.btnMostrar.setVisible(True)
            self.ventana.btnMostrar.setEnabled(True)
            self.ventana.btnOcultar.setVisible(False)
            self.ventana.btnOcultar.setEnabled(False)
            self.ventana.inputContra.setEchoMode(qtw.QLineEdit.Password)
    
    def activar(self, cont):
        if cont == 1:
            self.ventana.inputNombre.setEnabled(True)
            self.ventana.botonModificarN.setVisible(False)
            self.ventana.botonModificarN.setEnabled(False)
            self.ventana.botonGuardarN.setVisible(True)
            self.ventana.botonGuardarN.setEnabled(True)
        elif cont == 2:
            self.ventana.inputApellidoP.setEnabled(True)
            self.ventana.botonModificarApP.setVisible(False)
            self.ventana.botonModificarApP.setEnabled(False)
            self.ventana.botonGuardarApP.setVisible(True)
            self.ventana.botonGuardarApP.setEnabled(True)
        elif cont == 3:
            self.ventana.inputApellidoM.setEnabled(True)
            self.ventana.botonModificarApM.setVisible(False)
            self.ventana.botonModificarApM.setEnabled(False)
            self.ventana.botonGuardarApM.setVisible(True)
            self.ventana.botonGuardarApM.setEnabled(True)
        elif cont == 4:
            self.ventana.inputCorreo.setEnabled(True)
            self.ventana.labelArroba.setVisible(True)
            self.ventana.inputDominio.setVisible(True)
            self.ventana.inputDominio.setEnabled(True)
            self.ventana.labelCorreoNoEditar.setVisible(False)
            self.ventana.botonModificarCorreo.setVisible(False)
            self.ventana.botonModificarCorreo.setEnabled(False)
            self.ventana.botonGuardarCorreo.setVisible(True)
            self.ventana.botonGuardarCorreo.setEnabled(True)
        elif cont == 5:
            self.ventana.comboBoxC.setEnabled(True)
            self.ventana.botonRegistrarCargo.setVisible(False)
            self.ventana.botonRegistrarCargo.setEnabled(False)
            self.ventana.botonGuardarCargo.setVisible(True)
            self.ventana.botonGuardarCargo.setEnabled(True)
        elif cont == 6:
            self.ventana.inputContra.setEnabled(True)
            self.ventana.btnMostrar.setEnabled(True)
            self.ventana.botonRegistrarPass.setVisible(False)
            self.ventana.botonRegistrarPass.setEnabled(False)
            self.ventana.botonGuardarPass.setVisible(True)
            self.ventana.botonGuardarPass.setEnabled(True)
        self.ventana.btnAtras.setEnabled(False)
        self.ventana.labelAtras.setVisible(False)
    
    def modificar(self, conta):
        if conta != 4:
            cuadrosTexto = [self.ventana.inputNombre, self.ventana.inputApellidoP, self.ventana.inputApellidoM]
        else:
            cuadrosTexto = [self.ventana.inputNombre, self.ventana.inputApellidoP, self.ventana.inputApellidoM, self.ventana.inputCorreo, self.ventana.inputDominio]
        vacios = False
        
        for cuadro in cuadrosTexto:
            texto = cuadro.text()
            if texto == "" or texto.isspace():
                vacios = True
                break
            
        verPass = self.ventana.inputContra.text()
        if vacios or self.ventana.comboBoxC.currentIndex() < 1 or len(verPass) < 2:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        else:
            if conta == 1:
                self.ventana.inputNombre.setEnabled(False)
                self.ventana.botonModificarN.setVisible(True)
                self.ventana.botonModificarN.setEnabled(True)
                self.ventana.botonGuardarN.setVisible(False)
                self.ventana.botonGuardarN.setEnabled(False)
                objAux = self.ventana.inputNombre.text()
            elif conta == 2:
                self.ventana.inputApellidoP.setEnabled(False)
                self.ventana.botonModificarApP.setVisible(True)
                self.ventana.botonModificarApP.setEnabled(True)
                self.ventana.botonGuardarApP.setVisible(False)
                self.ventana.botonGuardarApP.setEnabled(False)
                objAux = self.ventana.inputApellidoP.text()
            elif conta == 3:
                self.ventana.inputApellidoM.setEnabled(False)
                self.ventana.botonModificarApM.setVisible(True)
                self.ventana.botonModificarApM.setEnabled(True)
                self.ventana.botonGuardarApM.setVisible(False)
                self.ventana.botonGuardarApM.setEnabled(False)
                objAux = self.ventana.inputApellidoM.text()
            elif conta == 4:
                self.ventana.inputCorreo.setEnabled(False)
                self.ventana.labelArroba.setVisible(False)
                self.ventana.inputDominio.setVisible(False)
                self.ventana.inputDominio.setEnabled(False)
                self.ventana.labelCorreoNoEditar.setVisible(True)
                self.ventana.botonModificarCorreo.setVisible(True)
                self.ventana.botonModificarCorreo.setEnabled(True)
                self.ventana.botonGuardarCorreo.setVisible(False)
                self.ventana.botonGuardarCorreo.setEnabled(False)
                objAux = (self.ventana.inputCorreo.text() + "@" + self.ventana.inputDominio.text())
                conta = 5
            elif conta == 5:
                self.ventana.comboBoxC.setEnabled(False)
                self.ventana.botonRegistrarCargo.setVisible(True)
                self.ventana.botonRegistrarCargo.setEnabled(True)
                self.ventana.botonGuardarCargo.setVisible(False)
                self.ventana.botonGuardarCargo.setEnabled(False)
                objAux = self.ventana.comboBoxC.currentText()
                conta = 8
            elif conta == 6:
                self.ventana.inputContra.setEnabled(False)
                self.ventana.btnMostrar.setEnabled(False)
                self.ventana.botonRegistrarPass.setVisible(True)
                self.ventana.botonRegistrarPass.setEnabled(True)
                self.ventana.botonGuardarPass.setVisible(False)
                self.ventana.botonGuardarPass.setEnabled(False)
                conta = 9
                if self.ventana.btnOcultar.isVisible():
                    self.cambioContraseña
                objAux = self.ventana.inputContra.text()
            if self.ventana.botonModificarN.isVisible() and self.ventana.botonModificarApP.isVisible() and self.ventana.botonModificarApM.isVisible() and self.ventana.botonModificarCorreo.isVisible() and self.ventana.botonRegistrarCargo.isVisible() and self.ventana.botonRegistrarPass.isVisible():
                self.ventana.btnAtras.setEnabled(True)
                self.ventana.labelAtras.setVisible(True)
            csvArch.modificar("Archivos de Datos/ListaUsuarios.csv", self.cont, conta, objAux)
            self.actualizar()