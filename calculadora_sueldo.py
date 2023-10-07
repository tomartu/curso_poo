def imprimir_valores(monto_categoria,monto_viatico):
    print("Honorarios es de :"+str(monto_categoria))
    print("Honorarios viatico y comida es de : "+str(monto_viatico))

maquinista: float = 211203.00
recibidor: float = 211203.00
comida_viatico: float = 5383.63

categoria = input("ingrese si categoria Maquinista (M) o recibidor (R): ")
Dias = input("cuantos dias laborables tuvo el mes: ")
Dias_laborables = int(Dias) * comida_viatico

if categoria == "M":
    imprimir_valores(maquinista, Dias_laborables)
elif categoria == "R":
    imprimir_valores(recibidor, Dias_laborables)


