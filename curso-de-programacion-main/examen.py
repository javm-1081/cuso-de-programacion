#ejercicio 1
aprobado1 = (6.0)
aprobado2 = (10.0)

notas = []

for i in range(4):
    nota = float(input(f"Ingresa la calificación {i+1}: "))
    notas.append(nota)

print("Resultados")
for nota in notas:
    if nota >= aprobado1 and nota <= aprobado2:
        print("Aprobado")

    else:
        print("Desaprobado")

#ejercicio 2

saldo = 1000
opcioneselegidas = []
opcionesvalidas = ("1", "2", "3", "4")

while True:
    print("1. Consultar, 2. Depositar, 3. Retirar, 4. Salir")
    opcion = input("Elije una opción: ")

    if opcion == "1":
        print(f"Su saldo es: {saldo}")
        opcioneselegidas.append("Consulta realizada con éxito")
        
    elif opcion == "2":
        cantidad = float(input(f"Introduzca la cantidad que desea depositar: "))

    elif opcion == "3":
        cantidadretirada = float(input("Introduzca la cantidad que desea retirar"))
        
        if cantidadretirada <= cantidad:
            cantidad -= cantidadretirada
            opcioneselegidas.append(f"Retiro: -${cantidadretirada}")
            print("Retiro exitoso.")
        
        else:
            print("No tienes esa cantidad de dinero")

    elif opcion == "4":
        print("Resumen de movimientos")
        for movimiento in opcioneselegidas:
            print(f"- {movimiento}")
        print("Gracias por usar el cajero.")
        break

    else:
        print("Opción inválida.")

#ejercicio3 

hp = [100, 100]
danos = (10, 25) 

print("Peleen")

while hp[0] > 0 and hp[1] > 0:
    print(f"\n Estado: jugador {hp[0]} HP vs Máquina {hp[1]} HP ---")
    
    accion = input("Qué ataque usarás? (1 Ligero, 2 Crítico): ")
    
    if accion == "1":
        print(f"Diste un golpe ligero -{danos[0]} HP")
        hp[1] -= danos[0] 
    
    elif accion == "2":
        print(f"Diste un golpe crítico! -{danos[1]} HP")
        hp[1] -= danos[1]
    else:
        print("Fallaste")

    if hp[1] <= 0:
        break

    print(f"Turno de la máquina -{danos[0]} HP")
    hp[0] -= danos[0]

if hp[0] <= 0:
    print("\n La máquina te ganó.")
else:
    print("\nGanaste.")


