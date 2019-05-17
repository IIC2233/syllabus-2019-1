from os import path
from PyQt5.QtWidgets import QLabel, QWidget, QLineEdit, \
    QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from back_end import MensajeJuego
    
class VentanaInicial(QWidget):

    senal_comenzar_juego = pyqtSignal()
    senal_mostrar_mensaje_error = pyqtSignal(int)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

        self.senal_comenzar_juego.connect(self.comenzar_juego)
        self.senal_mostrar_mensaje_error.connect(self.mostrar_mensaje)

    def setear_senales(self, juego, ventana_juego):
        self.senal_nombres = juego.senal_nombres
        self.senal_abre_ventana_juego = ventana_juego.senal_abre_ventana_juego

    def inicializa_GUI(self):
        self.setWindowTitle("Programadito")

        self.label_mensaje = QLabel("Mensaje: ")
        self.layout_principal = QVBoxLayout()

        self.boton_empezar= QPushButton("Empezar")
        self.boton_empezar.clicked.connect(self.ingresar_nombres)

        self.label_input_1 = QLabel("Nombre jugador 1:")
        self.label_input_2 = QLabel("Nombre jugador 2:")

        self.input_jugador_1 = QLineEdit()
        self.input_jugador_2 = QLineEdit()
        self.input_jugador_1.setPlaceholderText("Ingrese nombre jugador")
        self.input_jugador_2.setPlaceholderText("Ingrese nombre jugador")

        self.layout_input_1 = QHBoxLayout()
        self.layout_input_2 = QHBoxLayout()

        self.layout_input_1.addWidget(self.label_input_1)
        self.layout_input_1.addWidget(self.input_jugador_1)

        self.layout_input_2.addWidget(self.label_input_2)
        self.layout_input_2.addWidget(self.input_jugador_2)

        self.layout_principal.addLayout(self.layout_input_1)
        self.layout_principal.addLayout(self.layout_input_2)

        self.layout_principal.addWidget(self.label_mensaje)
        self.layout_principal.addWidget(self.boton_empezar)

        self.setLayout(self.layout_principal)

    def ingresar_nombres(self):
        input_jugador_1 = self.input_jugador_1.text()
        input_jugador_2 = self.input_jugador_2.text()
        self.senal_nombres.emit(input_jugador_1, input_jugador_2)

    def comenzar_juego(self):
        self.senal_abre_ventana_juego.emit()
        self.hide()

    def mostrar_mensaje(self, tipo):
        if tipo == 1:
            mensaje = "Mensaje: Algún jugador no tiene nombre"
        elif tipo == 2:
            mensaje = "Mensaje: Se he ingresado un caracter invalido"
        elif tipo == 3:
            mensaje = "Mensaje: Los jugadores tienen nombre iguales"
        self.label_mensaje.setText(mensaje)

