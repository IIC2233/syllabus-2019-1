class Jefe:
    def __init__(self, ataque):
        self.ataque = ataque

    def tiempo(self, progravenger):
        """Completar"""
        pass

    def poder(self, progravenger):
        """Completar"""
        pass

    def realidad(self, progravenger):
        """Completar"""
        pass


class Programmer:
    def __init__(self, vida):
        self.vida_max = vida
        self._vida = vida
    
    def decodificar(self, enemigo):
        """Completar"""
        pass

    @property
    def vida(self):
        """Completar"""
        pass

    @vida.setter
    def vida(self, value):
        """Completar"""
        pass



class Avenger:
    def __init__(self, fuerza, arma):
        self.fuerza = fuerza
        self.arma = arma

    @property
    def ataque(self):
        """Completar"""
        pass


class Progravenger(Avenger, Programmer):
    def __init__(self, vida, fuerza, arma, nombre):
        Avenger.__init__(self, fuerza, arma)
        Programmer.__init__(self, vida)

        self.nombre = nombre
    
    def atacar(self, henry):
        """Completar"""
        pass


class DrHenry(Jefe, Programmer):
    def __init__(self, vida, ataque):
        Jefe.__init__(self, ataque)
        Programmer.__init__(self, vida)

    def atacar(self, progravenger):
        """Completar"""
        pass
