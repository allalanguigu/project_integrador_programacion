# Proyecto integrador - Logica de Programacion
# Registro de calificaciones de un curso
# Etapa 4: se reemplaza el menu de consola por una ventana hecha con tkinter

import tkinter as tk
from tkinter import messagebox

# Tupla con los nombres de las evaluaciones (no cambia durante el programa)
EVALUACIONES = ("Parcial 1", "Parcial 2", "Examen")

NOTA_MINIMA = 0
NOTA_MAXIMA = 10
NOTA_PARA_APROBAR = 7

# Cada estudiante se guarda como un diccionario dentro de esta lista
estudiantes = []


# ---------- Funciones de logica (no dependen de la ventana) ----------

def es_numero(texto):
    """Devuelve True si el texto es un numero como 8 o 7.5"""
    texto = texto.replace(".", "", 1)
    return texto.isdigit()


def nota_valida(texto):
    """Devuelve True si el texto es un numero entre 0 y 10"""
    if not es_numero(texto):
        return False
    nota = float(texto)
    return nota >= NOTA_MINIMA and nota <= NOTA_MAXIMA


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


def buscar_estudiante(lista, nombre_buscado):
    """Busca un estudiante por su nombre y lo devuelve. Si no existe devuelve None"""
    for estudiante in lista:
        if estudiante["nombre"].lower() == nombre_buscado.lower():
            return estudiante
    return None


def agregar_estudiante(lista, nombre, notas):
    """Crea el diccionario del estudiante, lo agrega a la lista y lo devuelve"""
    promedio = calcular_promedio(notas)
    estudiante = {
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio,
        "estado": obtener_estado(promedio)
    }
    lista.append(estudiante)
    return estudiante


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


def texto_estudiante(estudiante):
    """Devuelve una linea de texto con los datos de un estudiante"""
    return (estudiante["nombre"] + "  |  Notas: " + str(estudiante["notas"]) +
            "  |  Promedio: " + str(round(estudiante["promedio"], 2)) +
            "  |  " + estudiante["estado"])


# ---------- Funciones de la ventana ----------

def actualizar_lista():
    """Borra la lista de la ventana y la vuelve a llenar"""
    lista_pantalla.delete(0, tk.END)
    for estudiante in estudiantes:
        lista_pantalla.insert(tk.END, texto_estudiante(estudiante))


def limpiar_campos():
    """Deja vacios los cuadros de texto"""
    campo_nombre.delete(0, tk.END)
    for campo in campos_notas:
        campo.delete(0, tk.END)
    campo_nombre.focus()


def registrar():
    """Se ejecuta al pulsar el boton Registrar"""
    nombre = campo_nombre.get().strip()

    if nombre == "":
        messagebox.showwarning("Dato faltante", "Escribe el nombre del estudiante.")
        return

    if buscar_estudiante(estudiantes, nombre) != None:
        messagebox.showwarning("Repetido", "Ese estudiante ya esta registrado.")
        return

    notas = []
    posicion = 0
    for campo in campos_notas:
        texto = campo.get().strip()
        if not nota_valida(texto):
            messagebox.showerror("Nota incorrecta",
                                 "La nota de " + EVALUACIONES[posicion] + " debe ser un numero entre 0 y 10.")
            return
        notas.append(float(texto))
        posicion = posicion + 1

    estudiante = agregar_estudiante(estudiantes, nombre, notas)
    actualizar_lista()
    limpiar_campos()
    messagebox.showinfo("Registrado", estudiante["nombre"] + "\nPromedio: " +
                        str(round(estudiante["promedio"], 2)) + "\nEstado: " + estudiante["estado"])


def buscar():
    """Se ejecuta al pulsar el boton Buscar"""
    nombre = campo_nombre.get().strip()

    if nombre == "":
        messagebox.showwarning("Dato faltante", "Escribe en el nombre a quien quieres buscar.")
        return

    estudiante = buscar_estudiante(estudiantes, nombre)

    if estudiante == None:
        messagebox.showinfo("Busqueda", "No se encontro a " + nombre + ".")
    else:
        mensaje = "Estudiante: " + estudiante["nombre"] + "\n"
        posicion = 0
        for evaluacion in EVALUACIONES:
            mensaje = mensaje + evaluacion + ": " + str(estudiante["notas"][posicion]) + "\n"
            posicion = posicion + 1
        mensaje = mensaje + "Promedio: " + str(round(estudiante["promedio"], 2)) + "\n"
        mensaje = mensaje + "Estado: " + estudiante["estado"]
        messagebox.showinfo("Busqueda", mensaje)


def ver_resumen():
    """Se ejecuta al pulsar el boton Resumen del curso"""
    if len(estudiantes) == 0:
        messagebox.showinfo("Resumen", "Todavia no hay estudiantes registrados.")
        return

    resumen = calcular_resumen(estudiantes)
    mensaje = "Estudiantes registrados: " + str(resumen["total"]) + "\n"
    mensaje = mensaje + "Promedio del curso: " + str(round(resumen["promedio_curso"], 2)) + "\n"
    mensaje = mensaje + "Aprobados: " + str(resumen["aprobados"]) + "\n"
    mensaje = mensaje + "Reprobados: " + str(resumen["reprobados"]) + "\n"
    mensaje = mensaje + "Mejor promedio: " + resumen["mejor"]["nombre"] + " (" + str(round(resumen["mejor"]["promedio"], 2)) + ")\n"
    mensaje = mensaje + "Menor promedio: " + resumen["menor"]["nombre"] + " (" + str(round(resumen["menor"]["promedio"], 2)) + ")"
    messagebox.showinfo("Resumen del curso", mensaje)


# ---------- Construccion de la ventana ----------

ventana = tk.Tk()
ventana.title("Registro de calificaciones")
ventana.geometry("620x460")

titulo = tk.Label(ventana, text="Registro de calificaciones del curso", font=("Arial", 14, "bold"))
titulo.grid(row=0, column=0, columnspan=4, pady=10)

tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=4, sticky="e")
campo_nombre = tk.Entry(ventana, width=40)
campo_nombre.grid(row=1, column=1, columnspan=3, padx=10, pady=4, sticky="w")

# Se crea un cuadro de texto por cada evaluacion de la tupla
campos_notas = []
fila = 2
for evaluacion in EVALUACIONES:
    tk.Label(ventana, text=evaluacion + " (0 a 10):").grid(row=fila, column=0, padx=10, pady=4, sticky="e")
    campo = tk.Entry(ventana, width=10)
    campo.grid(row=fila, column=1, padx=10, pady=4, sticky="w")
    campos_notas.append(campo)
    fila = fila + 1

tk.Button(ventana, text="Registrar", width=14, command=registrar).grid(row=5, column=0, padx=6, pady=10)
tk.Button(ventana, text="Buscar", width=14, command=buscar).grid(row=5, column=1, padx=6, pady=10)
tk.Button(ventana, text="Resumen del curso", width=16, command=ver_resumen).grid(row=5, column=2, padx=6, pady=10)
tk.Button(ventana, text="Limpiar", width=12, command=limpiar_campos).grid(row=5, column=3, padx=6, pady=10)

tk.Label(ventana, text="Estudiantes registrados:").grid(row=6, column=0, columnspan=4, padx=10, sticky="w")
lista_pantalla = tk.Listbox(ventana, width=95, height=12)
lista_pantalla.grid(row=7, column=0, columnspan=4, padx=10, pady=6)

campo_nombre.focus()
ventana.mainloop()
