"""
PRÁCTICA 01
Ejercicio 2:
- El entorno virtual debe tener un nombre relacionado con el problema; por
ejemplo: calificaciones_env.
- Instalar las siguientes librerías: Django: 5.0.6, fastapi: 0.112.0, numpy: 2.0.0 y
aws (última versión)
- Generar el archivo de requirements.txt (mostrar las librerías instaladas)
- Caso: Reporte de calificaciones:
Se tiene un alumno con calificaciones en tres cursos:
Matemáticas: 17, Ciencia: 14, Historia: 15
Cada curso tiene un peso diferente en la nota final:
Matemáticas: 40%, Ciencia: 30%, Historia: 30%
Realizar lo que se pide a continuación:
Calcula la nota final ponderada del alumno.
Muestra un mensaje como: "La nota final es: 15.6" con 1 decimal.
Evalúa si el alumno aprueba (nota final >= 13.0). Muestra un mensaje booleano:
"¿Aprobado?: True" o "¿Aprobado?: Sí"
Genera una cadena resumen que diga:
"El estudiante obtuvo una nota final de 15.6 y su estado final es: Aprobado"
En caso no apruebe indicar lo contrario en los mensajes.
"""

nota_matematicas = 17
nota_ciencia = 14
nota_historia = 15

peso_matematicas = 0.40
peso_ciencia = 0.30
peso_historia = 0.30

nota_final = (nota_matematicas * peso_matematicas) + (nota_ciencia * peso_ciencia) + (nota_historia * peso_historia)

print("La nota final es:",f"{nota_final:.1f}")

aprobado = nota_final >= 13.0
print("¿Aprobado?:{}".format(aprobado))

if aprobado:
    print("El estudiante obtuvo una nota final de {} y su estado final es aprobado".format(f"{nota_final:.1f}"))
else:
    print("Desaprobado")
