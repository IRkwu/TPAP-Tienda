import csv

# Definición de la clase Persona


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre},{self.edad}"

# Función para leer el archivo CSV y retornar un arreglo de personas


def leer_personas_desde_csv(nombre_archivo):
    personas = []
    with open(nombre_archivo, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila con los encabezados
        for row in reader:
            nombre = row[0]
            edad = int(row[1])
            persona = Persona(nombre, edad)
            personas.append(persona)
    return personas


# Llamada a la función para leer el archivo y obtener el arreglo de personas
personas = leer_personas_desde_csv('personas.csv')

# Imprimir los datos de las personas
print("Datos de personas:")
for persona in personas:
    print("Nombre:", persona.nombre)
    print("Edad:", persona.edad)
    print("----------")
