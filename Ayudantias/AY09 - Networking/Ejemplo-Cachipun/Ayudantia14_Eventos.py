__author__ = "chapito96 & fringlesinthestreet"

class EleccionBotonEvent:

    '''
    Clase para transportar la información al apretar un botón desde la
    Interfaz hacia el Cliente
    '''

    def __init__(self, eleccion):
        self.data = eleccion
        self.status = "eleccion"

class ResultadosEvent:

    '''
    Clase para transportar la información de los resultados desde el Cliente
    hacia la Interfaz
    '''

    def __init__(self, eleccion_1, eleccion_2, result):
        self.eleccion_1 = eleccion_1
        self.eleccion_2 = eleccion_2
        self.result = result
