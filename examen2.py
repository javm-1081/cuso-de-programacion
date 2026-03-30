#ejercicio1

frase = input("Ingresa una frase: ")

vocalesconteo = 0
consonantesconteo = 0

vocales = "aáeéiíoóuú"
consonantes = "bcdfghjklmnñpqrstvwxyz"

for caracter in frase.lower():
    
    if caracter in vocales:
        vocalesconteo += 1
    
    elif caracter in consonantes:
        consonantesconteo += 1
    
print(f"La frase {frase} tiene {vocalesconteo} vocales y {consonantesconteo} consonantes.")

#ejercicio2

import random

numeroaleatorio = random.randint(1, 100)
adivinado = False

print("Adivina el Número entre 1 y 100")

while not adivinado:
   
    intentos1 = int(input("Introduce tu número: "))
  
    if intentos1 < numeroaleatorio:
        print("Demasiado bajo.")

    elif intentos1 > numeroaleatorio:
        print("Demasiado alto.")
    
    else:
        adivinado = True
        print(f"El número era {numeroaleatorio}. Adivinaste.")

#ejercicio3

numeros = []

print("Ingresa los números que quieras.")

while True:
    respuesta = input("Introduce un número: ")
    
    if respuesta.lower() == "fin":
        break 

    numero = float(respuesta)
    numeros.append(numero)

if len(numeros) > 0:
    suma = sum(numeros)
    cantidad = len(numeros)
    promedio = suma / cantidad
    
    print(f"\nLista de números: {numeros}")
    print(f"El promedio es: {promedio}")
else:
    print("No ingresaste ningún número.")

