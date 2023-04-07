from Carrito import Carrito


def main():
    opcionMenu = 0

    while opcionMenu < 1 or opcionMenu > 4:
        print("\n --MENU-- \n")
        print("1.- Ver productos")
        print("2.- Seleccionar productos")
        print("3.- Realizar compra")
        print("4.- Ver envio")
        print("5.- Salir")
        opcionMenu = int(input("Opcion: "))

        if opcionMenu == 1:
            MostrarListaArticulos()
            opcionMenu = 0
        elif opcionMenu == 2:
            llenadoDeCarrito()
            opcionMenu = 0
        elif opcionMenu == 3:
            llenadoDeDatosDeEnvio()
            opcionMenu = 0
        elif opcionMenu == 4:
            print(envi.toString())
            opcionMenu = 5
        elif opcionMenu == 5:
            opcionMenu = 1


def llenadoDeCarrito():
    id = 0
    opcion = ''
    comprobacion = False

    while True:
        print("\n --INGRESE EL ID DE LOS PRODUCTOS A COMPRAR-- \n")
        id = int(input("ID: "))

        for articulo in ListaArticulos:
            if id == articulo.get_id:
                comprobacion = True
                AgregarArticulo(ListaArticulos[id])

        if comprobacion:
            print("Producto ingresado correctamente")
        else:
            print("Error, ID no existe")

        print("\n Desea agregar otro producto?\n")
        print("S = si // N = No")
        opcion = input("Opcion: ")
        comprobacion = False

        if opcion.lower() != 's':
            break
