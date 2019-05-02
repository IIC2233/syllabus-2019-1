class Alumno:
    def __init__(
        self,
        nombre,
        rut,
        num_alumno,
        ano_ingreso,
        carrera,
        curso,
        seccion,
        comentario,
    ):
        self.nombre = nombre
        self.rut = rut
        self.num_alumno = num_alumno
        self.ano_ingreso = ano_ingreso
        self.carrera = carrera
        self.curso = curso
        self.seccion = seccion
        self.comentario = comentario

    def __str__(self):
        nombre = f'Nombre alumno: {self.nombre}\n'
        rut = f'Rut: {self.rut}\n'
        num = f'Numero alumno: {self.num_alumno}\n'
        año = f'Año de ingreso: {self.ano_ingreso}\n'
        carrera = f'Carrera: {self.carrera}\n'
        comentario = f'Comentario: {self.comentario}\n'

        return nombre + rut + num + año + carrera + comentario + '\n'
