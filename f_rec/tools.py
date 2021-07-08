import os
import xml.dom.minidom
from glob import glob
import xml.etree.ElementTree as ET
import pandas as pd


class Factura:

    def __init__(self, file_name):
        self.doc = xml.dom.minidom.parse(file_name)

    def get_fecha_comprobante(self):
        cfdi_emisor = self.doc.getElementsByTagName("cfdi:Comprobante")
        return cfdi_emisor[0].getAttribute("Fecha")

    def get_proveedor_name(self):
        cfdi_emisor = self.doc.getElementsByTagName("cfdi:Emisor")
        return cfdi_emisor[0].getAttribute("Nombre")

    def get_subtotal(self):
        cfdi_emisor = self.doc.getElementsByTagName("cfdi:Comprobante")
        return cfdi_emisor[0].getAttribute("SubTotal")

    def get_iva(self):
        traslados = self.doc.getElementsByTagName("cfdi:Traslado")
        iva = [i for i in traslados if i.getAttribute("Impuesto") == "002"]
        iva_nr = {float(i.getAttribute("Importe")) for i in iva}
        iva_num = 0
        for i in iva_nr:
            iva_num += i
        return iva_num


class FacturaV2:

    def __init__(self, file_name):
        self.doc = ET.parse(file_name)

    def get_fecha_comprobante(self):
        root = self.doc.getroot()
        return root.attrib.get("Fecha")

    def get_proveedor_name(self):
        root = self.doc.getroot()
        emisor_tag = [children for children in root if "Emisor" in children.tag]
        emisor = emisor_tag[0]
        return emisor.attrib.get("Nombre")

    def get_subtotal(self):
        root = self.doc.getroot()
        return float(root.attrib.get("SubTotal"))

    def get_total(self):
        root = self.doc.getroot()
        return float(root.attrib.get("Total"))

    def get_all_taxes(self):
        root = self.doc.getroot()
        impuestos_tag = [children for children in root if "Impuestos" in children.tag]
        impuestos = impuestos_tag[0]
        return float(impuestos.attrib.get("TotalImpuestosTrasladados"))

    def get_conceptos(self):
        root = self.doc.getroot()
        conceptos_tag = [children for children in root if "Conceptos" in children.tag]
        conceptos = conceptos_tag[0]
        concepto_str = ""
        for i in conceptos:
            concepto_str += i.attrib.get("Descripcion") + "/ "
        return concepto_str

    def get_iva(self):
        root = self.doc.getroot()
        impuestos_tag = [children for children in root if "Impuestos" in children.tag]
        impuestos = impuestos_tag[0]
        traslados_tag = [children for children in impuestos]
        traslados = traslados_tag[0]
        traslado_n_tag = [children for children in traslados]
        ivas = [children for children in traslado_n_tag if children.attrib.get("Impuesto") == "002"]
        num = 0
        for children in ivas:
            n = float(children.attrib.get("Importe"))
            num += n
        return num


class Relacion:

    def __init__(self):
        self.a_fecha = []
        self.a_proveedor = []
        self.a_subtotal = []
        self.a_iva = []
        self.a_o_impuestos = []
        self.a_total = []
        self.a_concepto = []

    def crear_df(self):
        data = {
            'Fecha': self.a_fecha,
            'Proveedor': self.a_proveedor,
            'Subtotal': self.a_subtotal,
            'IVA': self.a_iva,
            'Otros Impuestos': self.a_o_impuestos,
            'Total': self.a_total,
            'Concepto': self.a_concepto
        }
        df = pd.DataFrame(data=data, columns=[*data.keys()])
        return df
