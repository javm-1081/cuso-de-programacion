# Listas para almacenar la informacion
productos = []
precios = []

print("\nBienvenido al Simulador de Cesta de Compra")

# Bucle principal del programa
continuar = True
while continuar:
    # Mostrar el menu
    print("\n" + "="*30)
    print("   MENÚ DE LA CESTA")
    print("="*30)
    print("1. AGREGAR un nuevo elemento")
    print("2. MOSTRAR la cesta")
    print("3. ELIMINAR un elemento")
    print("4. CALCULAR el total")
    print("5. RENUNCIAR / Salir")
    print("="*30)

    opcion = input("\nElige una opción (1-5): ").strip()

    if opcion == "1":
        print("\n--- Agregar Nuevo Artículo ---")
        nombre = input("\nIntroduce el nombre del artículo: ").strip()
        precio_input = input("\nIntroduce el precio de " + nombre + ": ").strip()
        
        # Conversion directa a decimal
        precio_num = float(precio_input)
        productos.append(nombre)
        precios.append(precio_num)
        print("\n" + nombre + " se ha añadido a la cesta.")

    elif opcion == "2":
        print("\n--- Contenido de tu Cesta ---")
        if len(productos) == 0:
            print("\nTu cesta está vacía.")
        else:
            # Recorrer las listas usando el indice para mantener la sincronizacion
            for i in range(len(productos)):
                print(str(i + 1) + ". " + productos[i] + " - $" + str(precios[i]))
        print("\n-----------------------------")

    elif opcion == "3":
        print("\n--- Eliminar Artículo ---")
        if len(productos) == 0:
            print("\nNo hay nada que eliminar.")
        else:
            # Mostrar la lista para que el usuario sepa que numero elegir
            for i in range(len(productos)):
                print(str(i + 1) + ". " + productos[i])
            
            indice_input = input("\nIntroduce el número del artículo que quieres eliminar: ").strip()
            
            # Convertir el texto a numero entero para el indice
            indice = int(indice_input) - 1
            
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                precios.pop(indice)
                print("\n" + eliminado + " ha sido eliminado de la cesta.")
            else:
                print("\nError: El número no está en la lista.")

    elif opcion == "4":
        print("\n--- Total de la Compra ---")
        if len(precios) == 0:
            print("\nEl total es $0.00")
        else:
            total = 0
            for p in precios:
                total = total + p
            print("\nEl total de tu compra es: $" + str(total))
        print("\n--------------------------")

    elif opcion == "5":
        print("\nGracias por usar el simulador. Hasta pronto.")
        continuar = False

    else:
        print("\nOpción no válida. Por favor elige un número del 1 al 5.")

    if continuar:
        input("\nPresiona Enter para continuar...")