from leer_archivos import obtener_sistema


class Instalacion:
    def __init__(self, **kwargs):
        self.tipo = kwargs["tipo"]
        self.region = kwargs["region"]
        self.comuna = kwargs["comuna"]
        self.hijos = []
        self.consumo = float(kwargs["consumo"])
        self.energia = float(kwargs["energia"])

    def agregar_instalacion(self, instalacion):
        # Implementar
        pass

    def distribuir_energia(self, energia):
        # Implementar
        pass


def resumen_sistema(sistema):
    # Implementar
    pass


def comuna_mayor_gasto(sistema):
    # Implementar
    pass


def casas_insuficiencia(sistema):
    # Implementar
    pass


def instanciar_sistema(atributos_sistema):
    # No modificar.
    # Se crea la central generadora
    central_generadora = Instalacion(**atributos_sistema[0])

    # Se crean y agregan las demás instalaciones
    for atributos in atributos_sistema[1:]:
        nueva_instalacion = Instalacion(**atributos)
        central_generadora.agregar_instalacion(nueva_instalacion)
    
    # Se distribuye la energia a través del sistema
    central_generadora.distribuir_energia(central_generadora.energia)

    return central_generadora


if __name__ == '__main__':
    # No modificar
    # Se probará DCCableling para 4 sistemas electricos:
    for i in range(1, 5):
        print(f"CONSULTAS SISTEMA ELÉCTRICO N°{i}")
        print("---------------------" * 2)
        atributos_de_sistema = obtener_sistema()
        sistema_electrico = instanciar_sistema(atributos_de_sistema)
        resumen_sistema(sistema_electrico)
        comuna_mayor_gasto(sistema_electrico)
        casas_insuficiencia(sistema_electrico)
        print("---------------------" * 2)
