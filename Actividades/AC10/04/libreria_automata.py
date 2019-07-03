from ErrorPersonalizado import ErrorRepetirDestino
from clases import Enemigo

class Navegador:
    def __init__(self):
        # No modifiques este metodo ¬¬
        self.destinos = dict()

    def signo(self, valor):
        # No modifiques este metodo tampoco ¬¬
        if valor > 0:
            return 1
        elif valor == 0:
            return 0
        else:
            return -1

    def definir_destino(self, nombre):
        print(f'Definiendo destino hacia {nombre}')
        return self.destinos[nombre]

    def agregar_destino(self, nombre, posicion):
        print(f'Agregando destino {nombre} en {posicion}')
        self.destinos[nombre] = posicion

    def destruir_enemigo(self, enemigo):
        print('Pium pium!')
        enemigo.vida = 0

    def esquivar_obstaculo(self, posicion_obstaculo, distancia):
        # Este metodo tambien lo llaman e_o en el enunciado
        # Agrega las excepciones antes de lo que viene a continuacion
        print(f'Esquivando obstaculo en {posicion_obstaculo}')
        x = self.signo(posicion_obstaculo[0]) * -1
        y = self.signo(posicion_obstaculo[1]) * -1
        velocidad = 1 // distancia
        if self.signo(velocidad) == 0:
            velocidad = 1

        return (x, y, velocidad)
