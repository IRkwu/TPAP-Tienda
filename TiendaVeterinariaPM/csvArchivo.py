import csv


class csvArch:
    def __init__(self):
        pass
    
    @classmethod
    def insertar(cls, archivo, obj):
        with open(archivo,"a",newline="") as w:
            lista = obj.string().split(",")
            write = csv.writer(w, delimiter=",") 
            write.writerow(lista)
            
    @classmethod
    def modificar(cls, archivo, posFila, posElemento, objAux):
        with open(archivo, "r", encoding="latin1") as w:
            lector = csv.reader(w, delimiter=",")
            lista_delistas = []
            for i, lista in enumerate(lector):
                if i == (posFila+1):
                    try:
                        lista[posElemento] = objAux
                    except IndexError:
                        return False
                lista_delistas.append(lista)

        with open(archivo, "w", newline="") as w:
            escritor = csv.writer(w, delimiter=",")
            for lista in lista_delistas:
                escritor.writerow(lista)
        return True