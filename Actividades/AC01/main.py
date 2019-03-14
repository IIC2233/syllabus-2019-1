"""
######################################
IMPORTANTE: LEER MUY BIEN EL ENUNCIADO
ANTES DE EMPEZAR A PROGRAMAR
######################################
"""

"""
Aquí debes importar las estructuras que estimes convenientes para la actividad
"""
from random import sample

"""
En esta sección debes completar las funciones para cargar los archivos al sistema.

"""

def cargar_emociones(ruta_archivo_emociones):
    """
    Esta función carga las emociones de los cims y los retorna en una estructura.
    """
    pass

def cargar_cims(ruta_archivo_cims, ruta_archivo_emociones):
    """
    Esta función carga los cims y los retorna en una estructura.
    """
    pass

def cargar_familias(ruta_archivo_familias, cims):
    """
    Esta función carga las familias y las retorna en una estructura.
    """
    pass

"""
En esta sección deberás completar las funciones para relacionar a los cims cargados anteriormente.

"""

def interactuar(id_cim_1, id_cim_2, cims):
    """
    Esta función se encarga de hacer interactuar a dos cims.
    """
    pass

def modificar_familia(id_cim, id_familia, cims, familias, agregar=True):
    """
    Esta función se encarga de agregar/eliminar a un cim según la familia indicada
    """
    pass

def emociones_comunes_familia(id_familia, familias):
    """
    Esta función retorna las emociones que todos los miembros de una familia tienen en común
    """
    pass

def acciones_mas_repetidas(cims):
    """
    Esta función retorna las aaciones que mas se repiten junto con su cantidad
    """
    pass

"""
Aquí puedes probar tus funciones al llamarlas con distintos valores
"""

if __name__ == '__main__':
    print("----------------------")
    print(" Bienvenido a DCCIMS")
    print("----------------------")

    print("----------------------")
    print("CARGA DE DATOS")
    print("----------------------")

    # DESCOMENTAR SIGUIENTES LINEAS PARA TESTEAR CARGA DE DATOS
    # cims = cargar_cims('cims.txt', 'emociones.txt')
    # familias = cargar_familias('familias.txt', cims)
    # Resultado esperado: no debe aparecer ningún mensaje de error

    print("----------------------")
    print("INTERACCIONES")
    print("----------------------")

    # Primera interacción:
    #     El cim de id 0 (Enzo Tamburini de 23 años) interactúa con el cim de id 1 (Daniela Concha de 21 años)
    # Resultado esperado: 
    #     Enzo Tamburini pierde la acción "carisma" y gana la acción "jardinería"
    #     Daniela Concha pierde la acción "jardinería" y gana la acción "carisma"

    # DESCOMENTAR SIGUIENTE LINEA PARA TESTEAR INTERACCION 1
    # interactuar("0", "1", cims)

    # Segunda interacción:
    #     El cim de id 2 (Pablo Olea de 21 años) interactúa con el cim de id 19 (Matthew Nelson de 22 años)
    # Resultado esperado: 
    #     Pablo Olea ya no tiene la acción "ejercicio físico" y gana una emoción al azar de Matthew Nelson
    #     Matthew Nelson ya no tiene la acción "ejercicio físico" y gana una emoción al azar de Pablo Olea

    # DESCOMENTAR SIGUIENTE LINEA PARA TESTEAR INTERACCION 2
    # interactuar("2", "19", cims)

    # Tercera interacción:
    #     El cim de id 3 (Dante Pinto de 20 años) es removido de la familia de id 12
    # Resultado esperado: 
    #     La familia de id 12 ya no tiene a Dante Pinto en su estructura.

    # DESCOMENTAR SIGUIENTE LINEA PARA TESTEAR INTERACCION 3
    # modificar_familia("3", "12", cims, familias, False)

    # Cuarta interacción:
    #     El cim de id 3 (Dante Pinto de 20 años) es agregado a la familia de id 12
    # Resultado esperado: 
    #     La familia de id 12 tiene guardado a Dante Pinto en su estructura.
 
    # DESCOMENTAR SIGUIENTE LINEA PARA TESTEAR INTERACCION 4
    # modificar_familia("3", "12", cims, familias, True)

    print("----------------------")
    print("CONSULTAS")
    print("----------------------")
  
    # Consulta 1:
    #     La familia de id 1 ve las emociones que tengan todos los miembros en común
    # Resultado esperado: 
    #     una estructura con las emociones: "contento", "enfadado"

    # DESCOMENTAR SIGUIENTES LINEA PARA TESTEAR CONSULTA 1
    # resultado = emociones_comunes_familia("1", familias)
    # print(resultado)

    # Consulta 2:
    #     Se ve cuales son las acciones más repetidas
    # Resultado esperado: 
    #     una lista de la forma: [["canto", "destreza manual", "violín"], 15]

    # DESCOMENTAR SIGUIENTE LINEA PARA TESTEAR CONSULTA 2
    # print(acciones_mas_repetidas(cims))
