import pymysql
import time
from datetime import date, timedelta
from datetime import datetime
import calendar
import datetime
import math
import sys
import os
from os import listdir

#rescatamos las Variables
basedatos = ["EUROFIRMS E.T.T.,S.L."]
bbdd_visitada =[]
documento = "vl"
#inicializamos variables
lineasfinal = ""
row = ""
fila=""
periodo_desde_anho=""
b = ""
bisiesto = ""
m = ""
parar=""
lista=[]
n=0
count= 0
lineasf=""
filask=""
filasss=""
numero_idcccc =""
lineasidcccc = 0
count3 = 0
count2 =0
lineassituacion = 0
count4 = 0
lineasvl = 0
lineasf = 0
z = 0
pag = 0
inicio = 0
final = 5
a = 0 
for a in range(len(basedatos)):
    ddbb = basedatos[a]
    if documento=="vl":
        anho_inicio = time.strftime("%Y")
        mes = time.strftime("%m")
        if mes =="12":
            mes_inicio = "05"
        if mes == "11":
            mes_inicio = "04"
        if mes == "10":
            mes_inicio = "03"
        if mes == "09":
            mes_inicio = "02"
        if mes  =="08":
            mes_inicio = "01"
        if mes == "07":
            mes_inicio = "12"
            anho_inicio = str(int(anho)-1)
        if mes =="06":
            mes_inicio = "11"
            anho_inicio = str(int(anho)-1)
        if mes =="05":
            mes_inicio = "10"
            anho_inicio = str(int(anho)-1)
        if mes =="04":
            mes_inicio = "09"
            anho_inicio = str(int(anho)-1)
        if mes =="03":
            mes_inicio = "08"
            anho_inicio = str(int(anho)-1)
        if mes =="02":
            mes_inicio = "07"
            anho_inicio = str(int(anho)-1)
        if mes =="01":
            mes_inicio = "06"
            anho_inicio = str(int(anho)-1)

        hoy = time.strftime("%d-%m-%Y")
        fecha_inicio = time.strftime("%d") + "-" + mes_inicio + "-" + anho_inicio
        connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = appsigspain)
        cursor = connection.cursor()
        cursor.execute( "SELECT Codigo from empresas where NombreEmpresa like ='" + basedatos + "'")
        for fila in filas:
            Codigo = fila[0]
        print (Codigo)



#     f = open('c:\\\\xampp\\\\htdocs\\\\sig\\\\Winsuite\\\\afi.afi','w')
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection.cursor()
#     cursor.execute( "SELECT fechaImportacion from peticiones_vl_pendientes order by fechaImportacion DESC limit 0,1")
#     filas =cursor.fetchall()
#     for fila in filas:
#         fechaI = fila[0]
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = 'app_sig')
#     cursor = connection.cursor()
#     a =  "(SELECT * FROM empresas where nombre like '"+ basedatos +"')"
#     # print a
#     cursor.execute(a)
#     rows =cursor.fetchall()
#     for row in rows:
#         autorizacion = row[3]
#         id_winsuite = "99R99999"
#     nombre = time.strftime("%d%H%M%S")
#     connection3 = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection3.cursor()
#     cursor.execute( "SELECT DISTINCT ccc ,periodo_desde,periodo_hasta FROM peticiones_vl_pendientes where fechaImportacion = "+"'" + str(fechaI) +"'")
#     f.write('ETIAFI80WS820'+ autorizacion + id_winsuite + "201504221839" + nombre + "AFIN 00000000000000A "+"\n")
#     filass =cursor.fetchall()
#     for fil in filass:
#         ccc = fil[0];
#         periodo_desde = fil[1];
#         periodo_hasta = fil[2];
#         mes_desde= periodo_desde.strftime("%m")
#         anho_desde= periodo_desde.strftime("%Y")
#         dia_desde=periodo_desde.strftime("%d")
#         periodo_desde = str(anho_desde)+str(mes_desde)+str(dia_desde)

#         mes_hasta= periodo_hasta.strftime("%m")
#         anho_hasta= periodo_hasta.strftime("%Y")
#         dia_hasta=periodo_hasta.strftime("%d")
#         periodo_hasta = str(anho_hasta)+str(mes_hasta)+str(dia_hasta)
#         # print f.closed
#         f.write('EMP'+ ccc + "                    " + "000000000000000" + "             " + "CL  " + "\n")
#         count = count + 1
#         lineasf = 3*count +2
#         f.write("RZS02"+"                                                       "+"00000000  " +"\n")
#         f.write("FCE" + periodo_desde + periodo_hasta + "0000000000000000                                   " + "\n")

