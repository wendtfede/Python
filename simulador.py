print("simulador de factura de electricidad")

def menu():
    print("opcion 1: tarifa residencial")
    print("opcion 2: tarifa comercial")
    print("opcion 3: salir")

menu()

lecturaAnterior = int(input("ingrese lectura anterior: "))
lecturaActual = int(input("ingrese lectura actual: "))

consumo = lecturaActual - lecturaAnterior

opcion = int(input("ingrese una opcion del menu (en numero): "))

if opcion == 1:
    precioKw = 35.65
    cargos = [365, 75.25, 1.21]

    monto = precioKw*consumo+cargofijo[0]+muni[1]+iva[2]

    if consumo <= 400:
        bonif = 250

        total = monto - bonif

        print(f"su factura es de {consumo} kw tiene bonificacion y debe pagar {total}")

    else:
        print(f"su factura es de {consumo} kw y debe pagar {monto}")

elif opcion == 2:
    precioKw = 135.36
    cargos = [506, 102.03, 2.25]

    monto = precioKw*consumo+cargofijo[0]+muni[1]+iva[2]

    if consumo <= 600:
        bonif = 150

        total = monto - bonif

        print(f"su factura es de {consumo} kw tiene bonificacion y debe pagar {total}")

    else:
        print(f"su factura es de {consumo} kw y debe pagar {monto}")

else:
    print("Ha decidido salir. Gracias por utilizar el programa")