class VentanaJuego(QWidget):

    senal_abre_ventana_juego = pyqtSignal()
    senal_ganador = pyqtSignal(str, int)
    senal_actualizar = pyqtSignal(MensajeJuego)
    
    def __init__(self, *args):
        super().__init__(*args)
        self.inicializa_GUI()

        self.senal_abre_ventana_juego.connect(self.show)
        self.senal_ganador.connect(self.mensaje_ganador)
        self.senal_actualizar.connect(self.actualizar_ventana)

    def setear_senales(self, juego):
        self.senal_nombres = juego.senal_nombres
        self.senal_reinicio = juego.senal_reinicio
        self.senal_comienza = juego.senal_comienza
        self.senal_tirar_carta = juego.senal_tirar_carta
        self.senal_juntar_cartas = juego.senal_juntar_cartas

    def inicializa_GUI(self):
        self.setWindowTitle("Programadito")

        self.layout_principal = QVBoxLayout()

        self.label_mensaje = QLabel("Mensaje: ")
        self.layout_principal.addWidget(self.label_mensaje)

        self.layout_superior = QHBoxLayout()
        
        self.boton_reiniciar = QPushButton("Reiniciar")
        self.boton_empezar = QPushButton("Empezar")
        self.boton_reiniciar.clicked.connect(self.reiniciar)

        self.boton_empezar.clicked.connect(self.empezar_juego)

        self.layout_superior.addWidget(self.boton_empezar)
        self.layout_superior.addWidget(self.boton_reiniciar)

        self.layout_intermedio = QHBoxLayout()

        self.label_carta = QLabel()

        self.layout_intermedio.addStretch()
        self.layout_intermedio.addWidget(self.label_carta)
        self.layout_intermedio.addStretch()

        self.layout_inferior = QHBoxLayout()

        self.layout_jugador_1 = QVBoxLayout()
        self.layout_jugador_2 = QVBoxLayout()

        self.label_jugador_1 = QLabel()
        self.imagen_jugador_1 = QLabel()
        self.contador_jugador_1 = QLabel()
        self.label_jugador_2 = QLabel()
        self.imagen_jugador_2 = QLabel()
        self.contador_jugador_2 = QLabel()

        self.imagen_jugador_1.setPixmap(
            QPixmap(path.join("cartas", "jugador_1.png")).scaled(100, 40))
        self.imagen_jugador_2.setPixmap(
            QPixmap(path.join("cartas", "jugador_2.png")).scaled(100, 40))

        self.layout_jugador_1.addWidget(self.imagen_jugador_1)
        self.layout_jugador_1.addWidget(self.label_jugador_1)
        self.layout_jugador_1.addWidget(self.contador_jugador_1)
        self.layout_jugador_1.addStretch(1)

        self.layout_jugador_2.addWidget(self.imagen_jugador_2)
        self.layout_jugador_2.addWidget(self.label_jugador_2)
        self.layout_jugador_2.addWidget(self.contador_jugador_2)
        self.layout_jugador_2.addStretch(1)
        
        self.imagen_carta = QLabel()
        self.imagen_carta.setPixmap(
            QPixmap(path.join("cartas", "red_joker.png")).scaled(150, 200))
        
        self.layout_inferior.addLayout(self.layout_jugador_1)
        self.layout_inferior.addWidget(self.imagen_carta)
        self.layout_inferior.addLayout(self.layout_jugador_2)

        self.layout_contenedor = QVBoxLayout()

        self.layout_contenedor.addLayout(self.layout_superior)
        self.layout_contenedor.addLayout(self.layout_intermedio)
        self.layout_contenedor.addLayout(self.layout_inferior)

        self.layout_principal.addLayout(self.layout_contenedor)
        self.setLayout(self.layout_principal)

    def keyPressEvent(self, qkey_event):
        if qkey_event.key() == Qt.Key_S:
            self.senal_tirar_carta.emit(1)
        elif qkey_event.key() == Qt.Key_K:
            self.senal_tirar_carta.emit(2)
        elif qkey_event.key() == Qt.Key_W:
            self.senal_juntar_cartas.emit(1)
        elif qkey_event.key() == Qt.Key_I:
            self.senal_juntar_cartas.emit(2)

    def reiniciar(self):
        self.label_mensaje.setText("Mensaje: ¡Presiona Empezar para empezar!")
        self.senal_reinicio.emit()

    def empezar_juego(self):
        self.label_mensaje.setText("Mensaje: Empezó el juego")
        self.senal_comienza.emit()

    def mensaje_ganador(self, jugador, tipo):
        if tipo == 1:
            self.label_mensaje.setText(
                f"Mensaje: El ganador del juego es {jugador}")
        elif tipo == 2:
            self.label_mensaje.setText(
                f"Mensaje: {jugador} gana esta ronda")
        elif tipo == 3:
            self.label_mensaje.setText(
                f"Mensaje: {jugador} presiono cuando no debia")
    
    def actualizar_ventana(self, mensaje):
        if mensaje.carta_contada is None:
            self.label_carta.setText("-")
        else:
            self.label_carta.setText(f"Carta: {mensaje.carta_contada}")
        if mensaje.carta_tirada is None:
            self.imagen_carta.setPixmap(
                QPixmap(path.join("cartas", "red_joker.png")).scaled(150, 200))
        else:
            self.imagen_carta.setPixmap(
                QPixmap(path.join("cartas", 
                    mensaje.carta_tirada)).scaled(150, 200))
        self.label_jugador_1.setText(mensaje.nombre_1)
        self.label_jugador_2.setText(mensaje.nombre_2)
        self.contador_jugador_1.setText(str(mensaje.mazo_1))
        self.contador_jugador_2.setText(str(mensaje.mazo_2))
        if mensaje.juego_comenzo:
            self.boton_empezar.setEnabled(False)
            self.boton_reiniciar.setEnabled(True)
        else:
            self.boton_empezar.setEnabled(True)
            self.boton_reiniciar.setEnabled(False)