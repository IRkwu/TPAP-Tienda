import csv
from PyQt5.QtWidgets import QMainWindow, QApplication
import PyQt5.QtWidgets as qtw
import sys
from uiAdminUser import admin
import crearUser
import modificarUser
import loginUser
import VerUsuario

class adminUser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ventana = admin()
        self.ventanaLog = loginUser.login()
        self.ventana.setupUi(self)
        self.lista = self.ventana.listaUsuario
        self.seleccionUser = -1
        self.actualizarLista()
        self.ventana.btnVerUsuario.setEnabled(False)
        self.ventana.btnEliminar.setEnabled(False)
        self.ventana.btnModificar.setEnabled(False)
        self.ventana.btnEliminar.clicked.connect(lambda: self.eliminar(self.seleccionUser))
        self.lista.itemSelectionChanged.connect(self.filaSel)
        ventana1 = crearUser.crearUser()
        self.ventana2 = modificarUser.modificarUser(self.seleccionUser)
        self.ventana.btnCrearUsuario.clicked.connect(lambda: self.cambio1(ventana1))
        self.ventana.btnModificar.clicked.connect(lambda: self.cambio(self.ventana2))
        self.ventana.btnAtras.clicked.connect(lambda: self.cambio1(self.ventanaLog))
        self.ventana3 = VerUsuario.VerUsuario(self.seleccionUser)
        self.ventana.btnVerUsuario.clicked.connect(lambda: self.cambio3(self.ventana3))
        
        
    def filaSel(self):
        self.fila = self.lista.selectedIndexes()
        if self.fila:
            self.ventana.btnVerUsuario.setEnabled(True)
            self.ventana.btnEliminar.setEnabled(True)
            self.ventana.btnModificar.setEnabled(True)
            self.seleccionUser = self.lista.currentRow()
        else:
            self.ventana.btnVerUsuario.setEnabled(False)
            self.ventana.btnEliminar.setEnabled(False)
            self.ventana.btnModificar.setEnabled(False)
        
    def eliminar(self, seleccion):
        with open('Archivos de Datos/ListaUsuarios.csv','r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for number,line in enumerate(lines):
                if number not in [seleccion+1]:
                    file.write(line)
        self.actualizarLista()
        
    def actualizarLista(self):
        with open('Archivos de Datos/ListaUsuarios.csv') as f:
            lector = csv.reader(f)
            next(lector)
            self.usuarios = [row for row in lector]

        contFilas = len(self.usuarios)
        self.lista.setRowCount(contFilas)

        for i, user in enumerate(self.usuarios):
            id = qtw.QTableWidgetItem(user[0])
            self.lista.setItem(i, 0, id)

            rut = qtw.QTableWidgetItem(user[7])
            self.lista.setItem(i, 1, rut)
            
            nombres = qtw.QTableWidgetItem(user[1])
            self.lista.setItem(i, 2, nombres)

            apellidos = qtw.QTableWidgetItem(user[2] + " " + user[3])
            self.lista.setItem(i, 3, apellidos)
            
            cargo = qtw.QTableWidgetItem(user[8])
            self.lista.setItem(i, 4, cargo)
        
    def cambio1(self, ventana):
        ventana.show()
        self.close()
    
    def cambio(self, ventana):
        self.ventana2.cont = self.seleccionUser
        self.ventana2.actualizar()
        ventana.show()
        self.close()
        
    

    def cambio3(self, ventana):
        self.ventana3.cont = self.seleccionUser
        self.ventana3.actualizar()
        ventana.show()
        self.close()