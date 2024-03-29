class empleados():
    cantidadEmp=50
    hsJornada=8
    hsSemanales=40
    empleadosAusentes=5
    turnoMañana=False
    turnoTarde=true

    def turno(self):
        self.turnoMañana=True
    
   
    def estado(self):
        if (self.turnoMañana):
            return "turno mañana esta trabajando"
        else:
            return "turno mañana no esta trabajando"


nomina=empleados()

print("la cantidad de la nomina es de : ",nomina.cantidadEmp)
print ("La cantidad neta de empleados trabajando es de : ",nomina.cantidadEmp-nomina.empleadosAusentes)
print("la horas semanales de la nomina es de: ",nomina.hsSemanales)
print(nomina.estado()) 

