from threading import Thread, Lock
from time import sleep
from random import random
import json

DATOS = [
    {"nombre": "Michael",
    "objetivo": "robar",
    "poder": 1,
    "tiempo_de_ataque": 1},

    {"nombre": "Juan",
    "objetivo": "movilidad",
    "poder": 6,
    "tiempo_de_ataque": 2},

    {"nombre": "Raul",
    "objetivo": "escudo",
    "poder": 3,
    "tiempo_de_ataque": 3}
]

class Progravenger(Thread):

    """
    Avenger, dependiendo de su objetivo se concentrara en
    áreas diferentes del titán.

    Debe reconocer que hacer dependiendo de su objetivo y 
    reflejarlo en el metodo run.

    Deben cumplirse las fórmulas para calcular los ataques
    segun el enunciado.
    """

    LOCK_INTERACCION = Lock()

    def __init__(self, nombre, objetivo, poder, tiempo_de_ataque, titan):
        super().__init__()
        self.daemon = True
        self.nombre = nombre
        self.objetivo = objetivo
        self.poder = poder
        self.tiempo_de_ataque = tiempo_de_ataque
        self.titan = titan

    def run(self):
        # Aca deberás programar la funcionalidad del
        # Progravenger dependiendo de su objetivo.
        # Recuerda que al robar el elemento el titán muere
        # y el Progravenger deberá dejar de ejecutarse.
        pass

class Threatan(Thread):

    """
    Titan, debe tener properties para escudo y movilidad.
    
    Debe mantenerse con vida hasta que su contenido
    del infinito sea robado.
    """

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.nombre = "Dr. Hernan"
        self._escudo = 100
        self._movilidad = 100
        self.robado = False

    @property
    def escudo(self):
        return self._escudo

    @escudo.setter
    def escudo(self, value):
        self._escudo = max(0, value)

    @property
    def movilidad(self):
        return self._movilidad

    @movilidad.setter
    def movilidad(self, value):
        self._movilidad = max(0, value)

    def run(self):
        # Deberá imprimir cada segundo las estadistica
        # que posee: Escudo y Movilidad
        pass
    
class Batalla(Thread):

    """
    Batalla principal, debe instanciar a los participantes e
    iniciar su funcionamiento.
    """

    def __init__(self):
        super().__init__()
        self.daemon = True
        self.titan = None
        self.progravengers = None

    def run(self):
        self.progravengers_assemble()
        self.attack()
        self.titan.join()


    def progravengers_assemble(self):
        # Debe instanciar al titán y a los progravengers.
        pass

    def attack(self):
        # Debe iniciar los threads
        pass

if __name__ == "__main__":
    BATALLA = Batalla()
    BATALLA.start()
    BATALLA.join()
