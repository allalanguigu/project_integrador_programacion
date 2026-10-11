# Registro de calificaciones de un curso

Proyecto integrador de la asignatura **Lógica de Programación**: *El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas*.

## Integrantes

- Alexander Lalangui

## Fecha

10 de octubre de 2026

## Objetivo del sistema

Ayudar a un docente a registrar las calificaciones de su curso y obtener al instante el promedio y el estado de cada estudiante, en lugar de calcularlos a mano en un cuaderno o en hojas sueltas.

## Problema que resuelve

Muchos docentes todavía llevan las notas a mano. Eso toma tiempo, produce errores al sumar y dividir, y hace difícil saber cómo va el curso en conjunto. Un programa sencillo reduce esos errores y deja más tiempo para enseñar.

## Funcionalidades

- **Registrar estudiante:** nombre y tres notas (Parcial 1, Parcial 2 y Examen).
- **Validar datos:** no acepta nombres vacíos, estudiantes repetidos ni notas fuera del rango de 0 a 10.
- **Calcular promedio y estado:** aprueba con promedio mayor o igual a 7.
- **Ver la lista** de estudiantes con sus notas, promedio y estado.
- **Buscar un estudiante** por su nombre.
- **Ver el resumen del curso:** promedio general, aprobados, reprobados, mejor y menor promedio.

## Cómo ejecutarlo

Se necesita Python 3 (tkinter ya viene incluido).

```
python project.py
```

## Estructura del repositorio

```
project.py                 Código del programa
README.md                  Este archivo
<<<<<<< HEAD
docs/diagramas/            Diagramas en formato draw.io y JPG
  casos_de_uso
  arquitectura
  diagrama_flujo_general
  diagrama_flujo_registrar
=======

>>>>>>> 43a52bca37f147f4bc5a7dcb563382843937e6f9
```

## Contenidos de la asignatura aplicados

| Unidad | Tema | Dónde se usa |
|---|---|---|
| 1 | Resolución de problemas y entorno de programación | Análisis del problema, Visual Studio Code, depuración y GitHub |
| 2 | Variables, tipos de datos y operadores | Notas como `float`, nombres como `str`, cálculo del promedio |
| 2 | Algoritmos y diagramas de flujo | Diagramas de la carpeta `docs/diagramas` |
| 3 | Condicionales | Validaciones y estado Aprobado o Reprobado |
| 3 | Bucles | `for` para recorrer notas y estudiantes |
| 4 | Tuplas, listas y diccionarios | Tupla `EVALUACIONES`, lista `estudiantes`, un diccionario por estudiante |
| 4 | Funciones y parámetros | Todo el programa está organizado en funciones |

<<<<<<< HEAD
=======
## Desarrollo de logica
<img width="1360" height="980" alt="arquitectura" src="https://github.com/user-attachments/assets/4edb140b-10d3-442b-bfd0-c9cd40e71415" />
<img width="1360" height="1040" alt="casos_de_uso" src="https://github.com/user-attachments/assets/80d5f869-9182-445b-8ad4-1d04bf6d1d2e" />
<img width="1560" height="1600" alt="diagrama_flujo_general" src="https://github.com/user-attachments/assets/e2962e56-74ff-4489-808a-d2b3da8e9760" />
<img width="1540" height="1840" alt="diagrama_flujo_registrar" src="https://github.com/user-attachments/assets/7b4222de-1ad1-4ad2-a054-e1e1fe89bd79" />




>>>>>>> 43a52bca37f147f4bc5a7dcb563382843937e6f9
## Desarrollo por etapas

1. Menú por consola y registro de estudiantes.
2. Funciones, validación de notas y estado de aprobación.
3. Búsqueda de estudiante y resumen del curso.
4. Interfaz gráfica con tkinter y messagebox.
5. Documentación y diagramas.

## Limitaciones

Los datos se guardan solo mientras el programa está abierto; al cerrarlo se pierden. Guardar en un archivo queda como mejora futura.
