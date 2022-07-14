#Ejercicio 04: Calculadora básica.
#*Sin funciones.
#Reyes Lugo Luz Daniela.

#Lista historial
historial = []

print("\tCALCULADORA BÁSICA")
while True:
    entrada = input("\nDeseas realizar alguna operación (Y/n): ")
    if entrada == "n":
        break

    #Menú
    print("\tMENU")
    print("1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Historial")
    opcion = input("Ingrese la opción: ")

    if opcion == "1":
        valor1 = int(input("\nIngrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        suma = valor1 + valor2
        t = f"SUMA: {valor1} + {valor2} = {suma}"
        historial.append(t)
        print("La suma es: "+str(suma))
        print(f"{valor1} + {valor2} = {suma}")
            
    elif opcion == "2":
        valor1 = int(input("\nIngrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        resta = (valor1) - (valor2)
        t = f"RESTA: {valor1} - {valor2} = {resta}"
        historial.append(t)
        print("La resta es: "+str(resta))
        print(f"{valor1} - {valor2} = {resta}")

    elif opcion == "3":
        valor1 = int(input("\nIngrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        mult = valor1 * valor2
        t = f"MULTIPLICACIÓN: {valor1} * {valor2} = {mult}"
        historial.append(t)
        print("La multiplicación es: "+str(mult))
        print(f"{valor1} * {valor2} = {mult}")

    elif opcion == "4":
        valor1 = int(input("\nIngrese el primer valor: "))
        valor2 = int(input("Ingrese el segundo valor: "))
        div = valor1 / valor2
        t = f"DIVISIÓN: {valor1} / {valor2} = {div}"
        historial.append(t)
        print("La división es: "+str(div))
        print(f"{valor1} / {valor2} = {div}")
    
    elif opcion == "5":
        if not historial:
            print("\nEl historial esta vacio.")
        else:
            print("\n\tHistorial")
            for x in historial:
                print(x)
            
            eliminar = input("\n¿Desea eliminar el historial? (y/n): ")
            if eliminar=="y":
                historial.clear()
                print("Historial eliminado!!")
    else:

        print("Esta opción no existe. :c")
