import os
from glob import glob
from f_rec import FacturaV2, Relacion

file = 'C:/Users/rodse/PycharmProjects/facturas_emitidas/0DFEDB0A-E554-44AD-ADCF-A369EFCEBEAF.xml'
fact = FacturaV2(file)

fact.get_iva()
