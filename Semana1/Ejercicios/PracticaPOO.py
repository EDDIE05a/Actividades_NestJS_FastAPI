
# Creacion de clase

class Libro:
    # Se crea un constructor que crea e inicializa los atributos de la clase
    def __init__(self, titulo, autor, año):

        # Se referencia los atributos de clase con el objeto actual
        self.titulo = titulo
        self.autor = autor
        self.año = año

    # Se crea un metodo que obtiene los atributos de la clase
    def mostrarDatos(self):
        print(f"El libro {self.titulo} fue hecho por {self.autor} y se publicó en el {self.año}")

#Se instancia la clase y se crea un objeto
primerLibro = Libro("Don Quijote", "Danie Carvajal", 2005)

# El objeto que se creo hace uso de un metodo de la clase
primerLibro.mostrarDatos()            
        
# ----------------------------------------------------------------------------------------------------------------

# Creacion de clase
class Persona:
    # Se crea un constructor que crea e inicializa los atributos de la clase
    def __init__(self, identificacion, nombre, edad, genero):

        # Se referencia los atributos de clase con el objeto actual
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

# Se crea una clase hija herando atributos de la clase padre
class Estudiante(Persona):
    # Se  inicializan los atributos de la clase hija
    def __init__(self, identificacion, nombre, edad, genero, carrera):
        # Llama al constructor de la clase padre con los atributos de esta
        super().__init__(identificacion, nombre, edad, genero)
        # Se agrega atributo adicional para la clase hija
        self.carrera = carrera
        
# ----------------------------------------------------------------------------------------------------------------

# Creacion de clase
class Rectangulo: 
    # Se crea un constructor que crea e inicializa los atributos de la clase
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Se crean un metodos para crear objetos apartir de la clase
    def calcularArea(self):
        area = self.ancho * self.alto
        print(area)

    def calcularPerimetro(self):
        perimetro = (self.ancho * 2) + (self.alto * 2)
        print(perimetro)
