import sys
import math
print("ingrese el precio, el número de usuarios , los gastos y utilidades del año anterior")

precio=float(sys.argv[1])
usuarios=float(sys.argv[2])
gastos=float(sys.argv[3])

utilidadesanoanterior=float(sys.argv[4])

if utilidadesanoanterior is None:
    utilidadesanoanterior=float(1000)

print("utilidades año anterior ")
print(utilidadesanoanterior)

utilidadactual=precio*usuarios-gastos
print("utilidades  sin impuesto actual ")
print(utilidadactual)

if utilidadactual>0:
    impuesto=utilidadactual*0.35
    utilidadmenosimpuestos=utilidadactual-impuesto
    #razon=(utilidadmenosimpuestos/utilidadesanoanterior)*100
    razon=(utilidadesanoanterior/utilidadmenosimpuestos)*100
    print("la razon utilidad actual con la anterior es ")
    print(razon)
else:
    #razon=(utilidadactual/utilidadesanoanterior)*100
    razon=(utilidadesanoanterior/utilidadmenosimpuestos)*100
    print("la razon utilidad actual con la anterior es negativa ")
    print(razon)