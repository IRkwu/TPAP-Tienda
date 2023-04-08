import sys
from Articulos import Articulos, ListaArticulos
from Carrito import Carrito, Carrito_Cliente
from Venta import Venta
from Envio import Envio

def llenadoDeCarrito():
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
                    Carrito_Cliente.AgregarArticulo(i)
                    comprobacion = True
                    print("Producto ingresado correctamente")
                else:
                    print("No hay stock del producto")
                    comprobacion = True
            i += 1

        if not comprobacion:
            print("Error, ID no existe")

        print("\nDesea agregar otro producto?\n")
        print("S = si // N = No")
        opcion = input("Opcion: ")
        comprobacion = False

        if opcion.lower() != 's':
            break
        
        
opcionMenu = 0

while True:
    print("\n --MENU-- \n")
    print("1.- Ver productos")
    print("2.- Seleccionar productos")
    print("3.- Realizar compra")
    print("4.- Ver envio")
    print("5.- Mostrar artículos del carrito")
    print("6.- Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        Articulos.MostrarListaArticulos()
    elif opcion == "2":
        llenadoDeCarrito()
    elif opcion == "3":
        Venta.ConfirmarVenta()
    elif opcion == "4":
        print(Envio.mostrarEnvio())
    elif opcion == "5":
        Carrito_Cliente.MostrarArticulosCarrito()
    elif opcionMenu == "6":
        print("Saliendo del Menu")
        break
    else:
        print("Opcion no válida. Intente de nuevo.")
