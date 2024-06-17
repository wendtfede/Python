from datetime import datetime

nombre = input("ingresa tu nombre: ")

anio_nacimiento = int(input("introduce tu año de nacimiento: "))

anio_actual = datetime.now().year

edad = anio_actual- anio_nacimiento

if edad >= 18:
    print(f"bienvenido {nombre} puedes participar porque tienes {edad} años y eres mayor")

else:
    print(f"{nombre} no puedes participar porque tienes {edad} años eres menor")
