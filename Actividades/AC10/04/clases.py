class Enemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100

    def __repr__(self):
        return "Enemigo"

class Pepino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.not_vida = 100

    def __repr__(self):
        return "Pickle Rick"

class NotEnemigo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tampoco_vida = 100

    def __repr__(self):
        return "Not Enemigo"
