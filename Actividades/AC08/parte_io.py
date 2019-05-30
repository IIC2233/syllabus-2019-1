import random

# paths de "La Gioconcha"
GIOCONCHA = "la_gioconcha.jpg"


# Debes comenzar a editar a partir de aquí
def cargar_imagen(ruta):
    """
    Función que se encarga de cargar la imagen y retornarla
    en forma de bytearray

    :param ruta: Path de la imagen que se quiere cargar
    """

    pass


def esconder_imagen(imagen):
    """
    Función que se encarga de aplicar el algoritmo de codificado a la imagen.

    :param imagen: Bytearray de la imagen que se quiere modificar
    """

    pass


def guardar_imagen(imagen):
    """
    Función que se encarga de guardar un bytearray como "imagen"

    :param imagen: Bytearray de la imagen a guardar
    """

    pass

def arreglar_imagen(ruta_imagen):
    """
    ESTA FUNCIÓN NO ES EVALUADA! Solamente es para encontrar el mensaje
    secreto.
    Función que invierte el proceso seguido por esconder_imagen()

    :param ruta_imagen: Path de imagen escondida a arreglar.
    """

    pass


# Ejecutando
if __name__ == "__main__":

    # Está prohibido modificar cualquier parte de esta sección

    print("\nCodificando a \"La Gioconcha!\"")
    try:
        GIOCONCHA_CODIFICATO = esconder_imagen(cargar_imagen(GIOCONCHA))
        guardar_imagen(GIOCONCHA_CODIFICATO)

        print("Imagen codificada!")
    except FileNotFoundError:
        print("ERROR: la imagen no se encuentra en el directorio "
              + "especificado.")
