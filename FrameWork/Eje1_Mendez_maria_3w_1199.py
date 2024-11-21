print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    #Setters
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("El nombre debe ser una cadena no vacía.")
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("La edad debe ser un número entero positivo.")
    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")
    #Getters
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    #Mostrar datos
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    #Verificar si es mayor de edad
    def es_mayor_de_edad(self):
        if self.edad is not None:
            return self.edad >= 18
        return False  # Si la edad no está definida, devolvemos Falso
#Ejemplo de uso
persona1 = Persona("Maria Mendez", 16, "12345678Z")
persona1.mostrar()
print(f"¿Es mayor de edad? {persona1.es_mayor_de_edad()}")
#Usando setters y getters
persona2 = Persona()
print(" ")
persona2.set_nombre("Valeria Ordoñez")
persona2.set_edad(16)
persona2.set_dni("98765432A")
persona2.mostrar()
print(f"¿Es mayor de edad? {persona2.es_mayor_de_edad()}")
