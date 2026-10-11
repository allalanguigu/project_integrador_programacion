# Proyecto integrador - Logica de Programacion
# Registro de calificaciones de un curso
# Etapa 2: el programa se organiza en funciones, se validan las notas
#          y se indica si el estudiante aprueba o reprueba

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


def mostrar_menu():
    """Muestra las opciones y devuelve la que elige el usuario"""
    print("")
    print("=== REGISTRO DE CALIFICACIONES ===")
    print("1. Registrar estudiante")
    print("2. Ver lista de estudiantes")
    print("3. Salir")
    return input("Elige una opcion: ")


def main():
    opcion = ""
    while opcion != "3":
        opcion = mostrar_menu()

        if opcion == "1":
            registrar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            print("Hasta luego.")
        else:
            print("Opcion no valida. Intenta de nuevo.")


main()
