from datetime import datetime
from functools import wraps


def registrar_pedido(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[PEDIDO RAPPI - {ahora}] Iniciando operación '{func.__name__}'...")
        resultado = func(*args, **kwargs)
        if resultado is not None:
            print(f"[PEDIDO RAPPI] Operación '{func.__name__}' finalizada correctamente.\n")
        else:
            print(f"[PEDIDO RAPPI] Operación '{func.__name__}' abortada por datos inválidos.\n")
        return resultado
    return wrapper


@registrar_pedido
def calcular_total(*args: tuple[str, float]) -> float | None:

    if not args:
        print("Error: No se ingresaron productos para calcular.")
        return None

    # Validamos estructura y precios
    for item in args:
        if not isinstance(item, tuple) or len(item) != 2:
            print("Error: Cada argumento debe ser una tupla con (nombre_producto, precio).")
            return None
        _, precio = item
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            print(f"Error: El precio del producto '{item[0]}' (S/ {precio}) no es válido.")
            return None

    print(f"Detalle de productos del pedido (Total: {len(args)} ítems):")
    precios = []
    for producto, precio in args:
        print(f"  - {producto}: S/ {precio:.2f}")
        precios.append(precio)

    total = sum(precios)
    print(f"Importe total calculado: S/ {total:.2f}")
    return total


@registrar_pedido
def procesar_pedido(cliente: str, **kwargs: float) -> float | None:
    #Recibe el nombre del cliente y productos con sus precios (**kwargs) detallando cada nombre.
    if not kwargs:
        print(f"Error: El pedido de {cliente} no contiene productos.")
        return None

    # Verificamos si hay precios inválidos (como negativos) para detallar cada uno
    precios = list(kwargs.values())
    hay_invalidos = any(
        not isinstance(p, (int, float)) or isinstance(p, bool) or p <= 0
        for p in precios
    )

    if hay_invalidos:
        print(f"Cliente: {cliente}")
        print("Detalle de productos ingresados:")
        for producto, precio in kwargs.items():
            valido = isinstance(precio, (int, float)) and not isinstance(precio, bool) and precio > 0
            estado = "Válido" if valido else "INVÁLIDO (Precio <= 0 o no numérico)"
            print(f"  - {producto.replace('_', ' ')}: S/ {precio:.2f} -> [{estado}]")
        print(f"Error en el pedido de {cliente}: Se detectó al menos un precio inválido. No se procesará el total.")
        return None

    print(f"Cliente: {cliente}")
    print("Detalle de productos del pedido:")
    for producto, precio in kwargs.items():
        print(f"  - {producto.replace('_', ' ')}: S/ {precio:.2f}")

    total = sum(precios)
    print(f"Importe total del pedido: S/ {total:.2f}")
    return total


# --- PRUEBAS OBLIGATORIAS ---
if __name__ == "__main__":
    print("=== PRUEBAS SISTEMA DE PEDIDOS RAPPI (CON NOMBRES DE PRODUCTOS) ===\n")

    # 1. Ejecutar calcular_total con tres y seis ítems (pasando nombre y precio en tuplas)
    print("--- Prueba 1: calcular_total con 3 productos ---")
    calcular_total(
        ("Salchipapa Familiar", 22.50),
        ("Inka Kola 1.5L", 8.00),
        ("Tequeños de Queso", 15.00)
    )

    print("--- Prueba 2: calcular_total con 6 productos ---")
    calcular_total(
        ("Lomo Saltado", 32.00),
        ("Arroz Chaufa de Pollo", 26.50),
        ("Chicha Morada 1L", 9.00),
        ("Papa Rellena", 7.50),
        ("Anticuchos", 20.00),
        ("Picarones", 10.00)
    )

    # 2. Registrar pedidos con **kwargs (nombres como nombres de argumentos)
    print("--- Prueba 3: Pedido con 4 productos válidos ---")
    procesar_pedido(
        cliente="Carlos Mendoza",
        Hamburguesa_Royal=24.90,
        Papas_Fritas=9.50,
        Gaseosa_500ml=5.00,
        Helado_Artart=7.50
    )

    print("--- Prueba 4: Pedido con un precio negativo ---")
    procesar_pedido(
        cliente="Ana Torres",
        Pizza_Familiar=45.00,
        Alitas_BBQ=-18.00,
        Limonada_Frozen=8.00
    )