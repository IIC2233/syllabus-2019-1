__author__ = "chapito96 & fringlesinthestreet"

import threading
import socket
import json
from PyQt5.QtCore import pyqtSignal, QObject
from Ayudantia14_Eventos import ResultadosEvent


class Client(QObject):

    '''
    Esta es la clase encargada de conectarse con el servidor e intercambiar información
    Hereda de QObject con el único motivo de poder emitir y conectar señales.
    Se recomienda que exista un BackEnd aparte del cliente (y que se relacionen).
    '''

    # Señal para avisar cuando llegan resultados del servidor
    trigger_resultados = pyqtSignal(ResultadosEvent)

    def __init__(self, window = None):

        # Como heredamos de QObject hay que hacer el llamado a super()
        super().__init__()
        print("Inicializando cliente...")

        # Inicializamos el socket principal del cliente.
        # Este corresponde al de una conexión TCP
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Primero definimos la dirección a la cual nos conectaremos.
        # En este caso se trabaja de manera local
        self.host = "localhost"

        # Definimos un Puerto al cual será conectado el cliente
        self.port = 1238

        try:
            # Primero nos conectamos al servidor, pasándole como argumento la tupla
            # (HOST, PORT) al cual nos queremos conectar.
            # Esto tira error si la conexión es privada o si no hay un servidor "escuchando"
            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor...")

            # hacemos True un boolean para que escuche
            self.connected = True

            # Luego, creamos un thread para comenzar a escuchar lo que nos envía el servidor
            # Usamos un thread para permitir que el programa realice otras cosas
            # mientras escucha al servidor
            thread = threading.Thread(target=self.listen_thread, daemon=True)
            thread.start()
            print("Escuchando al servidor...")

            # Finalmente, conectamos la señal con un método de la ventana
            self.trigger_resultados.connect(window.desplegar_resultado)

        except ConnectionRefusedError:
            # Si la conexión es rechazada, entonces se 'cierra' el socket
            print("Conexión terminada")
            self.socket_cliente.close()
            exit()

    def listen_thread(self):
        '''
        Este método es el usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        :return:
        '''

        # Si desean que un usuario pueda desconectarse
        while self.connected:
            # Primero recibimos los 4 bytes del largo
            response_bytes_length = self.socket_cliente.recv(4)
            # Los decodificamos
            response_length = int.from_bytes(response_bytes_length,
                                             byteorder="big")

            # Luego, creamos un bytearray vacío para juntar el mensaje
            response = bytearray()

            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response) < response_length:
                response += self.socket_cliente.recv(256)

            # Una vez que tenemos todos los bytes, entonces ahí decodificamos
            response = response.decode()

            # Luego, debemos cargar lo anterior utilizando json
            decoded = json.loads(response)

            # Para evitar hacer muy largo este método, el manejo del mensaje se
            # realizará en otro método
            self.handlecommand(decoded)

    def handlecommand(self, decoded):
        '''
        Este método toma el mensaje decodificado de la forma:
        {"status": tipo del mensaje, "data": información}
        :param decoded: diccionario con la información
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(decoded))

        # Esto se parece a lo que hacíamos en simulación

        # Vemos si el tipo de mensaje es de resultado
        if decoded["status"] == "result":
            # Si lo es, entonces tomamos la información y emitimos una señal
            data = decoded["data"]
            event = ResultadosEvent(data["eleccion_1"], data["eleccion_2"],
                                    data["res"])
            self.trigger_resultados.emit(event)


        # Aquí irían otras opciones
        # elif decoded["status"] == "logout": # Ejemplo!
            # hacer algo


    def send(self, msg):
        '''
        Este método envía la información al servidor. Recibe un mensaje del tipo:
        {"status": tipo del mensaje, "data": información}
        :param msg: diccionario con la información
        :return:
        '''

        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(msg)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        self.socket_cliente.send(msg_length + msg_bytes)




    def enviar_jugada(self, event):
        '''
        Este método es el que se gatilla con la señal y manda la información al método send
        :param event: instancia de EleccionBotonEvent con la información
        :return:
        '''

        # Tomamos la información del evento y la pasamos al formato antes descrito
        data = {"status": event.status, "data": event.data}

        # Llamamos al método send para enviar la info al servidor
        self.send(data)



if __name__ == "__main__":

    client = Client()
