from datetime import datetime


class Mascota:
    def __init__(self, id, nombre, especie, raza, fechaNacimiento, sexo, peso, tamaño, volumen, fichaMedica):
        self.__id = id
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__fechaNacimiento = fechaNacimiento
        self.__sexo = sexo
        self.__peso = peso
        self.__tamaño = tamaño
        self.__volumen = volumen
        self.__fichaMedica = fichaMedica

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def get_fechaNacimiento(self):
        return self.__fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento

    def get_sexo(self):
        return self.__sexo

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño

    def get_volumen(self):
        return self.__volumen

    def set_volumen(self, volumen):
        self.__volumen = volumen

    def get_fichaMedica(self):
        return self.__fichaMedica

    def set_fichaMedica(self, fichaMedica):
        self.__fichaMedica = fichaMedica

    def agregar_historial_medico(self, historial):
        self.__fichaMedica.append(historial)
