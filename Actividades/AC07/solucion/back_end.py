import os
from itertools import cycle
from random import choice
from PyQt5.QtCore import pyqtSignal, QObject

class MensajeJuego:
    
    def __init__(self, juego):
        self.carta_tirada = juego.carta_tirada
        self.carta_contada = juego.carta_contada
        self.nombre_1 = juego.nombre_jugador_1
        self.nombre_2 = juego.nombre_jugador_2
        self.mazo_1 = len(juego.mazo_jugador_1)
        self.mazo_2 = len(juego.mazo_jugador_2)
        self.juego_comenzo = juego.juego_comenzo

class Programadito(QObject):

    senal_nombres = pyqtSignal(str, str)
    senal_reinicio = pyqtSignal()
    senal_comienza = pyqtSignal()
    senal_tirar_carta = pyqtSignal(int)
    senal_juntar_cartas = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.nombre_jugador_1 = ""
        self.nombre_jugador_2 = ""
        self.senal_actualizar = None
        self.reiniciar_juego()
        
        self.senal_nombres.connect(self.ingresar_nombres)
        self.senal_reinicio.connect(self.reiniciar_juego)
        self.senal_comienza.connect(self.comenzar_juego)
        self.senal_tirar_carta.connect(self.tirar_carta)
        self.senal_juntar_cartas.connect(self.juntar_cartas)

    def setear_senales(self, ventana_inicial, ventana_juego):
        self.senal_comenzar_juego = ventana_inicial.senal_comenzar_juego
        self.senal_mostrar_mensaje_error = ventana_inicial.senal_mostrar_mensaje_error
        self.senal_ganador = ventana_juego.senal_ganador
        self.senal_actualizar = ventana_juego.senal_actualizar

    def reiniciar_juego(self):
        self.juego_comenzo = False
        self.turno_primero = True
        self.carta_contada = None
        self.carta_tirada = None
        self.cartas = cycle(["ace", "2", "3", "4", "5", "6", "7",
                            "8", "9", "10", "jack", "queen", "king"])
        self.mazo_jugador_1 = os.listdir("cartas")
        self.mazo_jugador_1.remove("jugador_1.png")
        self.mazo_jugador_1.remove("jugador_2.png")
        self.mazo_jugador_1.remove("black_joker.png")
        self.mazo_jugador_1.remove("red_joker.png")
        self.mazo_jugador_2 = self.mazo_jugador_1.copy()
        self.cartas_pozo = []

        self.actualizar_interfaz()

    def comenzar_juego(self):
        self.reiniciar_juego()
        self.juego_comenzo = True
        self.actualizar_interfaz()

    def ingresar_nombres(self, nombre_1, nombre_2):
        if nombre_1 == "" or nombre_2 == "":
            self.senal_mostrar_mensaje_error.emit(1)
        elif not nombre_1.isalnum() or not nombre_2.isalnum():
            self.senal_mostrar_mensaje_error.emit(2)
        elif nombre_1 == nombre_2:
            self.senal_mostrar_mensaje_error.emit(3)
        else:
            self.nombre_jugador_1 = nombre_1
            self.nombre_jugador_2 = nombre_2
            self.senal_comenzar_juego.emit()
            self.actualizar_interfaz()

    def tirar_carta(self, n_jugador):
        if not self.juego_comenzo:
            return
        if n_jugador == 1:
            if not self.turno_primero:
                return
            mazo = self.mazo_jugador_1
            jugador = self.nombre_jugador_1
        else:
            if self.turno_primero:
                return
            mazo = self.mazo_jugador_2
            jugador = self.nombre_jugador_1
        
        self.turno_primero = not self.turno_primero
        self.carta_contada = next(self.cartas)

        self.carta_tirada = choice(mazo)
        mazo.remove(self.carta_tirada)
        self.cartas_pozo.append(self.carta_tirada)
        
        if len(mazo) == 0:
            self.senal_ganador.emit(jugador, 1)
            self.juego_comenzo = False
    
        self.actualizar_interfaz()

    def juntar_cartas(self, jugador):
        if not self.juego_comenzo:
            return
        if self.carta_contada in self.carta_tirada:
            if jugador == 1:
                self.senal_ganador.emit(self.nombre_jugador_1, 2)
                self.mazo_jugador_2.extend(self.cartas_pozo)
                self.turno_primero = False
            else:
                self.senal_ganador.emit(self.nombre_jugador_2, 2)
                self.mazo_jugador_1.extend(self.cartas_pozo)
                self.turno_primero = True
        else:  # Jugador presiono boton cuando no correspondia
            if jugador == 1:
                self.senal_ganador.emit(self.nombre_jugador_1, 3)
                self.mazo_jugador_1.extend(self.cartas_pozo)
                self.turno_primero = True
            else:
                self.senal_ganador.emit(self.nombre_jugador_2, 3)
                self.mazo_jugador_2.extend(self.cartas_pozo)
                self.turno_primero = False
        self.cartas_pozo = []
        self.carta_tirada = None
        self.actualizar_interfaz()
    
    def actualizar_interfaz(self):
        if self.senal_actualizar:
            estado = MensajeJuego(self)
            self.senal_actualizar.emit(estado)
    