#     if count  == 1 or count == 2 or count == 3 or count == 4 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
#         countfinal = "0000"+ str(count)
#         # print countfinal
#     else:
#         countfinal ="000"+ str(count)
#         print countfinal
#     # print lineasf
#     for k  in range (0,9):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "0000000"+str(lineasf)

#     for k  in range (10,99):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "000000"+str(lineasf)

#     for k in range (100,999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "00000"+str(lineasf)
#     for k in range (1000,9999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "0000"+str(lineasf)
#     for k in range (10000,99999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "000"+str(lineasf)

#     f.write('ETFAFI80WS820'+ autorizacion + id_winsuite + "201504221840" + nombre + "AFIN " + countfinal+ lineasfinal +"   "+"\n")
#     f.close()









# if documento=="idcccc":
#     f = open('c:\\\\xampp\\\\htdocs\\\\sig\\\\Winsuite\\\\afi.afi','w')
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection.cursor()
#     cursor.execute( "SELECT fechaImportacion from peticiones_idcccc_pendientes order by fechaImportacion DESC limit 0,1")
#     filas =cursor.fetchall()
#     for fila in filas:
#         fechaI = fila[0]
#         print fechaI
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = 'app_sig')
#     cursor = connection.cursor()
#     a =  "(SELECT * FROM empresas where nombre like '"+ basedatos +"')"
#     # print a
#     cursor.execute(a)
#     rows =cursor.fetchall()
#     for row in rows:
#         autorizacion = row[3]
#         id_winsuite = "99R99999"
#     nombre = time.strftime("%d%H%M%S")
#     connection3 = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection3.cursor()
#     cursor.execute( "SELECT DISTINCT ccc ,periodo_desde,periodo_hasta FROM peticiones_idcccc_pendientes where fechaImportacion = "+"'" + str(fechaI) +"' and Revision = '2'")
#     f.write('ETIAFI80WS820'+ autorizacion + id_winsuite + "201504221839" + nombre + "AFIN 00000000000000A "+"\n")
#     filass =cursor.fetchall()
#     for fil in filass:
#         ccc = fil[0];
#         periodo_desde = fil[1];
#         periodo_hasta = fil[2];
#         mes_hasta= periodo_hasta.strftime("%m")
#         anho_hasta= periodo_hasta.strftime("%Y")
#         dia_hasta=periodo_hasta.strftime("%d")
#         periodo_hasta = str(anho_hasta)+str(mes_hasta)

#         mes_desde = (periodo_desde[5:7])
#         anho_desde = (periodo_desde[0:4])
#         anho_desde = int(anho_desde)
#         # print anho_desde
#         b = int (mes_desde)+ 1
#         # print periodo_hasta
#         while parar <= periodo_hasta:

#             if b == 1:
#                 b ="01"
#                 m = "31"
#             # print anho_desde
#             if b == 2:
#                 if (anho_desde == 2000 or anho_desde == 2004 or anho_desde == 2008 or anho_desde == 2012 or anho_desde == 2016 or anho_desde == 2020 or anho_desde == 2024 or anho_desde == 2028 or anho_desde == 2032 or anho_desde == 2036 or anho_desde == 2040 or anho_desde == 2044 or anho_desde == 2048 or anho_desde == 2052 or anho_desde == 2056) :
#                     # print "anho bisiesto"
#                     b = "02"
#                     m ="29"
#                 else :
#                     # print "anho normal"
#                     b = "02"
#                     m ="28"
#             if b == 3:
#                 b = "03"
#                 m = "31"
#             if b ==4:
#                 b = "04"
#                 m = "30"
#             if b == 5:
#                 b = "05"
#                 m = "31"
#             if b == 6:
#                 b = "06"
#                 m = "30"
#             if b == 7:
#                 b ="07"
#                 m = "31"
#             if b == 8 :
#                 b = "08"
#                 m = "31"
#             if b == 9 :
#                 b = "09"
#                 m = "30"
#             if b == 10:
#                 b = "10"
#                 m = "31"
#             if b ==11:
#                 b = "11"
#                 m = "30"
#                 # print "entro en el 11"
#             if b ==12:
#                 b = "12"
#                 # print "entro"
#                 m = "31"
#             if b==13:
#                 b ="01"
#                 m ="31"
#                 anho_desde = anho_desde + 1
#             # print b
#             f.write('EMP'+ ccc + "                    " + "000000000000000" + "             " + "PLC "  +"\n")
#             count = count + 1
#             lineasf = 3*count +2
#             f.write("RZS02"+"                                                       "+"00000000  " +"\n")
#             f.write ("FCE"+ str(anho_desde)+ str(b) + str("01") + str(anho_desde) + str(b) +str(m) +"00000000000000000" +"                                  "+ "\n")

