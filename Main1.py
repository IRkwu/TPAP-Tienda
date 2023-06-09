import sys
from Articulos import Articulos, ListaArticulos
from Carrito import Carrito, Carrito_Cliente
from Cliente import Cliente
from Venta import Venta
from Envio import Envio
import random
import time


def ingresarDatosNuevoCliente(tipoCliente):

    # random.seed(time.time()) es para que el numero genero sea aleatorio e irrepetible
    random.seed(time.time())
    id = random.randint(100000, 999999)
    nombres = input("Ingresar nombres: ")
    apellido_paterno = input("Ingresar apellido paterno: ")
    apellido_materno = input("Ingresar apellido materno: ")
    rut = input("Ingresar rut: ")
    # El cliente tipo 1 es porque necesita un envio
    if tipoCliente == 1:
        genero = input("Ingresar genero: ")
        fecha_nacimiento = input("Ingresar fecha nacimiento: ")
        email = input("Ingresar email: ")
        telefono = input("Ingresar telefono: ")
        direccion = input("Ingresar direcion: ")
        descripcion = input("Ingresar descripción del envio: ")

        # Se agregan los datos del cliente en ListaClientes
        Cliente.AgregarClientes(None, id, nombres, apellido_paterno, apellido_materno, genero,
                                fecha_nacimiento, rut, email, telefono, direccion, ["Mascota"], "Historial")
        Envio.AgregarEnvios(None, descripcion, id, direccion)
    # El cliente tipo 2 es porque no necesita un envio
    elif tipoCliente == 2:
        Cliente.AgregarClientes(None,
                                id, nombres, apellido_paterno, apellido_materno, "", "", rut, "", "", "", "", "")


def llenadoDeCarrito(tipo):
    id = ""
    opcion = ''
    comprobacion = False

    while True:
        print("\n --INGRESE EL ID DE LOS PRODUCTOS A COMPRAR-- \n")
        id = input("ID: ")
        i = 0
        for articulo in ListaArticulos:
            if id == articulo.get_id():
                if articulo.get_stock() > 0:
                    if tipo == 1:
                        Carrito_Cliente.AgregarArticuloUnidad(i)
                    elif tipo == 2:
                        Carrito_Cliente.AgregarArticuloLote(i)
                    comprobacion = True
                else:
                    print("No hay stock del producto")
                    comprobacion = True
            i += 1

        if not comprobacion:
            print("Error, ID no existe")

        print("\nDesea agregar otro producto?\n")
        print("S = Si // N = No")
        opcion = input("Opcion: ")
        comprobacion = False

        if opcion.lower() != 's':
            break


def ConfirmarEnvio():
    opcion = 0
    print("Usted necesita envio: ")
    print("1.Si // 2.No")
    opcion = int(input("Ingrese su opción: "))
    print("\n")
    if opcion == 1:
        print("Necesitamos su datos para realizar el envio")
        ingresarDatosNuevoCliente(1)
    elif opcion == 2:
        print("Necesitamos sus datos para realizar la boleta")
        ingresarDatosNuevoCliente(2)
    else:
        print("Opción equivocada. Intente nuevamente")


def compraPorUnidadOPorLote():
    opcion = 0
    while True:
        print("\n ¿Desea comprar por Unidad o por Lote?")
        print("1.- Unidad \n2.- Lote")
        opcion = int(input("Opcion: "))
        if opcion != 1 or 2:
            break
    return opcion


# Main - Menu


opcion = 0
pasoPorSeleccionarProducto = False
tipoCompra = 0
while True:
    print("\n --MENU-- \n")
    print("1.- Ver productos")
    print("2.- Seleccionar productos")
    print("3.- Realizar compra")
    print("4.- Ver envio")
    print("5.- Mostrar artículos del carrito")
    print("6.- Salir")

    opcion = input("Opcion: ")
    print("\n")

    if opcion == "1":
        Articulos.MostrarListaArticulos(None)
    elif opcion == "2":
        pasoPorSeleccionarProducto = True
        tipoCompra = compraPorUnidadOPorLote()
        llenadoDeCarrito(tipoCompra)
    elif opcion == "3":
        if pasoPorSeleccionarProducto:
            ConfirmarEnvio()
            Venta.ConfirmarVenta(None)
        else:
            print("Primero tiene que seleccionar productos antes de realizar la compra")
    elif opcion == "4":
        id = input("\nIngrese el id de transaccion del cliente: ")
        Envio.mostrarEnvio(id)
    elif opcion == "5":
        Carrito_Cliente.MostrarArticulosCarrito()
    elif opcion == "6":
        print("Saliendo del Menu")
        break
    else:
        print("Opcion no válida. Intente de nuevo.")


# ---------------------------- Tareas ----------------------------
# Llenar lista de articulos y organiza las marcas                                           ---LISTO----
# Que al seleccionar no envio, no copie los datos del ultimo cliente                        ---LISTO----
# Agregar compra de articulos por lote                                                      ---LISTO----
# Que no acceda al menu de solicita envio hasta que haya almenos un producto en el carrito  ---LISTO---
# Verificacion de cliente frecuente                                                         ---PENDIENTE----
# Al confirmar compra se reste el stock                                                     ---LISTO----
