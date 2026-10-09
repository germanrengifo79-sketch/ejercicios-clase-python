# Ejercicio 1: try / except básico
# Sin manejo de errores, ingresar "hola" en lugar de un número
# provocaría un ValueError y el programa se detendría.

try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: debe ingresar un número entero válido.")