import os

class Extraterrestre:
    def __init__(self, nombre, iu, numeros):
        self.nombre = nombre
        self.iu = iu
        self.numeros = numeros

    def __repr__(self):
        return f"Extraterrestre {self.nombre} con poder: {self.numeros}"


def cargar_extraterrestres(path_extraterrestres):
    """Completar"""
    pass

def simular_guerra(extraterrestres, path_guerra):
    """Completar"""
    pass

def encontrar_maximo_poder(extraterrestres):
    """Completar"""
    pass

if __name__ == "__main__":

    # Cambiar valor si quieres usar datos pequeños o grandes
    usar_mini = True

    if usar_mini:
        path_extraterrestres = os.path.join("data", "extraterrestres_mini.txt")
        path_guerra = os.path.join("data", "guerra_mini.txt")
    else:
        path_extraterrestres = os.path.join("data", "extraterrestres.txt")
        path_guerra = os.path.join("data", "guerra.txt")

    print("Cargando extraterrestres...")
    extraterrestres = cargar_extraterrestres(path_extraterrestres)

    if usar_mini:
        print("Los extraterrestres:")
        print(extraterrestres)

    print("Simulando guerra...")
    simular_guerra(extraterrestres, path_guerra)

    if usar_mini:
        print("Los extraterrestres:")
        print(extraterrestres)

    print("Buscando el mayor ladron de poder...")
    maximo_poder = encontrar_maximo_poder(extraterrestres)
    print(f"El con mayor poder es: {maximo_poder}")