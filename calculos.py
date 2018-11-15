from lxml import etree
import time
fecha= time.strftime("%x")
import sys
import os
import argparse
from os import listdir
import shutil
fechaControl = " "
COD = " "
PECU = " "
codcolectivo= " "
ocupacion = " "
APLICADO = " "
ctp = " "
gc = " "
contrato = " "
cnae = " "
aplicado =""
fraccionCuota = ""
periodoPresentacion = " "
a = ""
archivo_salida = open("./imports/load.csv","w")
# archivo_salida.write(str("Autorizado" + ";" + "Regimen" + ";" + "Ccc" + ";" + "PeriodoDesde" + ";" + "PeriodoHasta" + ";" + "FechaControl" + ";" + "PeriodoPresentacion" + ";" + "Liquidacion" + ";" + "NumeroDeLiquidacion" + ";" + "Naf" + ";" + "Nif" + ";" + "Caf" + ";" + "FechaDesde" + ";" + "FechaHasta" + ";" + "DiasCotizados" + ";" + "GrupoCotizacion" + ";"+ "Contrato" + ";" + "Cnae" + ";" + "CoDigoPeculiaridad" + ";" + "Pecularidad" + ";" + "FraccionCuota" + ";" + "TipoAplicado" + ";" +  "CodigoColectivo" + ";" + "Ocupacion" + ";" + "CoeficienteTiempoParcial" + ";" + "Codigo"+ ";" + "Descripcion" + ";" + "CuotaBase" + ";" + "CuotaTrabajador" + ";" + "CuotaEmpresarial" + ";" + "CuotaTotal" + ";" + "Fecha" + ";"+ "Ficheros" + "\n"))
z = 1
count = 0
for ficheros in listdir("./files/"):
    doc = etree.parse("./files/" + ficheros)
    print ficheros
    tree = doc.getroot()
    tipodocu = tree[0].tag
    autorizado = tree[0].text
    # print tipodocu
    die = tipodocu.find("Respuesta")
    print die
    if die < 0:
        # longitud etiqueta c
        etiquetac = tree[2]
        nc = len(etiquetac)
        # regimen
        etiquetad = etiquetac[0]
        regimen = etiquetad[0].text
        # ccc
        cccProvincia = etiquetad[1].text
        cccAleatorio = etiquetad[2].text
        ccc = cccProvincia + " " + cccAleatorio
        # periodoDesde
        etiquetaf = etiquetac[1]
        mes = etiquetaf[0].text
        ano = etiquetaf[1].text
        periodoDesde = ano+mes

        # periodoHasta
        etiquetag = etiquetac[2]
        mes1 = etiquetag[0].text
        ano1 = etiquetag[1].text
        periodoHasta = ano1 + mes1
        # liquidacion
        etiquetah = etiquetac[3].text
        liquidacion = etiquetah
        if liquidacion=="L03":
            # fecha control
            etiquetaj = etiquetac[4]
            mesFechaControl = etiquetaj[0].text
            anoFechaControl = etiquetaj[1].text
            fechaControl = anoFechaControl + mesFechaControl
            etiquetaj = etiquetac[5]
            mesperiodoPresentacion = etiquetaj[0].text
            anoperiodoPresentacion = etiquetaj[1].text
            periodoPresentacion = anoperiodoPresentacion + mesperiodoPresentacion
            # periodoPresentacion
            a = etiquetac[6].text
            print a
        else:
        # periodoPresentacion
            etiquetaj = etiquetac[4]
            mesperiodoPresentacion = etiquetaj[0].text
            anoperiodoPresentacion = etiquetaj[1].text
            periodoPresentacion = anoperiodoPresentacion + mesperiodoPresentacion
            # periodoPresentacion
            a = etiquetac[5].text
            print a
        etiquetaq = etiquetac[nc-1]
        nq = len(etiquetaq)
        # print nq
        # recorro todos los trabajadores
        i = 0
        while i < nq:
            etiquetaag = etiquetaq[i]
            # naf3
            etiquetaah = etiquetaag[0].text
            naf = etiquetaah
            naf1 = naf[0:2]
            naf2 = naf[2:12]
            naf3 = naf1 + " " + naf2
            # nif
            etiquetaai = etiquetaag[1]
            etiquetaam = etiquetaai[1].text
            nif = etiquetaam
            # caf
            etiquetaaj = etiquetaag[2].text
            # caf = etiquetaaj
            caf = " "
            # longitud de la etiqueta ak. Nos da el numero de tramos por cada trabajador
            etiquetaak = etiquetaag[3]
            nak = len(etiquetaak)
            # print nak
            # recorro todos los tramos
            j = 0
            while j < nak:
                etiquetaan = etiquetaak[j]
                # fechaD
                etiquetaao = etiquetaan[0]
                dia2 = etiquetaao[0].text
                mes2 = etiquetaao[1].text
                ano2 = etiquetaao[2].text
                fechaD = dia2 + "/" + mes2 + "/" + ano2
                # fechaH
                etiquetaap = etiquetaan[1]
                dia3 = etiquetaap[0].text
                mes3 = etiquetaap[1].text
                ano3 = etiquetaap[2].text
                fechaH = dia3 + "/" + mes3 + "/" + ano3
                # diascoti
                diascoti = etiquetaan[2].text
                etiquetaas = etiquetaan[4]
                nas = len(etiquetaas)
                # print nas
                k = 0
                while k < nas:
                    etiquetaaa = etiquetaas[k]
                    naa = len(etiquetaaa)
                    # print naa
                    n = 0
                    while n < naa:
                        etiqueta1 = etiquetaaa[n].tag
                        etiqueta4 = etiqueta1[-3] + etiqueta1[-2] + etiqueta1[-1]
                        # print etiqueta4
                        if etiqueta4 == "igo":
                            # CODI
                            CODI = etiquetaaa[n].text
                            if CODI =="200":
                                DESCRIPCION = "COT.EMPR. CUOTA DE OTRAS COTIZACIONES"
                            elif CODI =="300":
                                DESCRIPCION = "PERCEPCIONES"
                            elif CODI =="500":
                                DESCRIPCION = "CONTINGENCIAS COMUNES"
                            elif CODI =="501":
                                DESCRIPCION = "HORAS EXTRAS FUERZA MAYOR"
                            elif CODI =="502":
                                DESCRIPCION = "OTRAS HORAS EXTRAS"
                            elif CODI =="503":
                                DESCRIPCION = "APORTACION SERVICIOS COMUNES"
                            elif CODI =="509":
                                DESCRIPCION = "CONTING.COM.COTIZ.EMPRESARIAL"
                            elif CODI =="524":
                                DESCRIPCION = "ASISTENCIA SANITARIA CONCERTADA"
                            elif CODI =="528":
                                DESCRIPCION = "O.I.COTIZACION ADICIONAL EX-MUNPAL"
                            elif CODI =="531":
                                DESCRIPCION = "INCREMENTO COTI.CONTRATO TEMP.MENOR 7 DIAS"
                            elif CODI =="535":
                                DESCRIPCION = "CONT. COM. MATERNIDAD T. PARCIAL"
                            elif CODI =="536":
                                DESCRIPCION = "CONT. COM. EXP. REG. EMPLEO T. PARCIAL"
                            elif CODI =="537":
                                DESCRIPCION = "HORAS COMPLEMENTARIAS"
                            elif CODI =="551":
                                DESCRIPCION = "DEDUCCION CONTINGENCIAS EXCLUIDAS"
                            elif CODI =="552":
                                DESCRIPCION = "DEDUCCION COLABORACION VOLUNTARIA"
                            elif CODI =="563":
                                DESCRIPCION = "COMPENSACION IT ENFERMEDAD COMUN"
                            elif CODI =="571":
                                DESCRIPCION = "REDUCCIONES A CARGO DE LA TGSS"
                            elif CODI =="580":
                                DESCRIPCION = "REDUCCION REGISTRO CANARIO"
                            elif CODI =="586":
                                DESCRIPCION = "REDUCCIONES SEA A CARGO TGSS"
                            elif CODI =="587":
                                DESCRIPCION = "COTIZACION ADICIONALCOEF. RED. EDAD JUBIL."
                            elif CODI =="588":
                                DESCRIPCION = "COT.ADIC.COEF.REDU.EDAD JUBIL.MATERN.TP"
                            elif CODI =="589":
                                DESCRIPCION = "COT.ADIC.COEF.REDU.EDAD JUBIL.REG.EMPLEO TP"
                            elif CODI =="594":
                                DESCRIPCION = "COTIZACION ESPECIAL SOLIDARIDAD"
                            elif CODI =="595":
                                DESCRIPCION = "COTI.ESPECIAL SOLIDARIDAD MATERNIDAD TP"
                            elif CODI =="596":
                                DESCRIPCION = "COTIZACION ESPECIAL SOLIDARIDAD ERE TP"
                            elif CODI =="598":
                                DESCRIPCION = "LIQUIDO CONTINGENCIAS COMUNES"
                            elif CODI =="601":
                                DESCRIPCION = "IT DE ACCIDENTES DE TRABAJO"
                            elif CODI =="603":
                                DESCRIPCION = "CUOTA IT DE AT Y EP DE SITUACIONES ESPEC"
                            elif CODI =="611":
                                DESCRIPCION = "IMS DE ACCIDENTES DE TRABAJO"
                            elif CODI =="613":
                                DESCRIPCION = "CUOTA IMS DE AT Y EP DE SITUACIONES ESPE"
                            elif CODI =="634":
                                DESCRIPCION = "IMS DE AT MATERNIDAD PARCIAL"
                            elif CODI =="635":
                                DESCRIPCION = "IT DE AT MATERNIDAD PARCIAL"
                            elif CODI =="636":
                                DESCRIPCION = "IT DE AT REGULACION DE EMPLEO PARCIAL"
                            elif CODI =="637":
                                DESCRIPCION = "IMS DE AT REGULACION DE EMPLEO PARCIAL"
                            elif CODI =="663":
                                DESCRIPCION = "COMP.IT POR ACCIDENTE DE TRABAJO"
                            elif CODI =="698":
                                DESCRIPCION = "LIQUIDO DE ACCIDENTES DE TRABAJO"
                            elif CODI =="700":
                                DESCRIPCION = "OTRAS COTIZACIONES"
                            elif CODI =="701":
                                DESCRIPCION = "CUOTAS POR DESEMPLEO"
                            elif CODI =="702":
                                DESCRIPCION = "CUOTAS POR FOGASA"
                            elif CODI =="703":
                                DESCRIPCION = "CUOTAS POR FORMACION PROFESIONAL"
                            elif CODI =="705":
                                DESCRIPCION = "CUOTA DESEMPLEO COTIZACION EMPRESARIAL"
                            elif CODI =="706":
                                DESCRIPCION = "CUOTA FOGASA COTIZACION EMPRESARIAL"
                            elif CODI =="707":
                                DESCRIPCION = "CUOTA FORMACION PROFESIONAL COTIZ.EMPRES"
                            elif CODI =="708":
                                DESCRIPCION = "DESEMPLEO MATERNIDAD TIEMPO PARCIAL"
                            elif CODI =="709":
                                DESCRIPCION = "FOGASA MATERNIDAD TIEMPO PARCIAL"
                            elif CODI =="710":
                                DESCRIPCION = "FORM. PROFES. MATERNIDAD TIEMPO PARCIAL"
                            elif CODI =="711":
                                DESCRIPCION = "DESEMPLEO ERE TIEMPO PARCIAL"
                            elif CODI =="712":
                                DESCRIPCION = "FOGASA ERE TIEMPO PARCIAL"
                            elif CODI =="713":
                                DESCRIPCION = "FORM. PROFES. ERE TIEMPO PARCIAL"
                            elif CODI =="735":
                                DESCRIPCION = "FORMACION TEORICA PRESENCIAL"
                            elif CODI =="736":
                                DESCRIPCION = "FORMACION TEORICA A DISTANCIA"
                            elif CODI =="737":
                                DESCRIPCION = "BONIFICACION TUTORIA"
                            elif CODI =="760":
                                DESCRIPCION = "BONIF.Y SUBVENC.CON CARGO AL INEM"
                            elif CODI =="763":
                                DESCRIPCION = "BONIFICACION FORMACION CONTINUA"
                            elif CODI =="764":
                                DESCRIPCION = "BONIFIC. INVESTIG. DESARR. INNOVA. TECN."
                            elif CODI =="765":
                                DESCRIPCION = "REDUCCIONES SEA EN IT A CARGO DEL SPEE"
                            elif CODI =="766":
                                DESCRIPCION = "BONIFICACION GARANTIA JUVENIL"
                            elif CODI =="767":
                                DESCRIPCION = "BONIFICACION GARANTIA JUVENIL,EXCEDENTE TRABAJADOR"
                            elif CODI =="798":
                                DESCRIPCION = "LIQUIDO DE OTRAS COTIZACIONES"
                            elif CODI =="800":
                                DESCRIPCION = "RECARGO DE MORA"
                            elif CODI =="998":
                                DESCRIPCION = "LIQUIDO DE TOTALES"
                        elif etiqueta4 == "ase":
                            cuotaBase = etiquetaaa[n].text
                            cuotaBase = str (int (cuotaBase)/ float(100))
                            cuotaBase = cuotaBase.replace(".",",")
                        elif etiqueta4 == "dor":
                            cuotaTrabajador = etiquetaaa[n].text
                            cuotaTrabajador = str (int (cuotaTrabajador)/ float(100))
                            cuotaTrabajador = cuotaTrabajador.replace(".",",")
                        elif etiqueta4 == "ial":
                            cuotaEmpresarial = etiquetaaa[n].text
                            cuotaEmpresarial = str (int (cuotaEmpresarial)/ float(100))
                            cuotaEmpresarial = cuotaEmpresarial.replace(".",",")
                        elif etiqueta4 == "tal":
                            cuotaTotal = etiquetaaa[n].text
                            cuotaTotal = str (int (cuotaTotal)/ float(100))
                            cuotaTotal = cuotaTotal.replace(".",",")
                        # if n == (naa - 1) and cuotaEmpresarial !="0.0" and cuotaBase != "0.0":
                        #     APLICADO = float (cuotaEmpresarial)  / float(cuotaBase)
                        #     APLICADO = round(float (APLICADO)*float (100),1)
                        #     APLICADO = str(APLICADO) + "%"
                        n += 1
                    etiquetaar = etiquetaan[3]
                    nar = len(etiquetaar)
                    # print nar
                    l = 0
                    while l < nar:
                        # print l
                        # print nar
                        etiqueta = etiquetaar[l].tag
                        etiquetaar1 = etiqueta[-6] + etiqueta[-5] + etiqueta[-4] + etiqueta[-3] + etiqueta[-2] + etiqueta[-1]
                        etiquetaar2 = etiqueta[-2] + etiqueta[-1]
                        # print etiquetaar2
                        diego = etiquetaar[nar-1].tag
                        diego1 = diego[-2] + diego[-1]
                        # print etiquetaar1
                        if etiquetaar1 == "zacion":
                            gc = etiquetaar[l].text
                            # print gc
                        elif etiquetaar1 =="ntrato":
                            contrato = etiquetaar[l].text
                            # print contrato
                        elif etiquetaar1 == "arcial":
                            ctp = etiquetaar[l].text
                            ctp = "0"+","+ ctp
                            # print ctp
                        elif etiquetaar2 == "AE":
                            cnae = etiquetaar[l].text
                            # print cnae
                        elif etiquetaar1 == "pacion":
                            ocupacion = etiquetaar[l].text
                        if diego1 == "es":
                            # print "existe bd"
                            etiquetabd = etiquetaar[l]
                            nbd = len(etiquetabd)
                            # print nbd
                            m = 0
                            while m < nbd:
                                etiquetabg = etiquetabd[m]
                                # etiquetabg = etiquetabd[0]
                                # COD
                                COD = etiquetabg[0].text
                                if COD =="01":
                                    PECU ="01-Bonificacion Inem"
                                elif COD =="02":
                                    PECU = "02-Bonificacion Hacienda embarcaciones Zona Especial de Canarias"
                                elif COD == "04":
                                    PECU = "04-Incremento de tipos"
                                elif COD == "05":
                                    PECU = "05-Incremento de cuota"
                                elif COD == "06":
                                    PECU = "06-Decremento de tipos"
                                elif COD == "07":
                                    PECU = "07-Exoneracion"
                                elif COD == "08":
                                    PECU = "08-Colaboracion"
                                elif COD == "09":
                                    PECU = "09-Exclusiones"
                                elif COD == "10":
                                    PECU = "10-Decremento de cuota"
                                elif COD == "11":
                                    PECU = "11-Cotizacion adicional"
                                elif COD == "12":
                                    PECU = "12-Reduccion a cargo del INEM"
                                elif COD == "13":
                                    PECU = "13-Bonificacion SPEE Prog Fomento de Empleo-Porcentaje"
                                elif COD == "14":
                                    PECU = "14-Diferimiento en el ingreso de cuotas"
                                elif COD == "15":
                                    PECU = "15-Exoneracion E.R.E Fuerza mayor. Tiempo parcial "
                                elif COD == "16":
                                    PECU = "16-Bonificacion SPEE Prog Fomento de Empleo-Cuantia"
                                elif COD == "17":
                                    PECU = "17-Aportacion no obligatoria -Suspension Regulacion Empleo"
                                elif COD == "18":
                                    PECU = "18-Aportacion no obligatoria- Suspension Regulacion Empleo Parcial "
                                elif COD == "19":
                                    PECU = "19-Bonificacion SPEE con cargo a Hacienda"
                                elif COD == "20":
                                    PECU = "20-Periodo sin retribucion"
                                elif COD == "21":
                                    PECU = "21-IT.CC Pago Delegado"
                                elif COD == "22":
                                    PECU = "22-IT.CC Pago directo"
                                elif COD == "23":
                                    PECU = "23-IT.AT Pago delegado "
                                elif COD == "24":
                                    PECU = "24-IT.AT Pago Directo"
                                elif COD == "25":
                                    PECU = "25-IT.CC Pago delegado diferido "
                                elif COD == "26":
                                    PECU = "26-IT.CC Pago delegado diferido mes anterior"
                                elif COD == "27":
                                    PECU = "27-IT.AT Pago delegado diferido "
                                elif COD == "28":
                                    PECU = "28-IT.AT Pago delegado diferido mes anterior"
                                elif COD == "29":
                                    PECU = "29-IT.CC Colaboradoras excluidas 15 dias"
                                elif COD == "30":
                                    PECU = "30-IT.AT Colaboradoras excluidas"
                                elif COD == "31":
                                    PECU = "31-Maternidad/paternidad tiempo completo "
                                elif COD == "32":
                                    PECU = "32-Maternidad tiempo parcial"
                                elif COD == "33":
                                    PECU = "33-Paternidad tiempo parcial "
                                elif COD == "34":
                                    PECU = "34-Riesgo embarazo/lactancia"
                                elif COD == "35":
                                    PECU = "35-Funcionarios-permiso sin sueldo "
                                elif COD == "36":
                                    PECU = "36-Funcionarios-suspension provisional"
                                elif COD == "37":
                                    PECU = "37-Exoneracion E.R.E Fuerza mayor. Tiempo completo"
                                elif COD == "38":
                                    PECU = "38-Moratoria"
                                elif COD == "39":
                                    PECU = "39-Decremento BBCC"
                                elif COD == "40":
                                    PECU = "40-Tipo cotizacion especial SEA"
                                elif COD == "41":
                                    PECU = "41-Bonificacion Programa Fomento de Empleo. Cuantia diaria"
                                elif COD == "42":
                                    PECU = "42-Red. Cuota-SS cuantia"
                                elif COD == "43":
                                    PECU = "43-Tarifa plana"
                                elif COD == "44":
                                    PECU = "44-Cotizacion especial solidaridad"
                                elif COD == "45":
                                    PECU = "45-Pluriempoleo con exclusiones diferentes"
                                elif COD == "46":
                                    PECU = "46-Bonificacion Sistema Nacional Garantia Juvenil"
                                elif COD == "47":
                                    PECU = "47-Reduccion-Cuantia-Sin horas complementarias"
                                elif COD == "48":
                                    PECU = "48-Bonificacion-cuantia-Sin horas complementarias"
                                fraccionCuota = etiquetabg[1].text
                                codcolectivo = etiquetabg[2].text
                                aplicado = etiquetabg[3].text
                                archivo_salida.write(str(autorizado + ";" + regimen + ";" + ccc + ";" + periodoDesde + ";" + periodoHasta + ";" + fechaControl + ";" + periodoPresentacion + ";" + liquidacion + ";" + a + ";" + naf3 + ";" + nif + ";" + caf + ";" + fechaD + ";" + fechaH + ";" + diascoti + ";" + gc + ";"+ contrato + ";" + cnae + ";" + COD + ";"  + PECU + ";" + fraccionCuota +";"+ aplicado + ";" + codcolectivo + ";" + ocupacion + ";" + ctp + ";" + CODI + ";" + DESCRIPCION + ";" + cuotaBase + ";" + cuotaTrabajador + ";" + cuotaEmpresarial + ";" + cuotaTotal + ";" + fecha + ";" + ficheros + "\n"))
                                count = count + 1
                                if count == 1000000:
                                    z = z + 1
                                    archivo_salida.close()
                                    archivo_salida = open("./imports/load" + str (z) + ".csv","w")
                                    count = 0
                                COD = " "
                                PECU = " "
                                codcolectivo = " "
                                APLICADO = " "
                                m += 1
                        elif l == nar-1 and diego1 != "es":
                            archivo_salida.write(str(autorizado + ";" + regimen + ";" + ccc + ";" + periodoDesde + ";" + periodoHasta + ";" + fechaControl + ";" + periodoPresentacion + ";" + liquidacion + ";" + a + ";" + naf3 + ";" + nif + ";" + caf + ";" + fechaD + ";" + fechaH + ";" + diascoti + ";" + gc + ";"+ contrato + ";" + cnae + ";" + COD + ";" + PECU + ";" + fraccionCuota + ";" + aplicado + ";" +  codcolectivo + ";" + ocupacion + ";" + ctp + ";" + CODI + ";" + DESCRIPCION + ";" + cuotaBase + ";" + cuotaTrabajador + ";" + cuotaEmpresarial + ";" + cuotaTotal + ";" + fecha + ";"+ ficheros + "\n"))
                            count = count + 1
                            gc = " "
                            contrato = " "
                            cnae = " "
                            ctp = " "
                            ocupacion = " "
                            if count == 1000000:
                                z = z + 1
                                archivo_salida.close()
                                archivo_salida = open("./imports/load" + str (z) + ".csv","w")
                                count = 0
                        l += 1
                    cuotaBase = " "
                    cuotaTrabajador = " "
                    cuotaEmpresarial = " "
                    cuotaTotal = " "
                    CODI = " "
                    DESCRIPCION = " "
                    k += 1
                fechaD = " "
                fechaH = " "
                diascoti = " "
                j += 1
            fechaControl = " "
            COD = " "
            PECU = " "
            codcolectivo = " "
            APLICADO = " "
            gc = " "
            contrato = " "
            cnae = " "
            ctp = " "
            ocupacion = " "
            cuotaBase = " "
            cuotaTrabajador = " "
            cuotaEmpresarial = " "
            cuotaTotal = " "
            CODI = " "
            DESCRIPCION = " "
            naf3 = " "
            nif = " "
            caf = " "
            fechaD = " "
            fechaH = " "
            diascoti = " "
            i += 1
archivo_salida.close()
