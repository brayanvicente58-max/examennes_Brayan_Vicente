from datetime import datetime

class Persona:
    def __init__(self, nombre="", edad=0, saldo=0.0):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
        self.nacionalidad = "Peruana"
        self.fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M")

    def registrar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ").strip()
        while True:
            try:
                edad_ingresada = int(input(f"Ingrese la edad de {self.nombre}: "))
                if edad_ingresada < 0:
                    print("Error: La edad no puede ser un número negativo. Intente nuevamente.")
                    continue
                self.edad = edad_ingresada
                break
            except ValueError:
                print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

    def cumpleanos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Su nueva edad es {self.edad} años.")

    def mostrar_info(self):
        print(
            f"Nombre: {self.nombre} | Edad: {self.edad} | Nacionalidad: {self.nacionalidad} | Saldo: S/. {self.saldo:.2f}")


def mostrar_fecha_registro(persona):
    print(f"-> Persona: {persona.nombre} | Registrado el: {persona.fecha_registro}")


#Demostración del Ejercicio 1
if __name__ == "__main__":
    print("=== EJERCICIO 1: REGISTRO DE PERSONAS ===")

    # Creación de al menos dos objetos Persona
    persona1 = Persona()
    print("\n[Registro de la Persona 1]")
    persona1.registrar_datos()

    persona2 = Persona()
    print("\n[Registro de la Persona 2]")
    persona2.registrar_datos()

    print("\n--- Estado Inicial y Fecha de Creación ---")
    persona1.mostrar_info()
    mostrar_fecha_registro(persona1)

    persona2.mostrar_info()
    mostrar_fecha_registro(persona2)

    print("\n--- Aplicando el método cumpleaños ---")
    persona1.cumpleanos()
    persona2.cumpleanos()

    print("\n--- Estado Actualizado ---")
    persona1.mostrar_info()
    persona2.mostrar_info()