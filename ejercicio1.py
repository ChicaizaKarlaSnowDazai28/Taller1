radio= float(input("Escribe el radio del círculo: "))
if radio >0:
    pi = 3.1416
    area = pi * radio * radio
    perimetro = 2 * pi * radio

    print("El area del círculo es: ", area)
    print("El perímetro del circulo es: ", perimetro)

else:
    print("El radio debe ser un valor positivo")