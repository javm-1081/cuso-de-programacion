print("\nBienvenido al simulador de la cesta de compra")

cesta_productos = []
cesta_precios = []
opcion = ""

while opcion != "renunciar":
    print("\n--- MENU DE LA CESTA ---")
    print("1. AGREGAR un nuevo elemento")
    print("2. MOSTRAR el contenido de la cesta")
    print("3. ELIMINAR un elemento")
    print("4. CALCULAR el total de la compra")
    print("5. RENUNCIAR")
    
    opcion = input("\nQué eliges hacer? ").lower()

    if opcion == "agregar" or opcion == "1":
        nuevo_producto = input("\nQué producto quieres agregar? ").lower()
        precio_producto = float(input("\nCuál es el precio de " + nuevo_producto + "? "))
        
        cesta_productos.append(nuevo_producto)
        cesta_precios.append(precio_producto)
        print("\nHas agregado " + nuevo_producto + " a la cesta.")

    elif opcion == "mostrar" or opcion == "2":
        print("\nContenido de tu cesta:")
        if len(cesta_productos) == 0:
            print("\nLa cesta está vacía.")
        else:
            for i in range(len(cesta_productos)):
                print(str(i + 1) + ". " + cesta_productos[i] + " - $" + str(cesta_precios[i]))

    elif opcion == "eliminar" or opcion == "3":
        if len(cesta_productos) == 0:
            print("\nNo hay nada que eliminar.")
        else:
            print("\nLista actual:")
            for i in range(len(cesta_productos)):
                print(str(i + 1) + ". " + cesta_productos[i])
            
            indice_eliminar = int(input("\nQué número de elemento quieres eliminar? ")) - 1
            
            if indice_eliminar >= 0 and indice_eliminar < len(cesta_productos):
                eliminado = cesta_productos.pop(indice_eliminar)
                cesta_precios.pop(indice_eliminar)
                print("\nHas eliminado " + eliminado + " de la cesta.")
            else:
                print("\nEse número no es válido.")

    elif opcion == "calcular" or opcion == "4":
        total = 0
        for precio in cesta_precios:
            total = total + precio
        print("\nEl total de tu compra es: $" + str(total))

    elif opcion == "renunciar" or opcion == "5":
        print("\nGracias por usar el simulador. Hasta luego.")
        opcion = "renunciar"

    else:
        print("\nEsa no es una respuesta válida.")