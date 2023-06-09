# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventaProductos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import csv
import random
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from uiBoleta import uiBoleta
import csv
from PyQt5 import QtCore
from csvArchivo import csvArch


class uiVentaProductos(object):
        def __init__(self):
                self.carrito = []
                self.carritoid = []
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1280, 720)
                MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
                MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(0, 0, 1291, 720))
                self.frame.setMinimumSize(QtCore.QSize(1291, 720))
                self.frame.setMaximumSize(QtCore.QSize(1291, 701))
                self.frame.setStyleSheet("background-color: rgb(38, 87, 165);")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.labelTitulo = QtWidgets.QLabel(self.frame)
                self.labelTitulo.setGeometry(QtCore.QRect(376, 45, 528, 55))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelTitulo.setFont(font)
                self.labelTitulo.setStyleSheet("background-color: rgb(226, 226, 226);\n"
        "border-radius: 27px;")
                self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
                self.labelTitulo.setObjectName("labelTitulo")


                self.btnVerCarrito = QtWidgets.QPushButton(self.frame)
                self.btnVerCarrito.setGeometry(QtCore.QRect(1014, 633, 205, 55))
                self.btnVerCarrito.setEnabled(False)
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnVerCarrito.setFont(font)
                self.btnVerCarrito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnVerCarrito.setStyleSheet("background-color: rgb(240, 240, 240);\n"
        "border-radius: 27px")
                self.btnVerCarrito.setObjectName("btnVerCarrito")

                self.btnVerCarrito.clicked.connect(self.realizarCompra)


                self.listaProductos = QtWidgets.QTableWidget(self.frame)
                self.listaProductos.setGeometry(QtCore.QRect(10, 124, 571, 481))
                self.listaProductos.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.listaProductos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
                self.listaProductos.setAutoScrollMargin(16)
                self.listaProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.listaProductos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.listaProductos.setShowGrid(True)
                self.listaProductos.setGridStyle(QtCore.Qt.SolidLine)
                self.listaProductos.setWordWrap(True)
                self.listaProductos.setCornerButtonEnabled(True)
                self.listaProductos.setRowCount(0)
                self.listaProductos.setObjectName("listaProductos")
                self.listaProductos.setColumnCount(5)
                item = QtWidgets.QTableWidgetItem()
                self.listaProductos.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaProductos.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaProductos.setHorizontalHeaderItem(2, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaProductos.setHorizontalHeaderItem(3, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaProductos.setHorizontalHeaderItem(4, item)
                self.listaProductos.horizontalHeader().setVisible(True)
                self.listaProductos.horizontalHeader().setCascadingSectionResizes(False)
                self.listaProductos.horizontalHeader().setDefaultSectionSize(233)
                self.listaProductos.horizontalHeader().setHighlightSections(True)
                self.listaProductos.horizontalHeader().setSortIndicatorShown(False)
                self.listaProductos.horizontalHeader().setStretchLastSection(True)
                self.listaProductos.verticalHeader().setVisible(False)
                self.listaProductos.verticalHeader().setCascadingSectionResizes(False)
                self.listaProductos.verticalHeader().setHighlightSections(True)
                self.listaProductos.verticalHeader().setStretchLastSection(False)
                self.labelUsuarip = QtWidgets.QLabel(self.frame)
                self.labelUsuarip.setGeometry(QtCore.QRect(14, 10, 91, 91))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuarip.setFont(font)
                self.labelUsuarip.setStyleSheet("")
                self.labelUsuarip.setText("")
                self.labelUsuarip.setPixmap(QtGui.QPixmap("imagenes/Logo Cliente.png"))
                self.labelUsuarip.setAlignment(QtCore.Qt.AlignCenter)
                self.labelUsuarip.setObjectName("labelUsuarip")
                self.labelUsuario2 = QtWidgets.QLabel(self.frame)
                self.labelUsuario2.setGeometry(QtCore.QRect(114, 30, 91, 51))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuario2.setFont(font)
                self.labelUsuario2.setStyleSheet("")
                self.labelUsuario2.setObjectName("labelUsuario2")


                self.labelUsuarioEnLogin = QtWidgets.QLabel(self.frame)
                self.labelUsuarioEnLogin.setGeometry(QtCore.QRect(204, 30, 161, 51))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.labelUsuarioEnLogin.setFont(font)
                self.labelUsuarioEnLogin.setStyleSheet("")
                self.labelUsuarioEnLogin.setText("")
                self.labelUsuarioEnLogin.setObjectName("labelUsuarioEnLogin")


                self.labelAtras = QtWidgets.QLabel(self.frame)
                self.labelAtras.setGeometry(QtCore.QRect(40, 630, 71, 51))
                self.labelAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.labelAtras.setText("")
                self.labelAtras.setPixmap(QtGui.QPixmap("imagenes/Logo Atras.png"))
                self.labelAtras.setScaledContents(True)
                self.labelAtras.setObjectName("labelAtras")
                self.btnAtras = QtWidgets.QPushButton(self.frame)
                self.btnAtras.setGeometry(QtCore.QRect(39, 626, 70, 60))
                self.btnAtras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnAtras.setStyleSheet("background-color: transparent;")
                self.btnAtras.setText("")
                self.btnAtras.setObjectName("btnAtras")

                #Accion boton atras
                self.btnAtras.clicked.connect(self.cambiar_a_ventana_anterior)


                self.listaCarrito = QtWidgets.QTableWidget(self.frame)
                self.listaCarrito.setGeometry(QtCore.QRect(837, 120, 421, 481))
                self.listaCarrito.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.listaCarrito.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
                self.listaCarrito.setAutoScrollMargin(16)
                self.listaCarrito.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
                self.listaCarrito.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.listaCarrito.setShowGrid(True)
                self.listaCarrito.setGridStyle(QtCore.Qt.SolidLine)
                self.listaCarrito.setWordWrap(True)
                self.listaCarrito.setCornerButtonEnabled(True)
                self.listaCarrito.setRowCount(0)
                self.listaCarrito.setObjectName("listaCarrito")
                self.listaCarrito.setColumnCount(3)
                item = QtWidgets.QTableWidgetItem()
                self.listaCarrito.setHorizontalHeaderItem(0, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaCarrito.setHorizontalHeaderItem(1, item)
                item = QtWidgets.QTableWidgetItem()
                self.listaCarrito.setHorizontalHeaderItem(2, item)
                self.listaCarrito.horizontalHeader().setVisible(True)
                self.listaCarrito.horizontalHeader().setCascadingSectionResizes(False)
                self.listaCarrito.horizontalHeader().setDefaultSectionSize(134)
                self.listaCarrito.horizontalHeader().setHighlightSections(True)
                self.listaCarrito.horizontalHeader().setMinimumSectionSize(27)
                self.listaCarrito.horizontalHeader().setSortIndicatorShown(False)
                self.listaCarrito.horizontalHeader().setStretchLastSection(True)
                self.listaCarrito.verticalHeader().setVisible(False)
                self.listaCarrito.verticalHeader().setCascadingSectionResizes(False)
                self.listaCarrito.verticalHeader().setHighlightSections(True)
                self.listaCarrito.verticalHeader().setStretchLastSection(False)



                self.btnAgregarCantidad = QtWidgets.QPushButton(self.frame)
                self.btnAgregarCantidad.setGeometry(QtCore.QRect(630, 230, 171, 61))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnAgregarCantidad.setFont(font)
                self.btnAgregarCantidad.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnAgregarCantidad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 30px;\n"
        "border-width: 1px;\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-style: solid;")
                self.btnAgregarCantidad.setObjectName("btnAgregarCantidad")

                self.btnAgregarCantidad.clicked.connect(self.agregarAlCarrito)

                self.btnEliminar = QtWidgets.QPushButton(self.frame)
                self.btnEliminar.setGeometry(QtCore.QRect(629, 379, 171, 61))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.btnEliminar.setFont(font)
                self.btnEliminar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btnEliminar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 30px;\n"
        "border-width: 1px;\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-style: solid;")
                self.btnEliminar.setObjectName("btnEliminar")

                self.btnEliminar.clicked.connect(self.eliminarDelCarrito)

                self.labelFotoCarrito_2 = QtWidgets.QLabel(self.frame)
                self.labelFotoCarrito_2.setGeometry(QtCore.QRect(384, 616, 91, 91))
                self.labelFotoCarrito_2.setStyleSheet("background-color: transparent;")
                self.labelFotoCarrito_2.setText("")
                self.labelFotoCarrito_2.setPixmap(QtGui.QPixmap("imagenes/Carrito.png"))
                self.labelFotoCarrito_2.setScaledContents(True)
                self.labelFotoCarrito_2.setObjectName("labelFotoCarrito_2")
                self.labelValorTotal_2 = QtWidgets.QLabel(self.frame)
                self.labelValorTotal_2.setGeometry(QtCore.QRect(504, 636, 181, 54))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelValorTotal_2.setFont(font)
                self.labelValorTotal_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelValorTotal_2.setStyleSheet("background-color:transparent;")
                self.labelValorTotal_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelValorTotal_2.setObjectName("labelValorTotal_2")
                self.labelPrecioTotal_2 = QtWidgets.QLabel(self.frame)
                self.labelPrecioTotal_2.setGeometry(QtCore.QRect(704, 636, 210, 54))
                font = QtGui.QFont()
                font.setFamily("Open Sans Semibold")
                font.setPointSize(22)
                font.setBold(True)
                font.setWeight(75)
                self.labelPrecioTotal_2.setFont(font)
                self.labelPrecioTotal_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
                self.labelPrecioTotal_2.setStyleSheet("background-color:transparent;")
                self.labelPrecioTotal_2.setText("")
                self.labelPrecioTotal_2.setAlignment(QtCore.Qt.AlignCenter)
                self.labelPrecioTotal_2.setObjectName("labelPrecioTotal_2")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.cargarProductosCSV()
                self.listaProductos.itemSelectionChanged.connect(self.actualizarBotones)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.labelTitulo.setText(_translate("MainWindow", "VENTA DE PRODUCTOS"))
                self.btnVerCarrito.setText(_translate("MainWindow", "Ver carrito"))
                self.listaProductos.setSortingEnabled(False)
                item = self.listaProductos.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.listaProductos.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Nombre Producto"))
                item = self.listaProductos.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Categoria"))
                item = self.listaProductos.horizontalHeaderItem(3)
                item.setText(_translate("MainWindow", "Precio"))
                item = self.listaProductos.horizontalHeaderItem(4)
                item.setText(_translate("MainWindow", "Precio Lote"))
                self.labelUsuario2.setText(_translate("MainWindow", "Usuario: "))
                self.listaCarrito.setSortingEnabled(False)
                item = self.listaCarrito.horizontalHeaderItem(0)
                item.setText(_translate("MainWindow", "ID"))
                item = self.listaCarrito.horizontalHeaderItem(1)
                item.setText(_translate("MainWindow", "Nombre Producto"))
                item = self.listaCarrito.horizontalHeaderItem(2)
                item.setText(_translate("MainWindow", "Precio"))
                self.btnAgregarCantidad.setText(_translate("MainWindow", "Agregar"))
                self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
                self.labelValorTotal_2.setText(_translate("MainWindow", "Valor total:"))

         # Abre el archivo CSV y devuelve los datos como una lista de filas
        def leerDatosDesdeCSV(self):
                with open('Archivos de Datos/ListaArticulos.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                        return list(reader)


        def insertarDatosEnTabla(self, datos):
                for i, fila in enumerate(datos):
                        posicionFila = self.listaProductos.rowCount()
                        self.listaProductos.insertRow(posicionFila)

                        for columna, value in enumerate(fila):
                                item = QtWidgets.QTableWidgetItem(value)
                                item.setTextAlignment(QtCore.Qt.AlignCenter)
                                self.listaProductos.setItem(posicionFila, columna, item)

                                if columna == 2 :
                                        # Verificar si el stock es igual o por debajo del límite crítico
                                        if int(fila[6]) <= int(fila[2]):
                                                # Establecer el color de fondo de la celda en rojo
                                                item.setBackground(QtGui.QColor("red"))
                                                # Establecer el texto de la celda
                                                item.setText(f"Stock es igual o por debajo de: {fila[5]}")
                                        else:
                                                # Establecer el color de fondo de la celda en verde
                                                item.setBackground(QtGui.QColor("green"))
                                                item.setText("")

        # Carga los datos del archivo CSV en el tableWidget
        def cargarProductosCSV(self):
                datos = self.leerDatosDesdeCSV()

                if datos:
                        # Seleccionar las columnas "Id", "Nombre", "Categoria", "Marca", "Precio", "Stock" ,"Limite critico" (columnas 0, 7 , 1 y 2) 
                        datos_seleccionados = [[fila[2],fila[0] ,fila[9], fila[7], fila[4], fila[3] ,fila[5]] for fila in datos]
                        encabezados = datos_seleccionados.pop(0)  
                        self.listaProductos.setColumnCount(len(encabezados))
                        self.listaProductos.setHorizontalHeaderLabels(encabezados)

                        self.insertarDatosEnTabla(datos_seleccionados)
                else:
                        print("La lista de datos está vacía")

        def cambiar_ventana(self, nombreVentana):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = nombreVentana()
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_ventanaBoleta(self, idTransaccion):
                self.uiVentanaActual = QtWidgets.QApplication.activeWindow()
                self.uiVentanaActual.close()
                self.nuevaVentana = QtWidgets.QMainWindow()
                self.ui = uiBoleta(idTransaccion)
                self.ui.setupUi(self.nuevaVentana)
                self.nuevaVentana.show()

        def cambiar_a_ventana_anterior(self):
                self.ventanaActual = QtWidgets.QApplication.activeWindow()
                self.ventanaActual.close()
                from uiMenu import uiMenu  # Importación local para evitar el ciclo de importación
                self.ventanaAnterior = QtWidgets.QMainWindow(self.ventanaActual.parent())
                self.uiVentanaAnterior = uiMenu()
                self.uiVentanaAnterior.setupUi(self.ventanaAnterior)
                self.ventanaAnterior.show()
        
        def actualizarBotones(self):
                filasSeleccionada = self.listaProductos.selectedIndexes()

                if filasSeleccionada:
                        # Se seleccionó al menos una fila
                        self.btnVerCarrito.setEnabled(True)
                else:
                        # No se seleccionó ninguna fila
                        self.btnVerCarrito.setEnabled(False)

        def agregarAlCarrito(self):
                productoSeleccionado = self.listaProductos.currentRow()

                if productoSeleccionado != -1:
                        idProducto = self.listaProductos.item(productoSeleccionado, 0).text()
                        nombreProducto = self.listaProductos.item(productoSeleccionado, 1).text()
                        precioProducto = int(self.listaProductos.item(productoSeleccionado, 4).text())
                        stockProducto = int(self.listaProductos.item(productoSeleccionado, 6).text())

                        if stockProducto != 0:
                                stockProducto -= 1
                                self.listaProductos.item(productoSeleccionado, 6).setText(str(stockProducto))

                                self.carrito.append((idProducto, nombreProducto, precioProducto))
                                self.carritoid.append(idProducto)

                                self.actualizarCarrito()
                                self.actualizarPrecioTotal()
                
        
        def eliminarDelCarrito(self):
                productoSeleccionado = self.listaCarrito.currentRow()
                
                if productoSeleccionado != -1:
                        idProducto = (self.listaCarrito.item(productoSeleccionado, 0).text())

                        for fila in range(self.listaProductos.rowCount()):
                                idFila = (self.listaProductos.item(fila, 0).text())
                                if idFila == idProducto:
                                        stockActual = int(self.listaProductos.item(fila, 6).text())
                                        stockActual += 1
                                        self.listaProductos.item(fila, 6).setText(str(stockActual))
                                        break
                                
                        self.carrito.pop(productoSeleccionado)
                        self.carritoid.pop(productoSeleccionado)
                        self.actualizarCarrito()
                        self.actualizarPrecioTotal()
                else:
                        QMessageBox.warning(self.frame, "Error", "No se ha seleccionado ningún producto para eliminar.")



        def actualizarCarrito(self):
                totalDeFilas= len(self.carrito)
                self.listaCarrito.setRowCount(totalDeFilas)
                for i, (idProducto, nombreProducto, precioProducto) in enumerate(self.carrito):
                        self.listaCarrito.setItem(i, 0, QTableWidgetItem(str(idProducto)))
                        self.listaCarrito.setItem(i, 1, QTableWidgetItem(str(nombreProducto)))
                        self.listaCarrito.setItem(i, 2, QTableWidgetItem(str(precioProducto)))

        
        def actualizarPrecioTotal(self):
                total = sum(producto[2] for producto in self.carrito)
                self.labelPrecioTotal_2.setText(str(total))

        def realizarCompra(self):
                if not self.carrito:
                        QMessageBox.warning(None, "Error", "El carrito está vacío.")
                        return

                id_transaccion = random.randint(100000, 999999)
                valor_envio = sum(producto[2] for producto in self.carrito) * 0.20
                valor_total = int(self.labelPrecioTotal_2.text()) + valor_envio
                fecha_compra = date.today().strftime("%d/%m/%Y")

                articulos = self.carrito


                datos_boleta = [
                        id_transaccion,
                        "Diego Jaune",  
                        valor_envio,
                        valor_total,
                        fecha_compra,
                        articulos
                ]

                # Leer el contenido existente del archivo CSV
                with open("Archivos de Datos/Boletas.csv", "r") as file:
                        reader = csv.reader(file)
                        contenido_existente = list(reader)

                # Agregar los datos de la boleta al contenido existente
                contenido_existente.append(datos_boleta)

                # Escribir todo el contenido nuevamente en el archivo CSV
                with open("Archivos de Datos/Boletas.csv", "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(contenido_existente)

                QMessageBox.information(None, "Compra realizada", "La compra se ha realizado correctamente.")

                self.eliminarStock()

                # Limpiar carrito
                self.carrito.clear()

                # Limpiar la tabla del carrito
                self.listaCarrito.setRowCount(0)

                # Actualizar precio total en la interfaz
                self.labelPrecioTotal_2.setText("")

                self.cambiar_ventanaBoleta(id_transaccion)

        def eliminarStock(self):
                for x in self.carritoid:
                        with open('Archivos de Datos/ListaArticulos.csv', "r", encoding="ISO 8859-1") as r:
                                lector = csv.reader(r, delimiter=",")
                                next(lector)
                                i = 0
                                for l in lector:
                                        if f"{l[2]}" == f"{x}":
                                                self.Producto = l
                                                break
                                        i += 1
                        stockFinal = int(self.Producto[5]) - 1
                        csvArch.modificar("Archivos de Datos/ListaArticulos.csv", i, 5, stockFinal)
