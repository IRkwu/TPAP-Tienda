import sys
from Articulos import Articulos
from Carrito import Carrito

ListaArticulos = Articulos.CargarCSV('Archivos de Datos\ListaArticulos.csv')

def mostrar_menu():
    print("\n>>> Tienda de artículos para Mascotas")
    print("1. Ver productos disponibles")
    print("2. Agregar un producto del carrito")
    print("3 Eliminar un producto del carrito")
    print("4. Ver productos en el carrito")
    print("5. Salir")
    
    
while True:
    mostrar_menu()
    opcion = input("\nIngrese el número de la opción")
    if opcion == "1":
        Articulos.MostrarListaArticulos()
    elif opcion == "2":
        indice = int(input("Ingrese el numero del producto a agregar"))
    elif opcion == "3":
        indice = int(input("Ingrese el numero del producto a eliminar"))
    elif opcion == "4":
        print("Articulos del carrito:")
    elif opcion == "5":
        print("Gracias por la visita")
        sys.exit()
    else:
        print("\nOpción incorrecta. Intente nuevamente")
        