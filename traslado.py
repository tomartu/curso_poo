
def traslado_2007():
    print ("su tralado es de: "+str(traslado))

traslado:float=14500.55

pago_traslado=input("indique si ingreso a la empresa antes del 09/2007 (si) o (no): " )

if pago_traslado == "si":
    traslado_2007()
elif pago_traslado =="no":
    print("No cuenta con traslado")

