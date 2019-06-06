"""
server.py -- un simple servidor
"""

import pickle
from socket import socket

HOST = '127.0.0.1'


class Servidor:
    """
    Una clase que representa un servidor.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.cliente = None
        self.socket = socket()

        self.comandos = {
            "ls": self.lista_directorio,
            "descargar": self.enviar_archivo,
            "echo": self.crear_archivo,
            "cerrar_sesion": self.desconectar,
        }

    def run(self):
        """
        Enciende el servidor que puede conectarse
        y recibir comandos desde un único cliente.
        """

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Escuchando en {self.host}:{self.port}.")

        while self.cliente is None:
            self.cliente, _ = self.socket.accept()
            print("¡Un cliente se ha conectado!")

            while self.cliente:
                comando, args = pickle.loads(self.receive())
                self.comandos[comando](*args)

        print("Arrivederci.")

    def send(self, mensaje):
        """
        [COMPLETAR]
        Envía datos binarios al cliente conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        pass

    def receive(self):
        """
        [MODIFICAR]
        Recibe datos binarios del cliente, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        return self.cliente.recv(128)  # maldición, esto es demasiado poco.

    def lista_directorio(self):
        """
        [COMPLETAR]
        Envía al cliente una lista que contiene los nombres de
        todos los archivos existentes en la carpeta del servidor.
        """

        pass

    def enviar_archivo(self, ruta_archivo):
        """
        [COMPLETAR]
        Envía al cliente un archivo ubicado en el directorio del servidor.
        """

        pass

    def crear_archivo(self, ruta_archivo):
        """
        [COMPLETAR]
        Escribe un archivo con los datos recibidos desde el cliente.
        """

        pass

    def desconectar(self):
        self.cliente = None
        print("El cliente se ha desconectado.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    servidor = Servidor(int(port_))
    servidor.run()
