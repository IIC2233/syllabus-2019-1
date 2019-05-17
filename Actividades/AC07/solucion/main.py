import sys
from PyQt5.QtWidgets import QApplication
from front_end import VentanaInicial, VentanaJuego
from back_end import Programadito

if __name__ == "__main__":
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    a = QApplication(sys.argv)

    juego = Programadito()
    ventana_inicial = VentanaInicial()
    ventana_juego = VentanaJuego()

    juego.setear_senales(ventana_inicial, ventana_juego)
    ventana_juego.setear_senales(juego)
    ventana_inicial.setear_senales(juego, ventana_juego)

    ventana_inicial.show()
    sys.exit(a.exec())