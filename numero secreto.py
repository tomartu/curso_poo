numero_secreto=10

while True:
    numero=input("ingresa el numero secreto: ")

    try:
        numero= int(numero)
    except:
        print("no es un numero")
        continue
    if numero  != numero_secreto:
        if numero > numero_secreto:
            print("el numero es menor")

        elif numero < numero_secreto:
            print("el numero es mayor")
        else:
            print("adivinaste: ",numero_secreto)
