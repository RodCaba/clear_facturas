import os
from glob import glob
from f_rec import FacturaV2, Relacion
from datetime import date


PATH = os.path.abspath('')
files = glob(PATH + '/*.xml')


def main():
    rel = Relacion()
    for file in files:
        fact = FacturaV2(file)
        rel.a_folio.append(fact.get_folio())
        rel.a_fecha.append(fact.get_fecha_comprobante())
        rel.a_proveedor.append(fact.get_proveedor_name())
        rel.a_rfc.append(fact.get_rfc())
        rel.a_subtotal.append(fact.get_subtotal())
        rel.a_iva.append(fact.get_iva())
        try:
            rel.a_o_impuestos.append(int(fact.get_all_taxes() -fact.get_iva()))
        except:
            rel.a_o_impuestos.append(None)
        rel.a_total.append(fact.get_total())
        rel.a_concepto.append(fact.get_conceptos())
    df = rel.crear_df()
    df.to_excel("Facturas_recibidas_" + str(date.today())+ ".xlsx",sheet_name="Facturas_recibidas",
                columns=df.columns)


if __name__ == '__main__':
    main()
