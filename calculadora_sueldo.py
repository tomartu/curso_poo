def imprimir_valores(monto_categoria, monto_viatico):
    print("Honorarios es de :"+str(monto_categoria))
    print("Honorarios viatico y comida es de : "+str(monto_viatico))

Maquinista: float = 211203.00
Recibidor: float = 211203.00
Comida_viatico: float = 5383.63

categoria = input("ingrese si categoria Maquinista (M) o Recibidor (R): ")
Dias = input("cuantos dias laborables tuvo el mes: ")
Dias_laborables = int(Dias) * Comida_viatico

if categoria == "M":
    imprimir_valores(Maquinista, Dias_laborables)
elif categoria == "R":
    imprimir_valores(Recibidor, Dias_laborables)


