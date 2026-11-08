class Persona:
    def __init__(self, nombre, saldo_inicial=0.0):
        self.nombre = nombre
        try:
            self.saldo = float(saldo_inicial)
        except ValueError:
            self.saldo = 0.0

    def consultar_saldo(self):
        print(f"Saldo actual de {self.nombre}: S/. {self.saldo:.2f}")
        return self.saldo

    def transferir(self, destinatario, monto):
        print(f"\n[Intento de Transferencia] De {self.nombre} hacia {destinatario.nombre} por un monto de S/. {monto}")

        try:
            monto_num = float(monto)
        except (ValueError, TypeError):
            print("Error: El monto ingresado no es un valor numérico válido. Operación cancelada.")
            return False

        if monto_num <= 0:
            print("Error: El monto de la transferencia debe ser mayor a cero. Operación cancelada.")
            return False

        if monto_num > self.saldo:
            print(
                f"Error: Saldo insuficiente. {self.nombre} cuenta con S/. {self.saldo:.2f}, lo cual es menor al monto solicitado (S/. {monto_num:.2f}).")
            print("-> Los saldos se conservan sin cambios.")
            return False

        # Realizar la transferencia exitosa
        self.saldo -= monto_num
        destinatario.saldo += monto_num
        print("¡Transferencia realizada con éxito!")
        self.consultar_saldo()
        destinatario.consultar_saldo()
        return True


#Demostración del Ejercicio 2
if __name__ == "__main__":
    print("\n=== EJERCICIO 2: TRANSFERENCIAS ENTRE PERSONAS ===")

    # Crear dos personas con saldo inicial
    p_envia = Persona("Ana", 400.0)
    p_recibe = Persona("Luis", 150.0)

    p_envia.consultar_saldo()
    p_recibe.consultar_saldo()

    # 1. Transferencia válida
    p_envia.transferir(p_recibe, 100.0)

    # 2. Intento de transferencia rechazado (monto mayor al saldo)
    p_envia.transferir(p_recibe, 900.0)

    # 3. Intento de transferencia rechazado (monto menor o igual a cero)
    p_envia.transferir(p_recibe, -25.0)

    # 4. Intento de transferencia rechazado (monto no numérico)
    p_envia.transferir(p_recibe, "texto_invalido")