import os
#import pickle
#import json


class ContenidoDelInfinito:
    def __init__(self, nombre, semana, contenido):
        self.nombre = nombre
        self.semana = semana
        self.contenido = contenido

    def __setstate__(self, state):
        """COMPLETAR SOLO SI ES CORRESPONDIENTE"""
        params = ("nombre", "semana", "contenido")
        pass

    def __str__(self):
        return "nombre: {} - semana: {} - contenido: {} - sacrificio: {}".format(
            self.nombre,
            self.semana,
            self.contenido,
            self.sacrificio)


def buscar_contenido():
    """Completar"""
    pass


def obtener_contenido(path_alma):
    """Completar"""
    pass


def contenido_hook(contenido):
    """COMPLETAR SOLO SI ES CORRESPONDIENTE"""
    params = ("nombre", "semana", "contenido")
    pass


def deserializar_contenido(path_serializado):
    """Completar"""
    pass


if __name__ == "__main__":
    busqueda = False
    desencriptar = False
    deserializar = False
    try:
        print("Buscando path ...")
        path = buscar_contenido()
        if path:
            print("El camino al contenido del alma es: ", path)
            busqueda = True
        else:
            print("La busqueda del contenido del alma ha fracasado")
    except:
        print("La busqueda del contenido del alma ha fracasado")
    if busqueda:
        try:
            print("Desencriptando el contenido")
            obtener_contenido(path)
            if os.path.exists("desencriptado.alma"):
                print("El sacrificio ha sido aceptado")
                desencriptar = True
            else:
                print("Tu sacrificio no es el correcto")
        except:
            print("Tu sacrificio no es el correcto")
    if desencriptar:
        try:
            print("Deserializando el contenido")
            contenido = deserializar_contenido("desencriptado.alma")
            
            if contenido:
                deserializar = True
                print("Has logrado obtener el contenido")
            else:
                print("No has deserializado bien")
        except:
            print("No has deserializado bien")
    if deserializar:
        print(contenido)
        print(
            "nombre: I/O + Serializacion - semana: 11 - contenido: ['paths', 'bytes', 'serializacion'] - sacrificio: Tu sacrificio")
        print("Si ves esto, y las dos líneas anteriores estan bien, te hago entrega del Contenido del Alma")
