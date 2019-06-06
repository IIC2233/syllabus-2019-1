"""
client.py -- un simple cliente
"""

import pickle
from socket import socket, SHUT_RDWR

HOST = '127.0.0.1'


class Cliente:
    """
    Una clase que representa un cliente.
    """

    def __init__(self, port):
        self.host = HOST
        self.port = port
        self.socket = socket()
        self.connected = False

        self.comandos = {
            "help": self.help,
            "ls": self.ls,
            "echo": self.echo,
            "descargar": self.descargar,
            "cerrar_sesion": self.cerrar_sesion,
        }
        self.args_por_comando = {
            "help": 0,
            "ls": 0,
            "echo": 1,
            "descargar": 1,
            "cerrar_sesion": 0
        }

    def validar(self, comando, args):
        """
        [MOFIFICAR]
        Valida el comando y los argumentos ingresados por el usuario.
        """

        return True

    def run(self):
        """
        [MODIFICAR]
        Enciende el cliente que puede conectarse
        para enviar algunos comandos al servidor.
        """

        self.socket.connect((self.host, self.port))
        self.connected = True

        while self.connected:

            comando, *args = input('$ ').split()
            funcion = self.comandos.get(comando)

            if self.validar(comando, args):
                if comando == 'help':
                    self.help()
                else:
                    self.send(pickle.dumps((comando, args)))
                    funcion(*args)
            else:
                print("Escribe 'help' para obtener ayuda.")

    def send(self, mensaje):
        """
        [MODIFICAR]
        Envía datos binarios al servidor conectado por el socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        self.socket.sendall(mensaje)

    def receive(self):
        """
        [COMPLETAR]
        Recibe datos binarios del servidor, a través del socket,
        cumpliendo con el protocolo establecido en el enunciado.
        """

        pass

    def help(self):
        print("Esta es la lista de todos los comandos disponibles.")
        print('\n'.join(f"- {comando}" for comando in self.comandos))

    def ls(self):
        """
        [COMPLETAR]
        Este comando recibe una lista con los archivos del servidor.

        Ejemplo:
        $ ls
        - doggo.jpg
        - server.py
        """

        pass

    def echo(self, ruta_archivo):
        """
        [COMPLETAR]
        Este comando envía un input hacia el servidor
        con el contenido que deseas escribir.
        """

        pass

    def descargar(self, ruta_archivo):
        """
        [COMPLETAR]
        Este comando recibe un archivo ubicado en el servidor.
        """

        pass

    def cerrar_sesion(self):
        self.connected = False
        self.socket.shutdown(SHUT_RDWR)
        self.socket.close()
        print("Arrivederci.")


if __name__ == '__main__':
    port_ = input("Escriba el puerto: ")
    cliente = Cliente(int(port_))
    cliente.run()