#             # print parar
#             b = int (b) + 1
#             parar = str(anho_desde)  + "0" +str(b)
#             if b ==10:
#                 parar = str(anho_desde)  +str(b)
#             if b ==11:
#                 parar = str(anho_desde)  +str(b)
#             if b ==12:
#                 parar = str(anho_desde)  +str(b)

#         parar = ""
#     if count  == 1 or count == 2 or count == 3 or count == 4 or count == 5 or count == 6 or count == 7 or count == 8 or count == 9:
#         countfinal = "0000"+ str(count)
#         print countfinal
#     else:
#         countfinal ="000"+ str(count)
#         print countfinal
#     print lineasf
#     for k  in range (0,9):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "0000000"+str(lineasf)

#     for k  in range (0,99):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "000000"+str(lineasf)

#     for k in range (100,999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "00000"+str(lineasf)
#     for k in range (1000,9999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "0000"+str(lineasf)
#     for k in range (10000,99999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "000"+str(lineasf)

#     f.write('ETFAFI80WS820'+ autorizacion + id_winsuite + "201504221840" + nombre + "AFIN " + countfinal+ lineasfinal +"   "+"\n")


# if documento =="situacion":
#     f = open('c:\\\\xampp\\\\htdocs\\\\sig\\\\Winsuite\\\\afi.afi','w')
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection.cursor()
#     cursor.execute( "SELECT fechaImportacion from peticiones_situacion_pendientes order by fechaImportacion DESC limit 0,1")
#     filas =cursor.fetchall()
#     for fila in filas:
#         fechaI = fila[0]
#     connection = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = 'app_sig')
#     cursor = connection.cursor()
#     a =  "(SELECT * FROM empresas where nombre like '"+ basedatos +"')"
#     # print a
#     cursor.execute(a)
#     rows =cursor.fetchall()
#     for row in rows:
#         autorizacion = row[3]
#         id_winsuite = "99R99999"
#     nombre = time.strftime("%d%H%M%S")
#     cursor.close()
#     connection.close()
#     # conexion para sacar las lineas de la columnas de la tabla AFI
#     connection2 = pymysql.connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
#     cursor = connection2.cursor()
#     cursor.execute( "SELECT DISTINCT ccc FROM peticiones_isituacion_pendientes where fechaImportacion = "+"'" + str(fechaI) +"'")
#     f.write('ETIAFI80WS820'+ autorizacion + id_winsuite + "201504221839" + nombre + "AFIN 00000000000000A "+"\n")
#     filas =cursor.fetchall()
#     for fila in filas:
#         ccc = fila[0]
#         f.write('EMP'+ ccc + "                    " + "000000000000000"+ "             "+"CS  "+"\n")
#         count = count +1
#         lineasf = 2*count +2
#         f.write("RZS02"+"                                                       "+"00000000  " +"\n")
#         # #ultima linea del codigo
#         # # print count
#     if count  == 1 or count == 2 or count ==3 or count ==4 or count ==5 or count ==6 or count ==7 or count ==8 or count ==9:
#         countfinal = "0000"+ str(count)
#         # print countfinal
#     else:
#         countfinal ="000"+ str(count)
#         # print countfinal
#     # print lineasf
#     for k  in range (0,9):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "0000000"+str(lineasf)
#     for k  in range (0,99):
#         k = k+1
#         if k ==lineasf:
#             lineasfinal = "000000"+str(lineasf)

#     for k in range (100,999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "00000"+str(lineasf)
#     for k in range (1000,9999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "0000"+str(lineasf)
#     for k in range (10000,99999):
#         k = k + 1
#         if k ==lineasf:
#             lineasfinal = "000"+str(lineasf)
#     # print countfinal
#     # print lineasfinal
#     f.write('ETFAFI80WS820'+ autorizacion + id_winsuite + "201504221840" + nombre + "AFIN " + countfinal + lineasfinal + "   " + "\n")
