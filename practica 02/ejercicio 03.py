def solicitar_dos_valores():
    while True:
        try:
            val1 = float(input("Ingrese el primer valor numérico: "))
            val2 = float(input("Ingrese el segundo valor numérico: "))
            return val1, val2
        except ValueError:
            print("Error: Entrada no numérica detectada. Por favor, ingrese solo números válidos.")


def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error crítico: No es posible dividir entre cero.")
        return None
    except TypeError:
        print("Error crítico: Tipos de datos incompatibles para la división.")
        return None
    else:
        print("-> [Éxito] División calculada correctamente.")
        return resultado
    finally:
        print("-> [Finally] Finalizó el bloque de intento de división.")


def sumar(a, b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipos incompatibles para realizar la suma.")
        return None


def registrar_elementos_lista():
    while True:
        try:
            n = int(input("\n¿Cuántos elementos desea registrar en la lista (N)?: "))
            if n <= 0:
                print("El número de elementos debe ser mayor a cero.")
                continue

            lista = []
            for i in range(n):
                elemento = input(f"Ingrese el elemento [{i + 1}]: ")
                try:
                    if '.' in elemento:
                        elemento = float(elemento)
                    else:
                        elemento = int(elemento)
                except ValueError:
                    pass  # Se mantiene como cadena si no es numérico
                lista.append(elemento)
            return lista
        except ValueError:
            print("Error: Debe ingresar un número entero válido para la cantidad de elementos.")


def consultar_indice(lista):
    while True:
        try:
            indice = int(input(f"Ingrese el índice que desea consultar (0 al {len(lista) - 1}): "))
            elemento = lista[indice]
            print(f"-> Elemento encontrado en el índice {indice}: {elemento}")
            return elemento
        except ValueError:
            print("Error: El índice ingresado debe ser un número entero.")
        except IndexError:
            print(f"Error: El índice está fuera de rango. Debe estar entre 0 y {len(lista) - 1}.")


#Demostración del Ejercicio 3
if __name__ == "__main__":
    print("\n=== EJERCICIO 3: FUNCIONES Y MANEJO DE EXCEPCIONES ===")

    print("\n--- Pruebas de operaciones aritméticas ---")
    val1, val2 = solicitar_dos_valores()
    print(f"Resultado de la suma: {sumar(val1, val2)}")
    print(f"Resultado de la división: {dividir(val1, val2)}")

    print("\n--- Pruebas de manejo de listas y consultas ---")
    mi_lista = registrar_elementos_lista()
    print("Lista final generada:", mi_lista)

    consultar_indice(mi_lista)