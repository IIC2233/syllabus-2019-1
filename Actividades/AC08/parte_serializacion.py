import json
import os
import pickle
import random

# paths de los archivos
CARATTERISTICAS_CAMMINO = 'caratteristicas.json'
OPERAS_CAMMINO = 'operas.json'


# Debes comenzar a editar a partir de aquí
class Obra:
    """
    Clase para las Obras de Antonini Da Ossa
    """

    def __init__(self, nome=None, autore=None, anno=None, posto=None,
                 stile=None, descrizione=None):

        self.nome = nome
        self.autore = autore
        self.anno = anno
        self.posto = posto
        self.stile = stile
        self.descrizione = descrizione

    def __getstate__(self):
        """
        Serializa las obras, agregando el atributo 'messaggio' al diccionario.
        """

        pass


def cargar_obras(ruta_obras):
    """

    Funcion que carga las obras con las características pedidas,
    y luego entrega la lista de Obras.
    :param ruta_obras: Path de archivo de obras a cargar

    NOTA: DEBE USARSE la funcion obras_hook() como
     object hook para hacer el filtrado

    """
    pass


def obras_hook(dict_obras):
    """
    Object hook que hace los objetos de la clase Obra y los añade a una lista.
    HINT: Utilizar aquí el archivo caratteristicas ;)
    """

    pass


def generar_mensaje(lista_obras):
    """
    Serializa las obras y las guarda en archivos
    :param lista_obras: Lista de objetos de tipo obra cargados.
    """

    pass


def mensaje_bonus(lista_obras):
    """
    Encuentra el treceavo caracter de cada descripción de la lista de obras
    de Antonini Da Ossa
    :param lista_obras: Lista de objetos de tipo obra cargados.
    """

    pass


# Ejecutando
if __name__ == "__main__":

    # Está prohibido modificar cualquier parte de esta sección

    print("\nCargando las obras...")
    lista_operas = cargar_obras(OPERAS_CAMMINO)

    print("\nCodificando los mensajes...")
    generar_mensaje(lista_operas)

    print("\nObteniendo santo video...")
    parte_1 = mensaje_bonus(lista_operas)

    print("\nLa primera parte del santo video es {}".format(parte_1))
