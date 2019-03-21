from food import Pizza, Gaseosa, Agua, Plato
from abc import ABC, abstractmethod
import random


# Completar las clases donde corresponda #


class Personalidad(ABC):
    def reaccionar(self, plato):
        # Rellenar aquí
        pass

    @abstractmethod
    def feliz(self):
        pass

    @abstractmethod
    def molesto(self):
        pass


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Rellenar Aquí con las nuevas clases #
