class Persona(object):
    def __init__(self,nombre,edad,lugarResidencia):

        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugarResidencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado,edadEmpleado,residenciaEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()

        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)

lazaro = Persona("Lázaro", 52, "Valencia")
lazaro.descripcion()

print(isinstance(lazaro, Empleado))