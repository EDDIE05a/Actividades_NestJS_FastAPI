from datetime import date, datetime, timedelta

# -------------------- MANEJO DE FECHAS --------------------

fecha_hoy = date.today()
fecha_hora_actual = datetime.now()
cumpleaños = date(1990, 4, 15)
mañana = date.today() + timedelta(days = 1)
dias_transcurridos = (fecha_hoy - date(2025, 1, 1)).days



# -------------------- VARIABLES EN PYTHON -------------------

cadena = "String"
entero = 0
decimal = 1.75

# -------------------- CONCATENACION DE VARIABLES --------------------

print(f"En Java, los datos {cadena} no aceptan valores como {entero} o {decimal} si no tienen comillas")

# -------------------- CONVERSION DE TIPO DE DATOS --------------------

# Cadena a entero
edad_str = "30"
edad_int = int(edad_str)

# Entero a cadena
a = 10
s = str(a) 

# Flotante a entero
y = 3.14
z = int(y)  

# Cadena a flotante
b = "3.5"
f = float(b)

# -------------------- MANEJO DE BOOLEANS --------------------

es_Mayor = True
tiene_licencia = False

if es_Mayor and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

nota = 85

if nota >= 90:
    print("Eselente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Desaprobó")


# -------------------- SIMULACIÓN DE CASOS CON DICCIONARIO --------------------

def opcion_1():
    return "Opcion Uno"
def opcion_2():
    return "Opcion Dos"
switch = {1: opcion_1, 2: opcion_2}
resultado = switch.get(2, lambda: "Opción no valida")()
print(resultado)

# -------------------- CICLOS --------------------

# For

for i in range(1,6):
    print(i)

# While

cont = 3
while cont > 0:
    print(cont)
    cont -= 1    

# Bucle tipo foreach con lista y diccionario

animales = ["gato", "perro", "vaca"]
for animal in animales:
    print(animal)

persona = {"nombre": "Wilson", "edad": 30}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")


