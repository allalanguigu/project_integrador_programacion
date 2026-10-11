# Proyecto integrador - Logica de Programacion
# Registro de calificaciones de un curso
# Etapa 3: se agrega la busqueda de un estudiante y el resumen del curso
#          (promedio general, mejor y menor promedio, aprobados y reprobados)

# Tupla con los nombres de las evaluaciones (no cambia durante el programa)
EVALUACIONES = ("Parcial 1", "Parcial 2", "Examen")

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_PARA_APROBAR = 7

# Cada estudiante se guarda como un diccionario dentro de esta lista
estudiantes = []


def es_numero(texto):
    """Devuelve True si el texto es un numero como 8 o 7.5"""
    texto = texto.replace(".", "", 1)
    return texto.isdigit()


def pedir_nota(nombre_evaluacion):
    """Pide una nota y la repite hasta que este entre 0 y 10"""
    while True:
        texto = input("Nota de " + nombre_evaluacion + " (0 a 10): ")

        if not es_numero(texto):
            print("Escribe solo numeros, por ejemplo 8 o 7.5")
            continue

        nota = float(texto)

        if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
            print("La nota debe estar entre 0 y 10.")
        else:
            return nota


def calcular_promedio(notas):
    """Recibe una lista de notas y devuelve el promedio"""
    suma = 0
    for nota in notas:
        suma = suma + nota
    return suma / len(notas)


def obtener_estado(promedio):
    """Devuelve Aprobado o Reprobado segun el promedio"""
    if promedio >= NOTA_PARA_APROBAR:
        return "Aprobado"
    else:
        return "Reprobado"


def registrar_estudiante(lista):
    """Pide los datos de un estudiante y lo agrega a la lista"""
    nombre = input("Nombre del estudiante: ")

    if nombre == "":
        print("El nombre no puede estar vacio.")
        return

    if buscar_estudiante(lista, nombre) != None:
        print("Ese estudiante ya esta registrado.")
        return

    notas = []
    for evaluacion in EVALUACIONES:
        nota = pedir_nota(evaluacion)
        notas.append(nota)

    promedio = calcular_promedio(notas)

    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio,
        "estado": obtener_estado(promedio)
    }
    lista.append(estudiante)
    print("Estudiante registrado. Promedio:", round(promedio, 2), "-", estudiante["estado"])


def mostrar_estudiantes(lista):
    """Muestra todos los estudiantes registrados"""
    if len(lista) == 0:
        print("Todavia no hay estudiantes registrados.")
        return

    print("")
    print("--- Lista de estudiantes ---")
    numero = 1
    for estudiante in lista:
        print(str(numero) + ".", estudiante["nombre"], "-", estudiante["notas"],
              "- Promedio:", round(estudiante["promedio"], 2), "-", estudiante["estado"])
        numero = numero + 1


def buscar_estudiante(lista, nombre_buscado):
    """Busca un estudiante por su nombre y lo devuelve. Si no existe devuelve None"""
    for estudiante in lista:
        if estudiante["nombre"].lower() == nombre_buscado.lower():
            return estudiante
    return None


def consultar_estudiante(lista):
    """Pide un nombre y muestra las notas de ese estudiante"""
    nombre = input("Nombre a buscar: ")
    estudiante = buscar_estudiante(lista, nombre)

    if estudiante == None:
        print("No se encontro a", nombre)
    else:
        print("")
        print("Estudiante:", estudiante["nombre"])
        posicion = 0
        for evaluacion in EVALUACIONES:
            print(" ", evaluacion + ":", estudiante["notas"][posicion])
            posicion = posicion + 1
        print("  Promedio:", round(estudiante["promedio"], 2))
        print("  Estado:", estudiante["estado"])


def calcular_resumen(lista):
    """Recorre la lista y devuelve un diccionario con los datos del curso"""
    suma = 0
    aprobados = 0
    reprobados = 0
    mejor = lista[0]
    menor = lista[0]

    for estudiante in lista:
        suma = suma + estudiante["promedio"]

        if estudiante["estado"] == "Aprobado":
            aprobados = aprobados + 1
        else:
            reprobados = reprobados + 1

        if estudiante["promedio"] > mejor["promedio"]:
            mejor = estudiante
        if estudiante["promedio"] < menor["promedio"]:
            menor = estudiante

    resumen = {
        "total": len(lista),
        "promedio_curso": suma / len(lista),
        "aprobados": aprobados,
        "reprobados": reprobados,
        "mejor": mejor,
        "menor": menor
    }
    return resumen


def mostrar_resumen(lista):
    """Muestra el resumen del curso"""
    if len(lista) == 0:
        print("Todavia no hay estudiantes registrados.")
        return

    resumen = calcular_resumen(lista)
    print("")
    print("--- Resumen del curso ---")
    print("Estudiantes registrados:", resumen["total"])
    print("Promedio del curso:", round(resumen["promedio_curso"], 2))
    print("Aprobados:", resumen["aprobados"])
    print("Reprobados:", resumen["reprobados"])
    print("Mejor promedio:", resumen["mejor"]["nombre"], "con", round(resumen["mejor"]["promedio"], 2))
    print("Menor promedio:", resumen["menor"]["nombre"], "con", round(resumen["menor"]["promedio"], 2))


def mostrar_menu():
    """Muestra las opciones y devuelve la que elige el usuario"""
    print("")
    print("=== REGISTRO DE CALIFICACIONES ===")
    print("1. Registrar estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Buscar estudiante")
    print("4. Ver resumen del curso")
    print("5. Salir")
    return input("Elige una opcion: ")


def main():
    opcion = ""
    while opcion != "5":
        opcion = mostrar_menu()

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            consultar_estudiante(estudiantes)
        elif opcion == "4":
            mostrar_resumen(estudiantes)
        elif opcion == "5":
            print("Hasta luego.")
        else:
            print("Opcion no valida. Intenta de nuevo.")


main()
