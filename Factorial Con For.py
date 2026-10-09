# Ejercicio 5: Calcular el factorial de un número
n = int(input("Ingrese un número entero no negativo: "))

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(f"El factorial de {n} es: {factorial}")