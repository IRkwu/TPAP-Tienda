# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from uiMenu import uiMenu
import adminUser

class uiLogin(object):
        def __init__(self, parent=None):
                self.parent = parent
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1280, 720)
                MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
                MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 701))
                self.frame.setMinimumSize(QtCore.QSize(1291, 701))
                self.frame.setMaximumSize(QtCore.QSize(1291, 701))
                self.frame.setStyleSheet("background-color: rgb(38, 87, 165);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.label = QtWidgets.QLabel(self.frame)
                self.label.setGeometry(QtCore.QRect(355, 50, 528, 54))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.label.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        "border-radius: 27px;")
                self.label.setAlignment(QtCore.Qt.AlignCenter)
                self.label.setObjectName("label")
                self.label2 = QtWidgets.QLabel(self.centralwidget)
                self.label2.setGeometry(QtCore.QRect(400, 120, 440, 519))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.label2.setFont(font)
                self.label2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border: 2px solid #000000;")
                self.label2.setText("")
                self.label2.setAlignment(QtCore.Qt.AlignCenter)
                self.label2.setObjectName("label2")
                self.labelUsuario = QtWidgets.QLabel(self.centralwidget)
                self.labelUsuario.setGeometry(QtCore.QRect(567, 148, 92, 92))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuario.setFont(font)
                self.labelUsuario.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
                self.labelUsuario.setStyleSheet("")
                self.labelUsuario.setText("")
                self.labelUsuario.setPixmap(QtGui.QPixmap("imagenes/Logo Cliente.png"))
                self.labelUsuario.setAlignment(QtCore.Qt.AlignCenter)
                self.labelUsuario.setObjectName("labelUsuario")
                self.labelMedicamento = QtWidgets.QLabel(self.centralwidget)
                self.labelMedicamento.setGeometry(QtCore.QRect(440, 145, 62, 108))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelMedicamento.setFont(font)
                self.labelMedicamento.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
                self.labelMedicamento.setStyleSheet("")
                self.labelMedicamento.setText("")
                self.labelMedicamento.setPixmap(QtGui.QPixmap("imagenes/Medicamento png.png"))
                self.labelMedicamento.setAlignment(QtCore.Qt.AlignCenter)
                self.labelMedicamento.setObjectName("labelMedicamento")
                self.labelPastilla = QtWidgets.QLabel(self.centralwidget)
                self.labelPastilla.setGeometry(QtCore.QRect(711, 145, 95, 97))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelPastilla.setFont(font)
                self.labelPastilla.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
                self.labelPastilla.setStyleSheet("")
                self.labelPastilla.setText("")
                self.labelPastilla.setPixmap(QtGui.QPixmap("imagenes/Pastillas png.png"))
                self.labelPastilla.setAlignment(QtCore.Qt.AlignCenter)
                self.labelPastilla.setObjectName("labelPastilla")

                #Nombre Usuario
                self.nomUser = QtWidgets.QLineEdit(self.centralwidget)
                self.nomUser.setGeometry(QtCore.QRect(443, 272, 344, 62))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(14)
                self.nomUser.setFont(font)
                self.nomUser.setStyleSheet("border: 2px solid #000000;\n"
        "background-color: rgb(255, 255, 255);")
                self.nomUser.setText("")
                self.nomUser.setAlignment(QtCore.Qt.AlignCenter)
                self.nomUser.setObjectName("nomUser")

                #Contraseña Usuario
                self.cntUser = QtWidgets.QLineEdit(self.centralwidget)
                self.cntUser.setGeometry(QtCore.QRect(443, 357, 344, 62))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(14)
                self.cntUser.setFont(font)
                self.cntUser.setStyleSheet("border: 2px solid #000000;\n"
        "background-color: rgb(255, 255, 255);")
                self.cntUser.setText("")
                self.cntUser.setMaxLength(30)
                self.cntUser.setEchoMode(QtWidgets.QLineEdit.Password)
                self.cntUser.setAlignment(QtCore.Qt.AlignCenter)
                self.cntUser.setObjectName("cntUser")

                #Boton ingresar
                self.btnIngresar = QtWidgets.QPushButton(self.centralwidget)
                self.btnIngresar.setGeometry(QtCore.QRect(515, 448, 196, 46))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnIngresar.setFont(font)
                self.btnIngresar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnIngresar.setStyleSheet("border-color: rgb(0, 74, 173);")
                self.btnIngresar.setObjectName("btnIngresar")

                self.btnIngresar.clicked.connect(lambda:self.cambiar_ventana(uiMenu))

                #Boton Administracion de ususarios
                self.btnAdmin = QtWidgets.QPushButton(self.centralwidget)
                self.btnAdmin.setGeometry(QtCore.QRect(479, 524, 273, 46))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnAdmin.setFont(font)
                self.btnAdmin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnAdmin.setStyleSheet("border-color: rgb(0, 74, 173);")
                self.btnAdmin.setObjectName("btnAdmin")
                
                self.btnAdmin.clicked.connect(lambda:self.cambiar_ventana_admin())
                
                MainWindow.setCentralWidget(self.centralwidget)


                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Clinica CVI"))
                self.label.setText(_translate("MainWindow", "TIENDA CLINICA CVI"))
                self.nomUser.setPlaceholderText(_translate("MainWindow", "Nombre de Usuario"))
                self.cntUser.setPlaceholderText(_translate("MainWindow", "Contraseña"))
                self.btnIngresar.setText(_translate("MainWindow", "Ingresar"))
                self.btnAdmin.setText(_translate("MainWindow", "Administracion de usuarios"))

        def verificar_credenciales(self, nombre, contraseña):
                #hay que poner el directorio exacto
                with open('Archivos de Datos/ListaUsuarios.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader) 
                        for row in reader:
                                if row[1] == nombre and row[9] == contraseña:

                                        return True
                return False
        def verificar_admin(self,nombre,contraseña):
                with open('Archivos de Datos/ListaUsuarios.csv', 'r', newline='') as file:
                        reader = csv.reader(file)
                        next(reader)
                        for row in reader:
                                if row[1] == nombre and row[9] == contraseña:
                                        if row[10] == "Administrador":
                                                return True
                return False


        def cambiar_ventana(self, nombreVentana):
                nombre = self.nomUser.text()
                contraseña = self.cntUser.text()
                
                if self.verificar_credenciales(nombre, contraseña):

                        self.uiVentanaActual= QtWidgets.QApplication.activeWindow()
                        self.uiVentanaActual.close()
                        self.nuevaVentana = QtWidgets.QMainWindow()
                        self.ui = nombreVentana()
                        self.ui.setupUi(self.nuevaVentana)
                        self.nuevaVentana.show()
                else:
                        QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'RUT o contraseña incorrectos.')
                        
        def cambiar_ventana_admin(self):
                self.uiVentanaActual= QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                adminUser.adminUser().show()