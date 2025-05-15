listaFrutas = ["apple", "banana", "strawberry", "cherry"]

opcion = 0

while opcion != 3:
    
    print("---------- PANEL FRUTAL ---------")
    print("1. AÑADIR FRUTA")
    print("2. BUSCAR FRUTA")
    print("3. SALIR")
    opcion = int(input("Ingrese el numero de la opcion: "))

    if opcion == 1:
        nombreFruta = input("Ingrese el nombre de la fruta que desea añadir \n")
        frutaAdd = nombreFruta.lower()
        if frutaAdd in listaFrutas:
            print("La fruta ya esta en la lista")
        else:
            listaFrutas.append(frutaAdd)
            print("Fruta añadida correctamente")

    elif opcion == 2:
        nombreFruta = input("¿Que fruta desea buscar? \n" )
        frutaBuscar = nombreFruta.lower()
        if frutaBuscar in listaFrutas:
            print(f"La fruta {frutaBuscar} SI aparece en la lista")
        else:
            print(f"La fruta {frutaBuscar} NO aparece en la lista")

    else:
        print("Elija una opcion valida")

print("Gracias por usar el algoritmo xd")