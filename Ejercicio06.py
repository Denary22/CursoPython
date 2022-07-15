#Ejercicio 06: Funciones
#Reyes Lugo Luz Daniela

def factura(cantidad,porcentaje=16):
    total = cantidad + (cantidad*(porcentaje/100))
    return total

print("\n\tEjercicio 06")

cant = int(input("Ingrese la cantidad: "))
iva = input("Ingrese el porcentaje de IVA: ")
if iva == '':
    print("\nTotal de la factura: $"+str(factura(cant)))
else:
    iva = int(iva)
    print("\nTotal de la factura: $"+str(factura(cant,iva)))
