# Ejercicio 2: División segura con ZeroDivisionError
try:
    dividendo = float(input("Ingrese el dividendo: "))
    divisor   = float(input("Ingrese el divisor: "))
    resultado = dividendo / divisor
    print(f"Resultado: {dividendo} / {divisor} = {resultado}")
except ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: ingrese únicamente valores numéricos.")