RUTA_TESERACTO = "teseracto.txt"

def cargar_teseracto(ruta):
    """
    Función que recibe la ruta del archivo teseracto.txt y retorna la
    matriz de adyacencia del teseracto
    """
    return []


def recorrer_teseracto(matriz):
    """
    Función que recibe una matriz de adyacencia de un grafo y retorna la 
    ruta optima entre el nodo 0 y el nodo n de la matriz

    Retorna una lista con el orden de los nodos a recorrer
    """
    return []

if __name__ == "__main__":
    print("Iniciando carga del teseracto")
    teseracto = cargar_teseracto(RUTA_TESERACTO)
    print("Teseracto Cargado")

    print("Iniciando proceso de descifrado")
    ruta_optima = recorrer_teseracto(teseracto)
    print("¡Ruta óptima encontrada!")

    pasos = [str(i+1) +'.- '+ "Nodo " + str(n+1) for i,n in enumerate(ruta_optima)]
    pasos_string = '\n'.join(pasos)
    print(pasos_string)

