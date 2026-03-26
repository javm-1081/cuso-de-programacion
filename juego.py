print ("Es la novena entrada, dos outs, hombres en las esquinas y tu equipo pierde por una carrera.")

#nivel 1
decision1 = input("Qué eliges decides hacer? Batear, Tocar la bola o Esperar? > ").lower()

if decision1 == "batear":
    #nivel 2 Ruta de batear
    print("El lanzador tira una recta adentro a 100 mph.")
    decision2 = input("Qué haces? batear o esperar ?" ).lower()

    if decision2 == "batear":
        print(input)("Das un batazo al jardín derecho, llegas a la primera base pero ves que el jardinero todavía está lejos de la pelota. Qué haces? correr o quedarte").lower()
        decision3 = input("¿Qué haces? QUEDARTE en primera, CORRER a segunda o ESPERAR fuera de la base").strip().lower()
        
        if decision3 == "correr":
         decision4 = print("Llegas a segunda base.Intentas ROBAR la tercera o prefieres ESPERAR? ")
         
         if decision4 = "robar":
             decision 5 = input("Llegas a 3ra pero el bateador da un batazo de línea por donde estas tú")
              

    if decision2 == ("aguantar"):
        print("Strike, estás fuera, tu equipo perdió")
       


