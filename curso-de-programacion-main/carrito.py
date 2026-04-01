productos = []
precios = []

print("\n Cesta de Compra")

continuar = True
while continuar:
  
    print("\n   MENÚ DE LA CESTA")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar la cesta")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Salir")
   

    opcion = input("\nElige una opción (1-5): ").strip()

    if opcion == "1" or opcion == "Agregar":
        print("\nAgregar Nuevo Artículo")
        nombre = input("\nIntroduce el nombre del artículo: ").strip()
        precio_input = input(f"\nIntroduce el precio de {nombre}: ").strip()
        
        precio_num = float(precio_input)
        productos.append(nombre)
        precios.append(precio_num)
        print(f"\n {nombre} se ha añadido a la cesta.")

    elif opcion == "2" or opcion == "Mostrar":
        print("\nContenido de tu Cesta")
        
        if len(productos) == 0:
            print("\nTu cesta está vacía.")
        
        else:
           
            for i in range(len(productos)):
                print(str(i + 1) + ". " + productos[i] + " - $" + str(precios[i]))

    elif opcion == "Eliminar" or opcion == "3":
        print("\nEliminar Artículo")
        if len(productos) == 0:
            print("\nNo hay nada que eliminar.")
       
        else:
            for i in range(len(productos)):
                print(str(i + 1) + ". " + productos[i])
            
            indice_input = input("\nIntroduce el número del artículo que quieres eliminar: ").strip()
            
            indice = int(indice_input) - 1
            
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                precios.pop(indice)
                print(f"\n {eliminado} ha sido eliminado de la cesta.")
            
            else:
                print("\nError: El número no está en la lista.")

    elif opcion == "4" or opcion == "Calcular":
        print("\nTotal de la Compra")

        if len(precios) == 0:
            print("\nEl total es $0.00")
        
        else:
            total = 0
            for p in precios:
                total = total + p
            print("\nEl total de tu compra es: $" + str(total))

    elif opcion == "5" or opcion == "Salir":
        print("\nGracias por usar la cesta.")
        continuar = False

    else:
        print("\nOpción no válida. Elige un número del 1 al 5.")

    if continuar:
        input("\nPresiona Enter para continuar.")