# Ejercicio 3: else y finally
# else  → se ejecuta solo si NO ocurrió ninguna excepción
# finally → se ejecuta SIEMPRE, con o sin error

try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else:
    if edad >= 18:
        print("Acceso permitido.")
    else:
        print("Acceso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")