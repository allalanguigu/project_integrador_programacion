# Proyecto integrador - Logica de Programacion
# Registro de calificaciones de un curso
# Etapa 1: menu por consola, registrar estudiantes y ver la lista

# Cada estudiante se guarda como un diccionario dentro de una lista
estudiantes = []

opcion = ""

while opcion != "3":
    print("")
    print("=== REGISTRO DE CALIFICACIONES ===")
    print("1. Registrar estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Salir")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        nota1 = float(input("Nota del parcial 1 (0 a 10): "))
        nota2 = float(input("Nota del parcial 2 (0 a 10): "))
        nota3 = float(input("Nota del examen (0 a 10): "))

        promedio = (nota1 + nota2 + nota3) / 3

        estudiante = {
            "nombre": nombre,
            "notas": [nota1, nota2, nota3],
            "promedio": promedio
        }
        estudiantes.append(estudiante)
        print("Estudiante registrado. Promedio:", round(promedio, 2))

    elif opcion == "2":
        if len(estudiantes) == 0:
            print("Todavia no hay estudiantes registrados.")
        else:
            print("")
            print("--- Lista de estudiantes ---")
            for estudiante in estudiantes:
                print(estudiante["nombre"], "-", estudiante["notas"], "- Promedio:", round(estudiante["promedio"], 2))

    elif opcion == "3":
        print("Hasta luego.")

    else:
        print("Opcion no valida. Intenta de nuevo.")
