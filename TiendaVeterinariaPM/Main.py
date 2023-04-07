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


def GuardarCSV(articulos):
    with open('Archivos de Datos\ListaArticulos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre', 'Mascota', 'ID', 'Marca', 'Precio por unidad',
                        'Stock', 'Descripción', 'Categoría', 'Precio por lote', 'Límite crítico'])
        for articulo in articulos:
            writer.writerow([articulo.get_nombre(), articulo.get_mascota(), articulo.get_id(), articulo.get_marca(), articulo.get_precio_por_unidad(
            ), articulo.get_stock(), articulo.get_descripcion(), articulo.get_categoria(), articulo.get_precio_por_lote(), articulo.get_limite_critico()])


def CargarCSV(ruta_archivo):
    lista_articulos = []
    with open(ruta_archivo, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico = row
            articulo = Articulos(nombre, mascota, id, marca, int(precio_por_unidad), int(
                stock), descripcion, categoria, int(precio_por_lote), int(limite_critico))
            lista_articulos.append(articulo)
    return lista_articulos


def AgregarArticuloo(nombre, mascota, id, marca, precio_por_unidad, stock, descripcion, categoria, precio_por_lote, limite_critico):
    articulo = Articulos(nombre, mascota, id, marca, precio_por_unidad,
                         stock, descripcion, categoria, precio_por_lote, limite_critico)
    ListaArticulos.append(articulo)
    GuardarCSV(ListaArticulos)
    print("El artículo se agregó correctamente a la lista.")


# Cargar archivo CSV y llenar el arreglo de Articulos
ListaArticulos = CargarCSV('Archivos de Datos\ListaArticulos.csv')


def MostrarListaArticulos():
    contador = 1
    for articulo in ListaArticulos:
        print("Articulo:", contador, "\n[Nombre]:", articulo.get_nombre(), "[Mascota:]", articulo.get_mascota(), "[ID]:", articulo.get_id(), "[Marca]:", articulo.get_marca(), "[Precio Unidad]:", int(articulo.get_precio_por_unidad()), "[Stock]:", int(
            articulo.get_stock()), "[Descripcion]:", articulo.get_descripcion(), "[Categoría]:", articulo.get_categoria(), "[Precio Lote]:", int(articulo.get_precio_por_lote()), "[Limite Crítico]:", int(articulo.get_limite_critico()))
        contador += 1


# Ejemplo mostrar articulos
MostrarListaArticulos()

########### Verifica si el archivo es el módulo principal ###########
if __name__ == '__main__':
    # Llamada al método main
    main()
