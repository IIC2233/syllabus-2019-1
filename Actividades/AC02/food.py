from abc import ABC
import random


# Completar las clases donde corresponda #


class Pizza:
    def __init__(self, ingredientes):
        self._calidad = random.randint(50, 200)
        # Rellenar Aquí
        pass

    def revisar_tiempo(self):
        # Rellenar Aquí
        pass

    def revisar_ingredientes(self):
        # Rellenar Aquí
        pass

    @property
    def calidad(self):
        return self._calidad

    @calidad.setter  # Se controla que la calidad no sea negativa
    def calidad(self, valor):
        self._calidad = max(0, valor)


class Bebestible(ABC):
    def __init__(self):
        self._calidad = random.randint(50, 150)

    @property
    def calidad(self):
        return self._calidad

    @calidad.setter  # Se controla que la calidad no sea negativa
    def calidad(self, valor):
        self._calidad = max(0, valor)


class Plato:
    def __init__(self):
        self.pizza = None
        self.bebestible = None

# Rellenar Aquí con las nuevas clases #
