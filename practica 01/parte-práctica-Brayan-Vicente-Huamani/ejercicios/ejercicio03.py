"""
PRÁCTICA 01 - Módulo I (Python)
Ejercicio 3:
- Nombrar el nuevo entorno virtual según el problema; por ejemplo:
propinas_env. Mostrar una captura del entorno virtual vacío.
- Instalar las librerías del requirements.txt obtenido en el problema anterior en
este nuevo entorno virtual
- Mostrar las librerías instaladas en el nuevo entorno virtual (screemshot)
- Mostrar el proceso de instalación exitoso de todas las dependencias que se
verá en la terminal sobre este nuevo entorno virtual.
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
"""

total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina: "))
num_personas = int(input("Número de personas: "))

monto_propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + monto_propina
monto_por_persona = total_con_propina / num_personas

print("\nMonto total con propina: S/."f"{total_con_propina:.2f}")
print("Cada persona debe pagar: S/."f"{monto_por_persona:.2f}")

if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")