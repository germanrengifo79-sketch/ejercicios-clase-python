precio = float(input("Ingrese el precio del producto: ")) 
descuento = float(input("Ingrese el porcentaje de descuento: ")) 
valor_descuento = precio * descuento/100
precio_final = precio - valor_descuento 
print("El precio final a pagar es:", precio_final)
