"""
PRÁCTICA 01
Ejercicio 4:
Crea una lista vacía y realiza lo siguiente:
- Agrega los nombres de tres participantes.
- Inserta un nuevo participante en la segunda posición.
- Actualiza el nombre del primer participante.
- Elimina uno de los participantes.
- Muestra la lista final y la cantidad de participantes registrados.
- No utilizar ciclos ni recorridos.
"""

participantes = []

participantes.append("Ana")
participantes.append("Carlos")
participantes.append("David")

participantes.insert(1, "Beatriz")

participantes[0] = "Alicia"

participantes.remove("Carlos")

print("Lista final de participantes:", participantes)
print("Cantidad de participantes registrados:", len(participantes))