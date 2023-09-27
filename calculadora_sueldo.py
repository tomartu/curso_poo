maquinista: float = 211203.00
recibidor: float = 211203.00
comida_viatico: float = 5383.63

categoria = input("ingrese si categoria Maquinista (M) o recibidor (R): ")
Dias = input("cuantos dias laborables tuvo el mes: ")
Dias_laborables = int(Dias) * comida_viatico

if categoria == "M":
    print("Sueldo es de :"+str(maquinista))
    print("Sueldo viatico y comida es de : "+str(Dias_laborables))
elif categoria == "R":
    print("Sueldo es de :"+str(recibidor))
    print("Sueldo viatico y comida es de : "+str(Dias_laborables))
    