
#######################################################################
##############   vida Laboral España   ################################
#######################################################################


import pymysql
import sys
import time
fecha= time.strftime("%x")
import os
import argparse
# print "Procesando vida laboral"
from os import listdir
n = 1
archivo_salida = open("./import/load" + str (n) + ".csv","w")
autorizado =""

count = 0
for ficheros in listdir ("./files/"):
    pagina = open("./files/" + ficheros, "r")

    #Inicializamos las variables

    valor = ""
    NAF = ""
    NIF = ""
    nombre = ""
    ALTA = "0000-00-00"
    GC = " "
    CONTRATO = " "
    ctp = " "
    flag = 0
    flagAlta = 0
    flagBaja1 = 0
    flagvac = 0
    flag2 = 0
    Vac = "0000-00-00"
    BAJA = "0000-00-00"
    CL = " "
    flagBaja3 = 0
    flagBaja2 = 0
    CCC = " "
    REGIMEN = ""
    Denominacion = " "
    CNAE = ""
    cnaetxt = " "
    TIPO = " "
    flag5 = ""

    #comenzamos con el bucle linea a linea despues de sacar el encabezado.
    for line in pagina:
        valor4 = (line[0:2])
        if valor4 =="A=":
            autorizado = (line[2:10])
            # print autorizado
        # print line
        valor = (line[10:14])
        # print valor
        #print valor
        valor1 = (line[1:14])
        #print valor1
        valor2 =(line[7:13])
        #print valor2
        valor3 = (line[11:59])
        #print valor3

        if valor2 =="Codigo":
            CCC = (line[33:45])
            REGIMEN = (line[58:62])

        if valor2 == "Denomi":
            Denominacion = (line[21:70])
            Denominacion = Denominacion.rstrip()
            Denominacion = Denominacion.replace(";","")

        if valor2 == "Activ.":
            CNAE = (line[15:19])
            #print CNAE
            cnaetxt = (line[21:42])
            #print cnaetxt
            A = len(line)
            #print A
            if A == 76:
                TIPO = " "
            elif A != 76:
                TIPO = (line[75:79])
                #print TIPO


        #PINTAMOS PRIMERA VEZ
        if  flagBaja2 == 1 and ( valor =="BAJA" or valor == "    " ):

            archivo_salida.write(str(autorizado + ";" + CCC  + ";" + NAF + ";" + NIF +  ";" + ALTA + ";" + BAJA + ";" + Vac + ";" + CONTRATO + ";" + ctp + ";" + GC + ";" + CL + ";" + nombre + ";" + CNAE + ";"+ cnaetxt + ";" + TIPO + ";" + Denominacion + ";" + REGIMEN  + ";" + fecha + ";" + ficheros  + "\n"))
            flagBaja2 = 0
            flagBaja1 = 0
            BAJA = "0000-00-00"
            Vac= "0000-00-00"
            count = count + 1
            #print "pint2"

        a = (line[1:2])
        b = (line [8:9])

        if (a == "0"or a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" ) and (b == "0" or b == "1" or b == "2" or b == "3" or b == "4" or b == "5" or b == "6" or b == "7" or b == "8" or b == "9" ):
            NAF = (line[1:14])

            #print NAF
            NIF = (line[18:28])

            #print NIF
            nombre = (line[28:76])
            nombre = nombre.rstrip()
            #print nombre

        if valor =="BAJA":
            ALTA = (line[21:25])+ "-" + (line[18:20]) + "-" + (line[15:17])
            BAJA = (line[54:58])+"-"+(line[51:53])+"-"+(line[48:50])
            GC = (line[59:61])
            CONTRATO = (line[64:67])
            ctp = (line[68:73])
            flagBaja1 = 1

        if valor =="ALTA":
            ALTA = (line[21:25])+ "-" + (line[18:20]) + "-" + (line[15:17])
            GC = (line[59:61])
            CONTRATO = (line[64:67])
            ctp = (line[68:73])
            BAJA="0000-00-00"
            Vac = "0000-00-00"

            flagAlta = 1

        if valor =="    " and flagAlta ==1:
            CL = (line[37:40])
            flag = 1

        if valor1 == "VAC.RETRIB.NO" and flagBaja1 == 0:
            ALTA = "0000-00-00"
            BAJA = "0000-00-00"
            Vac = "0000-00-00"
            flagvac = 1

        if valor == "    " and flagBaja1 ==1:
            CL = (line[37:40])
            flagBaja2 = 1

        if valor == "B.NO" and flagBaja2 ==1:
            Vac =(line[43:47]) + "-" + (line[40:42]) + "-" +  (line[37:39])
            flagBaja3 = 1

        if valor == "    " and flagvac == 1:
            flag = 1

        if valor3 == "NO EXISTEN TRABAJADORES EN EL PERIODO SOLICITADO":
            ALTA = "0000-00-00"
            BAJA = "0000-00-00"
            Vac = "0000-00-00"
            GC = "-----"
            ctp ="-----"
            CL = "-----"
            NAF = "-----"
            NIF = "-----"
            CONTRATO = "-----"
            nombre = "-----"
            flag5 = 1
            count = count + 1


        if flag == 1 and (flagAlta == 1 or flagvac == 1):

            archivo_salida.write(str(autorizado +";" + CCC  + ";" + NAF + ";" + NIF +  ";" + ALTA + ";" + BAJA + ";" + Vac + ";" + CONTRATO + ";" + ctp + ";" + GC + ";" + CL + ";" + nombre + ";" + CNAE + ";"+ cnaetxt + ";" + TIPO + ";" + Denominacion + ";" + REGIMEN + ";"+ fecha + ";"+ ficheros  +  "\n"))
            flag = 0
            flag1 = 0
            flagAlta = 0
            flagvac2 = 0
            flagvac = 0
            valor = ""
            CONTRATO = ""
            ctp = ""
            Vac = "0000-00-00"
            CL = ""
            BAJA = "0000-00-00"
            count = count + 1
            #print "pinto1 "

        if flagBaja3 == 1:

            archivo_salida.write(str(autorizado + ";" + CCC  + ";" + NAF + ";" + NIF +  ";" + ALTA + ";" + BAJA + ";" + Vac + ";" + CONTRATO + ";" + ctp + ";" + GC + ";" + CL + ";" + nombre + ";" + CNAE + ";"+ cnaetxt + ";" + TIPO + ";" + Denominacion + ";" + REGIMEN  + ";" + fecha + ";" + ficheros  +  "\n"))

            flag = 0
            flagAlta = 0
            flagvac = 0
            valor = ""
            flag2 = 0
            GC = ""
            CONTRATO = ""
            ctp = " "
            Vac = "0000-00-00"
            CL = " "
            flagBaja1 = ""
            flagBaja2 = ""
            flagBaja3 = ""
            BAJA = "0000-00-00"
            count = count + 1
            #print "pinto3"

        if flag5 == 1:
            archivo_salida.write(str(autorizado + ";" + CCC  + ";" + NAF + ";" + NIF +  ";" + ALTA + ";" + BAJA + ";" + Vac + ";" + CONTRATO + ";" + ctp + ";" + GC + ";" + CL + ";" + nombre + ";" + CNAE + ";"+ cnaetxt + ";" + TIPO + ";" + Denominacion + ";" + REGIMEN  + ";" + fecha + ";"+ ficheros  + "\n"))
            flag = 0
            flagAlta = 0
            flagvac = 0
            valor = ""
            flag2 = 0
            GC = " "
            CONTRATO = " "
            ctp = " "
            CL = " "
            flagBaja1 = ""
            flagBaja2 = ""
            flagBaja3 = ""
            BAJA = "0000-00-00"
            Vac="0000-00-00"
            flag5 = 0
            count = count + 1

        #print count

        #print count
        if count == 800000:
            # print "entro"
            n = n + 1
            archivo_salida.close()
            archivo_salida = open("./import/load" + str (n) + ".csv","w")
            count = 0

    #cerramos ficheros
    pagina.close()
archivo_salida.close()

print("Datos Procesado Correctamente")
