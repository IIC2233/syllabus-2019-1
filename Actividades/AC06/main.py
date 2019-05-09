import threading
import time
import random


def desencriptar(texto):
    """"Funcion para desencriptar el problema dada por los ayudantes"""
    murci = "murcielago"
    numeros = "0123456789"
    nuevo_texto = ""

    for letras in texto:
        if letras in murci:
            nueva_letra = murci.index(letras)
            nuevo_texto += str(nueva_letra)
        elif letras in numeros:
            nueva_letra = numeros.index(letras)
            nuevo_texto += str(murci[int(nueva_letra)])
        else:
            nuevo_texto += letras
    return nuevo_texto


class Dragon(threading.Thread):

    def __init__(self):
        super().__init__()
        pass

    def comer(self):
        pass

    def run(self):
        pass

    def __str__(self):
        pass


class Dany:
    lock = "esto podría ser un lock..."
    def __init__(self):

        pass

    def convencer(self):
        pass


class Jinete(threading.Thread):
    lock = "esto podria ser un lock..."

    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        pass

    def run(self):
        pass


class Viaje(threading.Thread):
    def __init__(self):
        super().__init__()
        pass

    def agregar(self, nombre_dragon, nombre_jinete):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    # Aca deben instanciar las distintas clases y empezar el rescate
    pass














