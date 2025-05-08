
# ELEMENTOS PRINCIPALS
# class = defina una clase
# __init__ = Metodo constructor
# self = referencia al objeto actual
# super() = llamar al constructor
# __atributo Atributo privado

# Creacion de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Creacion de metodo   
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años") 

# Crear objetos
p1 = Persona("Laura", 28)
p1.saludar()        

# Encapsulamiento: Oculatar los atributos para que no sean modificados directamente

class CuentaBancaria:
    def __init__ (self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def mostrarSaldo(self):
        print(f"Saldo de {self._titular}: ${self._saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad  

    #cuenta = CuentaBancaria("Wilson", 1000)
    # cuenta.depositar(500)
    # cuenta.mostrar_saldo()

# Herencia: Una clase hija hereda atributos y metodos de una clase padre

class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super(). __init__(nombre, edad)
        self.cargo = cargo
    def presentar(self):
        print(f"{self.nombre}, {self.edad} años, trabaja como {self.cargo}")    