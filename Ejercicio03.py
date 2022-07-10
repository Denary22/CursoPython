#Ejercicio 03: Diccionarios
#Reyes Lugo Luz Daniela

#Diccionario con los producto:precio
verduras = {"brocoli":8.55,"pepino":6.87,"calabaza":11.55,"chayote":14.33}

#Pedir al usuarios los datos
print("\tEjercicio 03")
verdura = input("Ingrese la verdura que desea comprar: ").lower()
kilos = int(input("Ingrese el número de kilos: "))


if verdura in verduras:
    total = round((kilos * verduras[verdura]),2)

    print("\nDe " +str(kilos)+"kg de " +verdura)
    print("TOTAL: $"+str(total))
else:
    print("\nLo siento :(\nNo existe la verdura que ingreso")
    

    




