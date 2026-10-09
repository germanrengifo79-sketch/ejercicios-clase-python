# Ejercicio 4: Clasificar una nota académica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
else:
    print("Desempeño bajo")