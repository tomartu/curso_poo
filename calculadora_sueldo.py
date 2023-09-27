Maquinista: float = 211203.00
Recibidor: float = 211203.00
Comida_viatico: float = 5383.63

categoria = input("ingrese si categoria Maquinista (M) o Recibidor (R): ")
Dias=input("cuantos dias laborables tuvo el mes: ")
Dias_laborables = int(Dias) * Comida_viatico

if categoria == "M":
    print("sueldo es de :"+str(Maquinista))
    print("sueldo viatico y comida es de : "+str(Dias_laborables))
elif categoria == "R":
    print("sueldo es de :"+str(Recibidor))
    print("sueldo viatico y comida es de : "+str(Dias_laborables))