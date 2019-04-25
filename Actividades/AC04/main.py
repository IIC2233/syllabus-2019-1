import json


PATH_EXPORTACIONES = 'exportaciones.json'


class Pais:
    """
    Clase Pais que almacena su nombre y sus exportaciones.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.exportaciones = list()

    def agregar_exportacion(self, producto, destino):
        """
        Agrega una exportacion a lista de tuplas
        """
        pass

    def exporta_esto(self, producto):
        """
        Recibe un producto y retorna True si esta
        presente dentro de sus exportaciones, sino retorna False
        """
        pass


class RedComercio:
    """
    Clase RedComercio que almacena a los paises que la componen
    """
    def __init__(self, data_exportaciones):
        """
        Aquí se deberán crear los nodos pais y agregar sus exportaciones
        """
        pass

    def productos_importados(self, nombre_pais):
        """
        Retorna un set con todos los productos que son importados
        en un país determinado
        """
        pass

    
    def productos_producidos(self, nombre_pais):
        """
        Retorna un set de todos los productos que produce un país
        """
        pass

    def paises_clientes_finales(self, producto, nombre_pais):
        """
        Retorna un set con todos los países a los que llega finalmente
        un producto desde un país dado
        """
        pass
            


if __name__ == "__main__":
    # Esta sección carga el archivo en EXPORTACIONES, no la modifiques
    with open(PATH_EXPORTACIONES, "r", encoding = "utf8") as file:
        EXPORTACIONES = json.load(file)
    # La siguiente línea instancia a la clase RedComercio para crear el grafo
    COMERCIO = RedComercio(data_exportaciones = EXPORTACIONES)


    # Las siguientes líneas llaman a las consultas por implementar
    # para que compares tus resultados de consultas
    print(COMERCIO.productos_importados("Bélgica"))
    print(COMERCIO.productos_importados("Dinamarca"))
    print(COMERCIO.productos_importados("Estonia"))

    print(COMERCIO.productos_producidos("Estonia"))
    print(COMERCIO.productos_producidos("España"))
    print(COMERCIO.productos_producidos("Finlandia"))

    print(COMERCIO.paises_clientes_finales("Oro", "Albania"))
    print(COMERCIO.paises_clientes_finales("Oro", "Estonia"))
    print(COMERCIO.paises_clientes_finales("Carbón", "España"))
    print(COMERCIO.paises_clientes_finales("Trigo", "Finlandia"))
