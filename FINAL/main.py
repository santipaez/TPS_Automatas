import option1, option2, option3, option4, option5, option6

while True:
    print("Menú:")
    print("1. Listar las 5 canciones con más likes, vistas y comentarios")
    print("2. Listar las 5 canciones con mejor ratio (likes/view) y mostrar el porcentaje")
    print("3. Buscar una canción")
    print("4. Agregar nueva fila")
    print("5. Listar las 10 canciones más largas en formato legible")
    print("6. Listar los 10 artistas con más reproducciones en total")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        option1.listar_top_canciones()
    elif opcion == "2":
        # Implementa la lógica para listar las 5 canciones con mejor ratio y mostrar el porcentaje
        pass
    elif opcion == "3":
        # Implementa la lógica para buscar una canción por una parte del nombre
        pass
    elif opcion == "4":
        # Implementa la lógica para agregar una nueva fila al archivo
        pass
    elif opcion == "5":
        # Implementa la lógica para listar las 10 canciones más largas en formato legible
        pass
    elif opcion == "6":
        # Implementa la lógica para listar los 10 artistas con más reproducciones en total
        pass
    elif opcion == "0":
        # Salir del programa
        break
    else:
        print("Opción no válida. Intente de nuevo.")
