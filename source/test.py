import os
from glob import glob
from f_rec import FacturaV2, Relacion

PATH = os.path.abspath('')
files = glob(PATH + '/*.xml')

for file in files:
    fact = FacturaV2(file)
    print("Inicio de file: " + file)
    try:
        print(fact.get_fecha_comprobante())
    except:
        print("Error en file: " +file + " en fecha comprobante")
    try:
        print(fact.get_proveedor_name())
    except:
        print("Error en file: " +file + " en nombre proveedor")
    try:
        print(fact.get_subtotal())
    except:
        print("Error en file: " +file + " en subtotal")
    try:
        print(fact.get_iva())
    except:
        print("Error en file: " +file + " en iva")
    try:
        print(fact.get_all_taxes())
    except:
        print("Error en file: " +file + " en otros impuestos")
    try:
        print(fact.get_total())
    except:
        print("Error en file: " +file + " en total")
    try:
        print(fact.get_conceptos())
    except:
        print("Error en file: " +file + " en conceptos")

    print("Fin de file: " + file)

