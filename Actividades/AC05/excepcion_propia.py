class ErrorDatos(Exception):
	def __init__(self, cursos, alumnos):
		if not cursos and not alumnos:
			self.message = 'No existen los cursos ni los alumnos.'
		elif not cursos:
			self.message = 'No existen los cursos.'
		else:
			self.message = 'No existen los alumnos.'
