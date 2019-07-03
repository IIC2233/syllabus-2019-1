from libreria_automata import Navegador
from ErrorPersonalizado import ErrorRepetirDestino
from clases import Enemigo, NotEnemigo, Pepino
from random import choice
import pickle


if __name__ == '__main__':
    naveganding = Navegador()
    with open('simular', 'rb') as archivo:
        simulador = pickle.load(archivo)
        for accion in simulador:
            metodo, *args = accion

            if metodo == 'definir_destino':
                naveganding.definir_destino(*args)

            elif metodo == 'agregar_destino':
                naveganding.agregar_destino(*args)

            elif metodo == 'destruir_enemigo':
                naveganding.destruir_enemigo(*args)

            else:
                resultado = naveganding.esquivar_obstaculo(*args)
                print(f'La nave tomo el vector: {resultado} para evadir el obstaculo')
