print(" ")
print("Mendez_Sanchez_Maria_Guadalupe_Yazmin_3w_1199")
print(" ")
class Cuenta:
    #Definir la cuneta con self, titular y la cantidad con el resultado
    def __init__(self, titular, cantidad=0.0):
        if titular is None:
            raise ValueError("El titular de la cuenta es obligatorio.")
        self.titular = titular
        self.set_cantidad(cantidad) 
        #Defirnir self y titular 
    def set_titular(self, titular):
        if titular is None:
            raise ValueError("El titular no puede ser None.")
        self.titular = titular
        #Definir self
    def get_titular(self):
        return self.titular
    #Definir sel y titular con if y else
    def set_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número mayor o igual a cero.")
        self.cantidad = cantidad
        #Definir self con return
    def get_cantidad(self):
        return self.cantidad
    #Imprimir tirular y la cantidad de la cuneta
    def mostrar(self):
        print(f"Titular: {self.get_titular().get_nombre()}")
        print(f"Cantidad en la cuenta: {self.get_cantidad()}")
        #Ingresar la cantidad con if y else e imprimir la cantidad
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva.")
class Persona:
    #Definir self, nombre, edad y dni
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    def es_mayor_de_edad(self):
        return self.edad >= 18
    #Llamar a las variables para que pueda hacer el codigo
persona = Persona("Maria", 18, "12345678A")
cuenta = Cuenta(titular=persona, cantidad=1000)
cuenta.mostrar()
cuenta.ingresar(500)
cuenta.mostrar()
cuenta.retirar(200)
cuenta.mostrar()
cuenta.retirar(-50)