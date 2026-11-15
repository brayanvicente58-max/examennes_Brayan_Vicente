def mostrar_inventario(inventario: dict) -> None:
    #Muestra todos los productos disponibles y sus detalles.
    print("\n--- ESTADO ACTUAL DEL INVENTARIO ---")
    print(f"{'Código':<10} {'Nombre':<22} {'Precio (S/)':<15} {'Stock':<10}")
    print("-" * 60)
    for codigo, datos in inventario.items():
        print(f"{codigo:<10} {datos['nombre']:<22} {datos['precio']:<15.2f} {datos['cantidad']:<10}")
    print("-" * 60)


def registrar_compra(inventario: dict, codigo_producto: str, cantidad_solicitada: int) -> float | None:
    """Valida existencia/stock, calcula importe y descuenta del inventario."""
    print(f"\n>> Procesando compra: Producto '{codigo_producto}' | Cantidad: {cantidad_solicitada}")

    if codigo_producto not in inventario:
        print(f"Error: El producto '{codigo_producto}' no existe en el inventario.")
        return None

    if cantidad_solicitada <= 0:
        print("Error: La cantidad solicitada debe ser mayor a cero.")
        return None

    producto = inventario[codigo_producto]

    if cantidad_solicitada > producto["cantidad"]:
        print(f"Error: Stock insuficiente para '{producto['nombre']}'. Disponible: {producto['cantidad']}.")
        return None

    # Compra válida: calcular importe y actualizar existencias
    importe_total = producto["precio"] * cantidad_solicitada
    producto["cantidad"] -= cantidad_solicitada

    print(f"Compra exitosa: {cantidad_solicitada}x {producto['nombre']} -> Total a pagar: S/ {importe_total:.2f}")
    return importe_total


def calcular_valor_inventario(inventario: dict) -> float:
    """Retorna el valor monetario total de todos los productos en stock."""
    return sum(datos["precio"] * datos["cantidad"] for datos in inventario.values())


# --- PRUEBAS OBLIGATORIAS ---
if __name__ == "__main__":
    print("=== PRUEBAS CONTROL DE INVENTARIO ===")

    # Diccionario inicial con al menos cuatro productos
    inventario_tienda = {
        "P001": {"nombre": "Laptop Lenovo", "precio": 2800.00, "cantidad": 5},
        "P002": {"nombre": "Mouse Inalámbrico", "precio": 65.00, "cantidad": 20},
        "P003": {"nombre": "Teclado Mecánico", "precio": 190.00, "cantidad": 12},
        "P004": {"nombre": "Monitor 24 pulgadas", "precio": 650.00, "cantidad": 8},
    }

    # 1. Mostrar inventario inicial
    mostrar_inventario(inventario_tienda)
    print(f"Valor monetario inicial: S/ {calcular_valor_inventario(inventario_tienda):.2f}")

    # 2. Realizar una compra válida
    registrar_compra(inventario_tienda, "P001", 2)

    # 3. Realizar compra de un producto inexistente
    registrar_compra(inventario_tienda, "P999", 1)

    # 4. Realizar compra con cantidad superior al stock
    registrar_compra(inventario_tienda, "P004", 15)

    # 5. Mostrar inventario actualizado y su valor monetario total
    mostrar_inventario(inventario_tienda)
    valor_final = calcular_valor_inventario(inventario_tienda)
    print(f"Valor monetario total actualizado: S/ {valor_final:.2f}")