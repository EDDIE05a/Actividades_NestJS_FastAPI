from temas import condicionales, ciclos, funciones

def menu():
    print("\n=== Plataforma de Programación ===")
    print("1. Condicionales")
    print("2. Ciclos")
    print("3. Funciones")
    print("0. Salir")
    return input("Selecciona un tema: ")

def ejecutar_tema(opcion):
    if opcion == "1":
        respuesta = input("Con SI o no, responsda si en Pyhthon se pueden hacer condicionales anidados\n")
        print("✅ Correcto" if condicionales.ejercicio_1(respuesta) else "❌ Incorrecto")
    elif opcion == "2":
        respuesta = input("¿Cuántas veces se imprime 'Hola' si for i in range(3)? \n")
        print("✅ Correcto" if ciclos.ejercicio_1(respuesta) else "❌ Incorrecto")
    elif opcion == "3":
        respuesta = input("¿Qué palabra clave se usa para definir una función en Python? \n")
        print("✅ Correcto" if funciones.ejercicio_1(respuesta) else "❌ Incorrecto")

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "0":
            print("¡Hasta luego!")
            break
        ejecutar_tema(opcion)
