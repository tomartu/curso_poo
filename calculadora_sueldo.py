def imprimir_valores(monto_categoria, monto_viatico):
    print("Honorarios es de :"+str(monto_categoria))
    print("Honorarios viatico y comida es de : "+str(monto_viatico))

maquinista: float = 211203.00
recibidor: float = 211203.00
comida_viatico: float = 5383.63

categoria = input("ingrese si categoria Maquinista (M) o Recibidor (R): ")
# Dias = input("cuantos dias laborables tuvo el mes: ")
# try:
#     Dias_laborables = int(Dias) * Comida_viatico
# except Exception as e:
#     print("Exception: "+str(e))
#     exit()

Dias_laborables = None

while Dias_laborables is None:
    try:
        Dias = input("cuantos dias laborables tuvo el mes: ")
        Dias_laborables = int(Dias) *comida_viatico
    except Exception as e:
        print("Exception: "+str(e))
        print("Debe ingresar un numero válido")
        Dias_laborables = None
        continue
    finally:
        print("Esto se ejecuta SIEMPRE")


if categoria == "M":
    imprimir_valores(maquinista, Dias_laborables)
elif categoria == "R":
    imprimir_valores(Recibidor, Dias_laborables)


