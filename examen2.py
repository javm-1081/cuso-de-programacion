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

#ejercicio 4

def es_palindromo(texto):
   
    palabra = texto.lower().replace(" ", "")
    
    return palabra == palabra[::-1]

palabrausuario = input("Introduce una palabra o frase: ")

if es_palindromo(palabrausuario):
    print("Es un palíndromo.")

else:
    print("No es un palíndromo.")

#ejercicio 5

def contarfrecuencia(frase):
    
    palabras = frase.split()
    contador = {}
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        
        else:
            contador[palabra] = 1
    
    return contador

fraseusuario = input("Introduce una frase: ")
resultado = contarfrecuencia(fraseusuario) 

print("\nFrecuencias:")
print(resultado)

#ejercicio6

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma = 0

for x in numeros:

 if x % 2 == 0:
     suma = suma + x


print(f"La suma de los números pares es {suma}")

#ejercicio7

agenda = {} 

def mostrarcontactos():
    print("\nNombre" + "Número de contacto")
    for nombre, numero in agenda.items():
        print("{nombre}{numero}")
    
while True:
     print("\nOpciones: ")
     print("1. Añadir contacto")
     print("2. Buscar contacto")
     print("3. Mostrar todos los contactos")
     print("4. Elimimnar contacto")
     print("5. Salir")
     opcion = input("Qué deseas hacer?: ")

     if opcion == 1:
         nombre = input("Nombre del contacto: ")
         numero = input("Número de contacto")
         agenda[nombre] = numero
         print("El contacto ha sido añadido")
    
     elif opcion == 2:
         nombrebuscar = input("Nombre del contacto a buscar")
         
         if nombrebuscar in agenda:
             print(f"Su numero es {agenda[nombrebuscar]}")

         else:
          print("No se encontró el contacto")

     elif opcion == 3: 
         if not agenda:
             print("La agenda está vacía")
         else:
             mostrarcontactos()
     
     elif opcion == 4:
         nombreeliminar = input("NOmbre del contacto a eliminar: ")
         if nombreeliminar in agenda:
             agenda.pop(nombreeliminar)
             print("El contacto ha sisdo eliminado")
         else:
             print("No se encontró el contacto")

     elif opcion == 5:
         print("Hasta pronto")
         break 
     
     else:
         print("Esa no es una respuesta válida")

