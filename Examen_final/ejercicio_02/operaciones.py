import random

def generar_lista(n: int) -> list[int]:
    #Genera una lista de n enteros aleatorios entre 1 y 100.
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("La cantidad 'n' debe ser un número entero positivo mayor a cero.")
    return [random.randint(1, 100) for _ in range(n)]


def eliminar_duplicados(lista: list[int]) -> list[int]:
    #Retorna una nueva lista sin elementos repetidos manteniendo el orden.
    return list(dict.fromkeys(lista))


def ordenar_listas(lista: list[int]) -> tuple[list[int], list[int]]:
    #Retorna dos listas independientes: una ascendente y otra descendente.
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente


def obtener_mayor_par(lista: list[int]) -> int | str:
    #Retorna el mayor número par de la lista o un mensaje si no existen pares.
    pares = [num for num in lista if num % 2 == 0]
    if not pares:
        return "No existen números pares en la lista."
    return max(pares)


def obtener_elemento(lista: list[int], posicion: int) -> int:
    #Retorna el elemento en la posición indicada controlando índices inválidos.
    if not isinstance(posicion, int) or posicion < 0:
        raise IndexError(f"La posición {posicion} no es válida (debe ser un entero >= 0).")
    try:
        return lista[posicion]
    except IndexError:
        raise IndexError(f"Posición {posicion} fuera de rango. La lista tiene {len(lista)} elementos.")