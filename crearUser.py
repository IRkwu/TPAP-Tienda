import csv
import random
from PyQt5.QtWidgets import QMainWindow
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from uiCrearUser import uiCrear
import adminUser
from Usuario import Usuario
from csvArchivo import csvArch

class crearUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = uiCrear()
        self.ventana.setupUi(self)
        self.ventana.btnOcultar.setVisible(False)
        self.ventana.btnOcultar.setEnabled(False)
        self.ventana.btnMostrar.clicked.connect(lambda: self.cambioContraseña())
        self.ventana.btnOcultar.clicked.connect(lambda: self.cambioContraseña())
        self.ventana.btnAtras.clicked.connect(self.volver)
        self.digito = qtg.QRegExpValidator(qtc.QRegExp("[0-9K]"), self)
        self.restricRut = qtg.QRegExpValidator(qtc.QRegExp("[0-9]+"), self)
        self.soloStr = qtg.QRegExpValidator(qtc.QRegExp("[a-zA-ZáéíóúÁÉÍÓÚüÜ ]+"))
        self.restricCorreo = qtg.QRegExpValidator(qtc.QRegExp("[^@]+"))
        self.ventana.inputRut.setValidator(self.restricRut)
        self.ventana.inputDigito.setValidator(self.digito)
        self.ventana.inputNombre.setValidator(self.soloStr)
        self.ventana.inputApellidoP.setValidator(self.soloStr)
        self.ventana.inputApellidoM.setValidator(self.soloStr)
        self.ventana.inputCorreo.setValidator(self.restricCorreo)
        self.ventana.inputDominio.setValidator(self.restricCorreo)
        self.restricFechaMin = qtc.QDate(1924, 1, 1)
        self.restricFechaMax = qtc.QDate(2005, 12, 31)
        self.ventana.btnRegistrar.clicked.connect(self.agregarUser)
    
    def cambioContraseña(self):
        if self.ventana.btnMostrar.isVisible():
            self.ventana.btnMostrar.setVisible(False)
            self.ventana.btnMostrar.setEnabled(False)
            self.ventana.btnOcultar.setVisible(True)
            self.ventana.btnOcultar.setEnabled(True)
            self.ventana.inputPassword.setEchoMode(qtw.QLineEdit.Normal)
        else:
            self.ventana.btnMostrar.setVisible(True)
            self.ventana.btnMostrar.setEnabled(True)
            self.ventana.btnOcultar.setVisible(False)
            self.ventana.btnOcultar.setEnabled(False)
            self.ventana.inputPassword.setEchoMode(qtw.QLineEdit.Password)
    
    def agregarUser(self):
        cuadrosTexto = [self.ventana.inputNombre, self.ventana.inputApellidoP, self.ventana.inputApellidoM, self.ventana.inputCorreo, self.ventana.inputDominio, self.ventana.inputRut]
        vacios = False
        fecha = self.ventana.dateNacimiento.date()
        
        for cuadro in cuadrosTexto:
            texto = cuadro.text()
            if texto == "" or texto.isspace():
                vacios = True
                break
            
        verPass = self.ventana.inputPassword.text()
        if vacios or self.ventana.comboBoxG.currentIndex() < 1 or self.ventana.comboBoxC.currentIndex() < 1 or len(verPass) < 2:
            qtw.QMessageBox.warning(self, "Hay campos sin rellenar", "Por favor, rellene sus datos correctamente.")
        elif fecha < self.restricFechaMin or fecha > self.restricFechaMax:
            qtw.QMessageBox.warning(self, "Fecha invalida", "Parece que la fecha no es valida, ingrese una fecha entre los años 1924 - 2005.")
        else:
            with open('Archivos de Datos/ListaUsuarios.csv', 'r', encoding="utf-8") as r:
                l = csv.reader(r, delimiter=",")
                next(l)
                for lis in l:
                    if lis[7] == (self.ventana.inputRut.text() + "-" + self.ventana.inputDigito.text()):
                        qtw.QMessageBox.warning(self, "ERROR", "El rut ingresado ya existe.\nPorfavor, ingrese un rut nuevo, o en su defecto, ingrese un rut valido.")
                        return
            nombre = self.ventana.inputNombre.text()
            caracteres = random.randint(3, 30)
            nums = [str(random.randint(0, 9)) for _ in range(caracteres)]
            id = ''.join(nums)
            apellidoP = self.ventana.inputApellidoP.text()
            apellidoM = self.ventana.inputApellidoM.text()
            genero = self.ventana.comboBoxG.currentText()
            correo = (self.ventana.inputCorreo.text() + "@" + self.ventana.inputDominio.text())
            fechaNac = fecha.toString("dd/MM/yyyy")
            rut = (self.ventana.inputRut.text() + "-" + self.ventana.inputDigito.text())
            cargo = self.ventana.comboBoxC.currentText()
            contrasena = self.ventana.inputPassword.text()
            user1 = Usuario(str(id), str(nombre), str(apellidoP), str(apellidoM), str(genero), str(correo), str(fechaNac), str(rut), str(cargo), str(contrasena))
            csvArch.insertar("Archivos de Datos/ListaUsuarios.csv", user1)
            adminUser.adminUser().actualizarLista()
            adminUser.adminUser().show()
            self.close()
        
    
    def volver(self):
        adminUser.adminUser().show()
        self.close()