from TiendaVeterinariaPM import *


# Guardado de archivo en excel

articulos = [
    Articulos("Cama Iglu", "Gato", "A12", "Catto", 28900, 30,
              "Cama para gatos con forma de Iglu", "Camas", 130050, 3),
    Articulos("Cama Dona", "Perro", "A13", "Doggo", 24900, 30,
              "Cama para perros con forma de dona", "Camas", 112050, 3),
]


def GuardarExcel(articulo):
    # Dataframe para articulo
    df = pd.DataFrame({
        'Nombre': [articulo.get_nombre() for articulo in articulos],
        'Mascota': [articulo.get_mascota() for articulo in articulos],
        'ID': [articulo.get_id() for articulo in articulos],
        'Marca': [articulo.get_marca() for articulo in articulos],
        'Precio por unidad': [articulo.get_precio_por_unidad() for articulo in articulos],
        'Stock': [articulo.get_stock() for articulo in articulos],
        'Descripcion': [articulo.get_descripcion() for articulo in articulos],
        'Categoria': [articulo.get_categoria() for articulo in articulos],
        'Precio por lote': [articulo.get_precio_por_lote() for articulo in articulos],
        'Limite critico': [articulo.get_limite_critico() for articulo in articulos]
    })

    # Guardado del dataframe
    writer = pd.ExcelWriter(
        'Archivos de Datos\ListaArticulos.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Articulo')
    writer._save()


GuardarExcel(articulos)
