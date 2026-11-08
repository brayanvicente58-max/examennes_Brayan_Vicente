class PersonaTransaccion:
    def __init__(self, nombre, saldo_inicial=0.0):
        self.nombre = nombre
        try:
            self.saldo = float(saldo_inicial)
        except ValueError:
            self.saldo = 0.0

    def consultar_saldo(self):
        return f"Titular: {self.nombre} | Saldo disponible: S/. {self.saldo:.2f}"

    def transferir(self, destinatario, monto):
        print(f"\n[Intentando Transacción] De {self.nombre} hacia {destinatario.nombre} por S/. {monto}")

        try:
            monto_num = float(monto)
        except (ValueError, TypeError):
            print("Error: El monto ingresado no es un valor numérico válido.")
            return False

        if monto_num <= 0:
            print("Error: El monto de la transferencia debe ser mayor a cero.")
            return False

        if monto_num > self.saldo:
            print(f"Error: Saldo insuficiente. {self.nombre} cuenta con S/. {self.saldo:.2f}, lo cual es menor al monto solicitado (S/. {monto_num:.2f}).")
            print("-> La transacción no pudo realizarse. Los saldos se conservan sin cambios.")
            return False

        self.saldo -= monto_num
        destinatario.saldo += monto_num
        print("¡La única transacción se realizó con éxito!")
        return True


def mostrar_saldos(p1, p2):
    print(f"\n--- Consulta de Saldo ---")
    print(p1.consultar_saldo())
    print(p2.consultar_saldo())


#Ejecución del Ejercicio 2
if __name__ == "__main__":
    print("=== EJERCICIO 2: CONSULTAS Y TRANSACCIÓN ===")

    nombre1 = input("Ingrese el nombre de la Persona 1 (Remitente): ").strip()
    saldo1 = input(f"Ingrese el saldo inicial para {nombre1}: ")
    p1 = PersonaTransaccion(nombre1, saldo1)

    nombre2 = input("Ingrese el nombre de la Persona 2 (Destinatario): ").strip()
    saldo2 = input(f"Ingrese el saldo inicial para {nombre2}: ")
    p2 = PersonaTransaccion(nombre2, saldo2)

    print("\n[PASO 1: Consulta de saldos iniciales]")
    mostrar_saldos(p1, p2)

    print("\n[PASO 2: Ejecución de la transacción]")
    while True:

        monto_ingresado = input(f"Ingrese el monto para la transferencia de {p1.nombre} a {p2.nombre}: S/. ")

        if p1.transferir(p2, monto_ingresado):
            break
        else:
            print("Intento fallido. Vuelva a intentarlo hasta que la transacción se concrete.\n")

    print("\n[PASO 3: Consulta final de saldos actualizados]")
    mostrar_saldos(p1, p2)
    print("\n¡Proceso finalizado con éxito!")