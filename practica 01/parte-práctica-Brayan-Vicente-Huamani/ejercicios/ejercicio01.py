"""
PRÁCTICA 01
Ejercicio 1:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un
usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una
conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su
salario, según corresponda.

"""

nombre = "Carlos Perez"
salario = 2500.00
edad = "32"
compania = "Tech Solutions"

print("--- TIPOS DE VARIABLES INICIALES ---")
print("nombre:",type(nombre))
print("salario:",type(salario))
print("edad:",type(edad))
print("compañía:" ,type(compania))
print("-------------------------------------")

edad_int = int(edad)

if edad_int > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    porcentaje_bono = 0.10
else:
    print("Usted tiene un bono del 5% en el mes diciembre")
    porcentaje_bono = 0.05

bono_final = (salario ** 2) + (salario * porcentaje_bono)

print("El bono final es: S/.",f"{bono_final:,.2f}")