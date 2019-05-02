import json
from alumnos import Alumno
from excepcion_propia import ErrorDatos
import csv

class DCCBanner:
    def __init__(self):
        self.cursos = dict()
        self.alumnos = list()

    def chequear_rut(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que su rut no siga
        el formato correcto.
        '''
        pass

    def chequear_numero_alumno(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que su nro. de
        alumno no siga el formato correcto.
        '''
        pass

    def chequear_curso(self, alumno):
        '''
        Recibe un alumno y levanta una excepción en caso de que el curso que
        haya pedido no siga el formato correcto.
        '''
        pass

    def inscribir_alumnos(self):
        '''
        Para cada uno de los alumnos en file_path chequea que su información
        esté correcta, si no lo está la corrige. Finalmente los inscribe al
        curso pedido.
        '''
        pass

    def cargar_cursos(self, archivo_cursos):
        '''
        Carga los cursos iniciales en el DCCBanner. No deben hacer nada
        con este método.
        '''
        with open(archivo_cursos, 'r') as file:
            cursos = json.load(file)
            for nombre_curso, secciones in cursos.items():
                self.cursos[nombre_curso] = secciones

    def cargar_alumnos(self, archivo_alumnos):
        '''
        Para cada uno de los alumnos en file_path los carga al atributo
        self.alumnos
        '''
        with open(archivo_alumnos, 'r') as file:
            alumnos = csv.reader(file, delimiter=';')
            for line in alumnos:
                line = [attr.strip() for attr in line]
                self.alumnos.append(Alumno(*line))

    def cargar_datos(self, archivo_cursos, archivo_alumnos):
    	'''
    	Carga los datos de alumnos y cursos, en caso de fallar, captura la
    	excepción y manda un mensaje explicando que falló.
    	'''
    	pass



if __name__ == '__main__':
    DCCBanner = DCCBanner()
    # Este try intenta cargar un archivo que no existe, por lo que el sistema
    # no se poblaría y debería entrar al except ErrorDatos. Lo que deben hacer
    # es buscar donde hacer raise de dicha excepción. Acá nada.
    try:
        DCCBanner.cargar_datos('cursos.json', 'hernan.jpg')
        DCCBanner.inscribir_alumnos()

    except ErrorDatos as ex:
    	print(ex.message)

    finally:
        # Después puedes cambiar este alumnos.csv por big_alumnos.csv
    	DCCBanner.cargar_datos('cursos.json', 'alumnos.csv')
    	DCCBanner.inscribir_alumnos()
    # Lo siguiente es para debuggear. Para el archivo de datos más grande de
    # alumnos les recomendamos cambiar el print(alumno) por print(alumno.nombre)
    for curso, secciones in DCCBanner.cursos.items():
        print(f'Curso: {curso}\n')
        for seccion in secciones:
            print(f'Seccion {seccion}\n')
            alumnos = secciones[seccion]
            for alumno in alumnos:
                print(alumno)
        print('*'*40)
