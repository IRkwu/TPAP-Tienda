import datetime
from Carrito import Carrito, Carrito_Cliente
from Cliente import Cliente, ListaClientes
from Boleta import Boleta, HistorialBoletas
from Usuario import Usuario, Lista_Usuarios
from Articulos import Articulos, ListaArticulos
from Envio import Envio
import csv


class Venta:
    def __init__(self):
        self.__fecha_venta = datetime.now()
        self.__venta_confirmada = False
        self.__boletas = []

    def ConfirmarVenta(self):
        # Agregar boleta al historial de boletas
        Boleta.AgregarBoleta(None, ListaClientes[-1].get_id(), Lista_Usuarios[1].get_nombres(), ListaClientes[-1].get_nombres()+" "+ListaClientes[-1].get_apellidoPaterno(), datetime.datetime.now().date(
        ), Carrito_Cliente.MostrarArticulosBoleta(), Carrito_Cliente.CalcularTotal()+Envio.CalcularDescuentoEnvio(Carrito_Cliente.CalcularTotal()), Envio.CalcularDescuentoEnvio(Carrito_Cliente.CalcularTotal()))
        # Imprimir la ultima boleta agregada
        HistorialBoletas[-1].imprimir_boleta()
        # Vaciar el carrito para que el nuevo cliente ingrese los productos

        Articulos.GuardarCSV_Articulos(None, ListaArticulos)

        Carrito_Cliente.VaciarCarrito()

    def get_fecha_venta(self):
        return self.__fecha_venta

    def set_fecha_venta(self, fecha_venta):
        self.__fecha_venta = fecha_venta

    def get_venta_confirmada(self):
        return self.__venta_confirmada

    def set_venta_confirmada(self, venta_confirmada):
        self.__venta_confirmada = venta_confirmada

    # Funcion para guardar el Historial de las boletas
    def GuardarCSV_Boletas(self, nombre_archivo):
        with open('Archivos de Datos\HistorialBoletas.csv', 'w', newline='') as csvfile:
            writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['Nombre vendedor', 'Nombre cliente',
                            'Fecha venta', 'Articulos', 'Total', 'Costo envio'])
            for boleta in self.__boletas:
                writer.writerow([boleta.get_nombre_vendedor(), boleta.get_nombre_cliente(
                ), boleta.get_fecha_venta(), boleta.get_articulos(), boleta.get_total(), boleta.get_costo_envio()])
