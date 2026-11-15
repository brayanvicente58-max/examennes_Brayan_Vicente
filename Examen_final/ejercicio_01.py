class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int = 2020):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio if anio > 0 else 2020

    def actualizar_marca(self, nueva_marca: str) -> None:
        if nueva_marca.strip():
            self.marca = nueva_marca.strip()
        else:
            print("Error: La marca no puede estar vacía.")

    def actualizar_anio(self, nuevo_anio: int) -> None:
        if isinstance(nuevo_anio, int) and nuevo_anio > 0:
            self.anio = nuevo_anio
        else:
            print(f"Error: El año ({nuevo_anio}) debe ser un entero mayor que cero.")

    def mostrar_datos(self) -> None:
        print(f"Vehículo: {self.marca} {self.modelo} | Año: {self.anio}")


class VehiculoAlquiler(Vehiculo):
    def __init__(self, marca: str, modelo: str, codigo: str, tarifa_diaria: float, anio: int = 2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        # Encapsulamiento de tarifa_diaria
        self.__tarifa_diaria = 0.0
        self.actualizar_tarifa(tarifa_diaria)

    def obtener_tarifa(self) -> float:
        return self.__tarifa_diaria

    def actualizar_tarifa(self, nueva_tarifa: float) -> None:
        if isinstance(nueva_tarifa, (int, float)) and nueva_tarifa > 0:
            self.__tarifa_diaria = float(nueva_tarifa)
        else:
            print(f"[Validación] Error: La tarifa ({nueva_tarifa}) debe ser mayor que cero. No se modificó.")

    def aumentar_tarifa(self, porcentaje: float = 10) -> None:
        if porcentaje > 0:
            incremento = self.__tarifa_diaria * (porcentaje / 100)
            self.__tarifa_diaria += incremento
            print(f"Tarifa de {self.codigo} incrementada en {porcentaje}%. Nueva tarifa: S/ {self.__tarifa_diaria:.2f}")
        else:
            print("Error: El porcentaje de incremento debe ser positivo.")

    def calcular_descuento(self, dias_alquiler: int) -> tuple[float, float, float]:
        """Calcula el importe base, el descuento aplicado y el total final."""
        if dias_alquiler <= 0:
            raise ValueError("Los días de alquiler deben ser mayores a cero.")

        importe_base = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            tasa_descuento = 0.05  # 5%
        elif 2 <= dias_alquiler <= 5:
            tasa_descuento = 0.10  # 10%
        else:
            tasa_descuento = 0.15  # 15%

        monto_descuento = importe_base * tasa_descuento
        total_final = importe_base - monto_descuento
        return importe_base, monto_descuento, total_final

    def mostrar_detalle_alquiler(self, dias_alquiler: int) -> None:
        self.mostrar_datos()
        importe_base, descuento, total = self.calcular_descuento(dias_alquiler)
        print(f"Código: {self.codigo} | Tarifa diaria actual: S/ {self.__tarifa_diaria:.2f}")
        print(f"Días de alquiler: {dias_alquiler}")
        print(f"Importe antes de descuento: S/ {importe_base:.2f}")
        print(f"Descuento aplicado: S/ {descuento:.2f}")
        print(f"Total final a pagar: S/ {total:.2f}")
        print("-" * 50)


# --- PRUEBAS ---
if __name__ == "__main__":
    print("=== PRUEBAS SISTEMA DE ALQUILER DE VEHÍCULOS ===\n")

    # 1. Crear dos vehículos diferentes
    auto1 = VehiculoAlquiler("Toyota", "Corolla", "VH-001", 120.0, 2023)
    auto2 = VehiculoAlquiler("Hyundai", "Tucson", "VH-002", 180.0)  # Usa año por defecto 2020

    # 2. Aplicar dos incrementos consecutivos a la tarifa de uno de ellos
    print(">> Aplicando incrementos a auto1:")
    auto1.aumentar_tarifa()      # Incremento por defecto (10%) -> 132.0
    auto1.aumentar_tarifa(15)    # Segundo incremento (15%) -> 151.8
    print()

    # 3. Calcular descuentos e importes finales con distintas cantidades de días
    print(">> Cálculos de alquiler:")
    auto1.mostrar_detalle_alquiler(1)  # Menos de 2 días (5%)
    auto2.mostrar_detalle_alquiler(4)  # Entre 2 y 5 días (10%)
    auto2.mostrar_detalle_alquiler(7)  # Más de 5 días (15%)

    # 4. Intentar asignar una tarifa negativa y verificar que no se modifique
    print(">> Prueba de tarifa negativa en auto2:")
    print(f"Tarifa antes del intento: S/ {auto2.obtener_tarifa():.2f}")
    auto2.actualizar_tarifa(-50.0)
    print(f"Tarifa después del intento: S/ {auto2.obtener_tarifa():.2f}")