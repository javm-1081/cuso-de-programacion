print ("Es la novena entrada, dos outs, hombres en las esquinas y tu equipo pierde por una carrera.")

#nivel 1
decision1 = input("Qué eliges hacer? Batear, Tocar la bola o Esperar? ").lower()

if decision1 == "batear":
    #nivel 2 Ruta de batear
    print("El lanzador tira una recta adentro a 100 mph.")
    decision2 = input("Qué haces? batear o esperar? " ).lower()

    if decision2 == "batear" or decision2 == "bateo":
      print("Das un batazo al jardín derecho, llegas a la primera base pero ves que el jardinero todavía está lejos de la pelota.")
      decision3 = (input)("Qué haces? correr o quedarte? ").strip().lower()
   
      if decision3 == "correr" or decision3 == "corro":
        decision4 = input("Llegas a segunda base. Intentas Robar la tercera o prefieres Esperar? ")

        if decision4 == "robar":
            print("Llegas a 3ra pero el bateador da un batazo de línea por donde estas tú.")
            decision5 = input("Qué haces? Seguir o Regresar a 2da base? ")

            if decision5 == "seguir":
                print("El 3ra base no atrapó la bola y seguiste hacia home plate, pero el jardinero lanza la bola a home y llega al mismo tiempo que tú.")
                decision6 = input("Qué haces? Saltar, Deslizarte o Chocar? ")
            
                if decision6 == "deslizarte" or decision6 == "deslizarme":
                    print("Safe, anotaste y tu equipo ganó.")
                
                elif decision6 == "chocar":
                        print("El receptor aguantó el choque, estás fuera.")
            
            elif decision5 == "regresar":
                print("Te hicieron out en segunda, tu equipo perdió.")

        elif decision4 == "esperar" or decision4 == "espero":
          print("Te quedaste esperando y el siguiente bateador se ponchó. Se acabó el juego.")

      elif decision3 ==  "quedarte" or decision3 == "quedarme":
        print("Te aseguraste en primera, pero el siguiente bateador falló. Tu equipo perdió.")

    elif decision2 == "aguantar":
        print("Strike, estás fuera, tu equipo perdió.")
        
elif decision1 == "esperar" or decision1 == "espero":
    print("Strike, estás fuera, tu equipo perdió.")
    
elif decision1 == "tocar":
    print("\n Pones el bate y la bola sale rodando hacia el 3era base ")
    decision22 = input("Qué haces? Correr o Mirar a ver si es foul? ").strip().lower()

    if decision22 == "correr":
            print("\n El 3era base tira mal a primera.")
            decision33 = input("Qué haces? Avanzar a segunda o Asegurar primera? ").strip().lower()

            if decision33 == "avanzar":
                 decision44 = input("Llegas a segunda base. Intentas Robar la tercera o prefieres Esperar? ")
                 
                 if decision44 == "robar":
                     print("Llegas a 3ra pero el bateador da un batazo de línea por donde estas tú.")
                     decision55 = input("Qué haces? Seguir o Regresar a 2da base?")
                     
                     if decision55 == "seguir":
                         print("El 3ra base no atrapó la bola y seguiste hacia home plate, pero el jardinero lanza la bola a home y llega al mismo tiempo que tú.")
                         decision66 = input("Qué haces? Saltar, Deslizarte o Chocar ")
                         
                         if decision66 == "Deslizarte" or decision6 == "Deslizarme":
                            print("Safe, anotaste y tu equipo ganó")
                
                         elif decision6 == "Chocar":
                             print("El receptor aguantó el choque, estás fuera")
            
                     elif decision5 == "Regresar":
                         print("Te hicieron out en segunda, tu equipo perdió")
else:
    print("\n Esa no es una respuesta válida.")
        

      


