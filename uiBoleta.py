# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boleta.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import random
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets


class uiBoleta(object):
        def __init__(self, idTransaccion):
            self.idTransaccion = idTransaccion
        def setupUi(self, MainWindow):
                print(self.idTransaccion)
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1280, 720)
                MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
                MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 720))
                self.frame.setMinimumSize(QtCore.QSize(1291, 720))
                self.frame.setMaximumSize(QtCore.QSize(1291, 720))
                self.frame.setStyleSheet("background-color: rgb(38, 87, 165);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.labelTitulo = QtWidgets.QLabel(self.frame)
                self.labelTitulo.setGeometry(QtCore.QRect(387, 57, 528, 54))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelTitulo.setFont(font)
                self.labelTitulo.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelTitulo.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        "border-radius: 27px;")
                self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
                self.labelTitulo.setObjectName("labelTitulo")
                self.label2 = QtWidgets.QLabel(self.frame)
                self.label2.setEnabled(False)
                self.label2.setGeometry(QtCore.QRect(122, 127, 1051, 471))
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


                self.btnVolverMenu = QtWidgets.QPushButton(self.frame)
                self.btnVolverMenu.setGeometry(QtCore.QRect(1020, 630, 231, 61))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnVolverMenu.setFont(font)
                self.btnVolverMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnVolverMenu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 30px;\n"
        "border-width: 1px;\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-style: solid;")
                self.btnVolverMenu.setObjectName("btnVolverMenu")

                #Accion boton volver
                self.btnVolverMenu.clicked.connect(self.cambiar_a_ventana_anterior)

                self.labelidTransaccion = QtWidgets.QLabel(self.frame)
                self.labelidTransaccion.setGeometry(QtCore.QRect(130, 140, 181, 54))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelidTransaccion.setFont(font)
                self.labelidTransaccion.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelidTransaccion.setStyleSheet("background-color:transparent;")
                self.labelidTransaccion.setAlignment(QtCore.Qt.AlignCenter)
                self.labelidTransaccion.setObjectName("labelidTransaccion")
                self.labelVendedor = QtWidgets.QLabel(self.frame)
                self.labelVendedor.setGeometry(QtCore.QRect(120, 200, 181, 54))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelVendedor.setFont(font)
                self.labelVendedor.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelVendedor.setStyleSheet("background-color:transparent;")
                self.labelVendedor.setAlignment(QtCore.Qt.AlignCenter)
                self.labelVendedor.setObjectName("labelVendedor")
                self.labelArticulos = QtWidgets.QLabel(self.frame)
                self.labelArticulos.setGeometry(QtCore.QRect(129, 259, 150, 60))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelArticulos.setFont(font)
                self.labelArticulos.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelArticulos.setStyleSheet("background-color:transparent;")
                self.labelArticulos.setAlignment(QtCore.Qt.AlignCenter)
                self.labelArticulos.setObjectName("labelArticulos")
                self.labelFecha = QtWidgets.QLabel(self.frame)
                self.labelFecha.setGeometry(QtCore.QRect(920, 540, 91, 51))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelFecha.setFont(font)
                self.labelFecha.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelFecha.setStyleSheet("background-color:transparent;")
                self.labelFecha.setAlignment(QtCore.Qt.AlignCenter)
                self.labelFecha.setObjectName("labelFecha")
                self.labelValor = QtWidgets.QLabel(self.frame)
                self.labelValor.setGeometry(QtCore.QRect(920, 500, 91, 51))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelValor.setFont(font)
                self.labelValor.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelValor.setStyleSheet("background-color:transparent;")
                self.labelValor.setAlignment(QtCore.Qt.AlignCenter)
                self.labelValor.setObjectName("labelValor")
                self.labelEnvio = QtWidgets.QLabel(self.frame)
                self.labelEnvio.setGeometry(QtCore.QRect(920, 460, 91, 51))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelEnvio.setFont(font)
                self.labelEnvio.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelEnvio.setStyleSheet("background-color:transparent;")
                self.labelEnvio.setAlignment(QtCore.Qt.AlignCenter)
                self.labelEnvio.setObjectName("labelEnvio")
                self.labelImagen = QtWidgets.QLabel(self.frame)
                self.labelImagen.setGeometry(QtCore.QRect(1050, 140, 91, 91))
                self.labelImagen.setStyleSheet("background-color: transparent;")
                self.labelImagen.setText("")
                self.labelImagen.setPixmap(QtGui.QPixmap("imagenes/Icono Fondo.png"))
                self.labelImagen.setScaledContents(True)
                self.labelImagen.setObjectName("labelImagen")
                self.labelidTransaccion_2 = QtWidgets.QLabel(self.frame)
                self.labelidTransaccion_2.setGeometry(QtCore.QRect(300, 140, 181, 54))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelidTransaccion_2.setFont(font)
                self.labelidTransaccion_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelidTransaccion_2.setStyleSheet("background-color:transparent;")
                self.labelidTransaccion_2.setText("")
                self.labelidTransaccion_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelidTransaccion_2.setObjectName("labelidTransaccion_2")
                self.labelVendedor_2 = QtWidgets.QLabel(self.frame)
                self.labelVendedor_2.setGeometry(QtCore.QRect(260, 200, 181, 54))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelVendedor_2.setFont(font)
                self.labelVendedor_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelVendedor_2.setStyleSheet("background-color:transparent;")
                self.labelVendedor_2.setText("")
                self.labelVendedor_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelVendedor_2.setObjectName("labelVendedor_2")
                self.labelEnvio_2 = QtWidgets.QLabel(self.frame)
                self.labelEnvio_2.setGeometry(QtCore.QRect(1000, 470, 151, 31))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelEnvio_2.setFont(font)
                self.labelEnvio_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelEnvio_2.setStyleSheet("background-color:transparent;")
                self.labelEnvio_2.setText("")
                self.labelEnvio_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelEnvio_2.setObjectName("labelEnvio_2")
                self.labelValor_2 = QtWidgets.QLabel(self.frame)
                self.labelValor_2.setGeometry(QtCore.QRect(1000, 510, 161, 31))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelValor_2.setFont(font)
                self.labelValor_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelValor_2.setStyleSheet("background-color:transparent;")
                self.labelValor_2.setText("")
                self.labelValor_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelValor_2.setObjectName("labelValor_2")
                self.labelFecha_2 = QtWidgets.QLabel(self.frame)
                self.labelFecha_2.setGeometry(QtCore.QRect(1000, 550, 161, 30))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.labelFecha_2.setFont(font)
                self.labelFecha_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelFecha_2.setStyleSheet("background-color:transparent;")
                self.labelFecha_2.setText("")
                self.labelFecha_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelFecha_2.setObjectName("labelFecha_2")
                self.listArticulos = QtWidgets.QListWidget(self.frame)
                self.listArticulos.setEnabled(True)
                self.listArticulos.setGeometry(QtCore.QRect(250, 300, 391, 281))
                self.listArticulos.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.listArticulos.setObjectName("listArticulos")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.obtenerDatosBoleta()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.labelTitulo.setText(_translate("MainWindow", "BOLETA"))
                self.btnVolverMenu.setText(_translate("MainWindow", "Volver al Menú"))
                self.labelidTransaccion.setText(_translate("MainWindow", "ID de Transacción:"))
                self.labelVendedor.setText(_translate("MainWindow", "Vendedor:"))
                self.labelArticulos.setText(_translate("MainWindow", "Articulos:"))
                self.labelFecha.setText(_translate("MainWindow", "Fecha:"))
                self.labelValor.setText(_translate("MainWindow", "Valor:"))
                self.labelEnvio.setText(_translate("MainWindow", "Envío:"))


        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from uiMenu import uiMenu  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = uiMenu()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()


        def obtenerDatosBoleta(self):

                # Buscar la boleta correspondiente en el archivo CSV
                with open('Archivos de Datos/Boletas.csv', 'r', encoding='utf-8') as file:
                        csv_reader = csv.reader(file)
                        next(csv_reader)  # Saltar la primera fila (encabezado)
                        lineas = list(csv_reader)

                # Verificar si se encontró la boleta
                boleta_encontrada = False
                for linea in lineas:

                        if int(linea[0]) == (self.idTransaccion):
                                self.labelidTransaccion_2.setText(linea[0])
                                self.labelVendedor_2.setText(linea[1])
                                self.labelEnvio_2.setText(linea[2])
                                self.labelValor_2.setText(linea[3])
                                self.labelFecha_2.setText(linea[4])

                                articulos = linea[5].strip('][').split(', (')
                                self.listArticulos.clear()
                                self.listArticulos.addItems(articulos)

                                boleta_encontrada = True
                                break

                if not boleta_encontrada:
                        QtWidgets.QMessageBox.critical(self.centralwidget, 'Error', 'No se encontró la boleta correspondiente al ID de transacción.')




                
        