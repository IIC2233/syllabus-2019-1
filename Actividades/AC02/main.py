from people import Chef, Ayudante, Empatico, Exigente
from pykitchen import PyKitchen

if __name__ == '__main__':  # Aquí se instancian los distintos objetos
    cocineros = [Chef("Cristian Ruz"), Chef("Antonio Ossa"),
                 Chef("Fernando Florenzano"), Chef("Vicente Domínguez")]
    clientela = [Ayudante("Dr. H^4", Exigente()), Ayudante("Herny", Empatico()),
                 Ayudante("Tini Tamburini", Exigente()),
                 Ayudante("Ignacio", Empatico())]
    cocina = PyKitchen(cocineros, clientela)
    cocina.atender()
