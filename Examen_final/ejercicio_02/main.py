import operaciones


def ejecutar_flujo(cantidad: int, pos_valida: int, pos_invalida: int) -> None:
    print(f"--- Ejecución con n = {cantidad} ---")
    try:
        lista_original = operaciones.generar_lista(cantidad)
        sin_duplicados = operaciones.eliminar_duplicados(lista_original)
        asc, desc = operaciones.ordenar_listas(sin_duplicados)
        mayor_par = operaciones.obtener_mayor_par(sin_duplicados)

        print(f"Lista original:       {lista_original}")
        print(f"Sin duplicados:       {sin_duplicados}")
        print(f"Orden ascendente:     {asc}")
        print(f"Orden descendente:    {desc}")
        print(f"Mayor número par:     {mayor_par}")

        # Prueba de posición válida
        elem_valido = operaciones.obtener_elemento(sin_duplicados, pos_valida)
        print(f"Elemento en pos [{pos_valida}]:  {elem_valido}")

        # Prueba de posición fuera de rango
        print(f"Intentando acceder a pos [{pos_invalida}]...")
        operaciones.obtener_elemento(sin_duplicados, pos_invalida)

    except (ValueError, IndexError) as error:
        print(f"[Excepción capturada]: {error}")
    print()


# --- PRUEBAS OBLIGATORIAS ---
if __name__ == "__main__":
    print("=== PRUEBAS PROCESAMIENTO DE NÚMEROS ===\n")

    # 1. Dos ejecuciones con cantidades distintas (incluyendo posición válida y fuera de rango)
    ejecutar_flujo(cantidad=10, pos_valida=2, pos_invalida=25)
    ejecutar_flujo(cantidad=6, pos_valida=0, pos_invalida=10)

    # 2. Probar una cantidad n inválida
    ejecutar_flujo(cantidad=-5, pos_valida=0, pos_invalida=1)