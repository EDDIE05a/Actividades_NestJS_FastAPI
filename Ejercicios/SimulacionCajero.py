creditoAprobado = 5000
sumaRetiros = 0
restanteCredito = 0

print(f"Tiene un credito aprobado de {creditoAprobado}.")

while restanteCredito <= creditoAprobado :

    print("1. RETIRAR SALDO")
    print("2. SALDO DISPONIBLE")
    print("3. SALIR")
    opcion = int(input("Ingrese el numero de la opcion: "))

    if opcion == 1:
        cantidadRetirar = float(input("¿Cuanto desea retirar? \n"))

        if cantidadRetirar <= creditoAprobado and cantidadRetirar > 0:
            sumaRetiros += cantidadRetirar
            restanteCredito = creditoAprobado - sumaRetiros
            print(f"Retiro Exitoso, su retiro fue de {cantidadRetirar}")
            print("Saldo disponible:", restanteCredito)

        else:
            print("Error, no puede retirar esa cantidad")    

    elif opcion == 2:
        print(f"Su saldo es de {restanteCredito}")

    elif opcion == 3:
        break

print("Gracias por usar el cajero")        