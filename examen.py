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
     