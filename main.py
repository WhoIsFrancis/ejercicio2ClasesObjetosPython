class Alumno:
    nombre = None
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def calcularNota(self, nota):
        if self.nota >= 6:
            print("El alumno esta aprobado con la nota: ", self.nota)
        else:
            print("El alumno no aprobo ya que su nota es menor que 6")

    def imprimir(self):
        print("Nombre: ", self.nombre, "\nNota: ", self.nota)


alumno = Alumno("Francisco", 5)
alumno.imprimir()
alumno.calcularNota(alumno.nota)