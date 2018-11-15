
###########################################################################################
###########                                                                     ###########
###########             Fichero Audirtoria España                               ###########
###########             Creado por : Juan Flores (Fiabilis)                     ###########
###########################################################################################

#Hacemos un import con las librerias que vamos a utilizar
import openpyxl
import pymysql
from datetime import datetime  #libreria para poder operar con el tiempo
from datetime import datetime, date, time, timedelta
import time

#### Definimos las variables a utilizar en el programa #######
IDsGrupo = []
Codigos = []
lista_hoja1 =[]
############ vamos a coger el grupo de empresas y  meterlas en un array para meternas en el bucle ##########
connection = pymysql.connect(host='localhost',port=3306,user='root',db= 'appsigspain')
cursor = connection.cursor()
cursor.execute("SELECT IDGrupo from empresas where Subvencion = '1'")
filas =cursor.fetchall()
for fila in filas:
    IDGrupo = fila[0]
    IDsGrupo.append(IDGrupo)
connection.close()


##una vez creado el bucle lo metemos para que coja todas aquellas empresas que si tienen subvenciones.
for inicio in range (0,len(IDsGrupo)):
    IDsGrupo[inicio] = IDGrupo
    # SELECT empresas.Codigo  from empresas INNER JOIN  autorizados ON  empresas.IDGrupo = autorizados.IDGrupo  WHERE empresas.IDGrupo ='A0366'
 
    #######conexion a la base de datos para saber el grupo al que quieres hacer la subvencion  #########
    connection = pymysql.connect(host='localhost',port=3306,user='root',db= 'appsigspain')
    cursor = connection.cursor()
    cursor.execute("SELECT empresas.Codigo  from empresas INNER JOIN  autorizados ON  empresas.IDGrupo = autorizados.IDGrupo  WHERE empresas.IDGrupo ='"+ IDGrupo +"'" )
    filas =cursor.fetchall()
    for fila in filas:
        Codigo= fila[0]
        if Codigo != "":
            Codigos.append(Codigo)

    for i in range(0,len(Codigos)):
        connection = pymysql.connect(host='localhost',port=3306,user='root',db= Codigos[i])
        cursor = connection.cursor()
        cursor.execute( "SELECT * from vl where SUBDATE(CURDATE(), 30) < FechaAlta order by NAF, FechaAlta desc")
        filas =cursor.fetchall()
        for fila in filas:
            CCC = fila[2]
            NAF = fila[3]
            NIF =fila[4]
            FechaAlta = fila[5]
            FechaBaja = fila[6]
            FinVacac  = fila[7]
            Contrato = fila[8]
            Ctp = fila[9]
            GC = fila[10]
            CL  = fila[11]
            NOMBRE= fila[12]
            Cnae  = fila[13]
            CnaeTxt = fila[14]
            Tipo = fila[15]
            RazonSocial = fila[16]
            Regimen  = fila[17]
            Autorizacion  = fila[1]
            lista_hoja1.append([CCC,NAF,NIF,FechaAlta,FechaBaja,FinVacac,Contrato,Ctp,GC,CL,NOMBRE,Cnae,CnaeTxt,Tipo,RazonSocial,Regimen,Autorizacion])
    connection.close()
    print(lista_hoja1)
    # #definimos las varibles con las que vamos a trabajar asi como la ruta de la misma el fichero es la variable de la base de datos
    # ## una vez descargada la tabla en memoria empezamos a trabajar con ella y para eso tenemos que ver que patrones tiene ##
    archivo_salida = open("./import/posiblesactivos.csv","w")
    # # # # print lista_hoja1
    for x in range(0,len(lista_hoja1)):
        Contrato = lista_hoja1[x][6]
        ccc = lista_hoja1[x][0]
        ctp = lista_hoja1[x][7]
        ctp = ctp.replace(",",".")
        ctp1 = ctp[0:2]
        if ctp1 == "  ":
        	ctp = float(1.0)
        if ctp =="" or ctp == " ":
            ctp =float(1.0)
        ctp = float(ctp)
        FechaBaja =lista_hoja1[x][4]
        ###################################################################
        ############# Madrid###############################################
        ###################################################################

        array_madrid =["100","200","130","230","150","250","420","520"]
        ccc_madrid = ["28"]
        ctp_madrid = float(0.625)

        if Contrato in array_madrid and ccc[0:2] in ccc_madrid and ctp >= ctp_madrid and FechaBaja =="0000-00-00":

            if x != len(lista_hoja1)-1:
                naf_empleado = lista_hoja1[x][1]
                autorizado_1 = lista_hoja1[x][16]
                naf_2 = lista_hoja1[x+1][1]
                autorizado_2 =lista_hoja1[x+1][16]
                if str(naf_empleado + autorizado_1) == str(naf_2 + autorizado_2):
                    fechas =lista_hoja1[x+1][4]# obtengo la fecha de baja de entrada anterior
                    if fechas == "0000-00-00":
                        mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Madrid"+"\n"))
                    if fechas != "0000-00-00":
                        delta = lista_hoja1[x][3] - lista_hoja1[x+1][4]
                        if delta.days >=180:
                            mirar ="mirar subvencion"
                        else:
                            mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" + str(mirar) +";"+ ""+ ";"+"Madrid"+"\n"))                   
                if str(naf_empleado + autorizado_1) != str(naf_2 + autorizado_2):
                    mirar ="mirar subvencion"
                    archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" + str(mirar) +";"+ ""+ ";"+"Madrid"+"\n"))
            if x == len(lista_hoja1)-1:
                mirar ="mirar subvencion"
                archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Madrid"+"\n"))
    #     ###################################################################
    #     ############# Badajoz y caceres ###################################
    #     ###################################################################

        array_badajoz =["100","200","130","230","150","250"]
        ccc_badajoz= ["06","10"]
        ctp_badajoz = float(0.5)

        if Contrato in array_badajoz and ccc[0:2] in ccc_badajoz and ctp >= ctp_badajoz and FechaBaja =="0000-00-00":
            if x != len(lista_hoja1)-1:
                naf_empleado = lista_hoja1[x][1]
                autorizado_1 = lista_hoja1[x][16]
                naf_2 = lista_hoja1[x+1][1]
                autorizado_2 =lista_hoja1[x+1][16]
                if str(naf_empleado + autorizado_1) == str(naf_2 + autorizado_2):
                    fechas =lista_hoja1[x+1][4]# obtengo la fecha de baja de entrada anterior
                    if fechas == "0000-00-00":
                        mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar)+";"+ ""+ ";"+"Badajoz y Caceres"+"\n"))
                    if fechas != "0000-00-00":
                        delta = lista_hoja1[x][3] - lista_hoja1[x+1][4]
                        if delta.days >=180:
                            mirar ="mirar subvencion"
                        else:
                            mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar)+";"+ ""+ ";"+"Badajoz y Caceres"+"\n"))                   
                if str(naf_empleado + autorizado_1) != str(naf_2 + autorizado_2):
                    mirar ="mirar subvencion"
                    archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+ str(lista_hoja1[x][15])+";"+ str(lista_hoja1[x][16])+ ";" + str(mirar) +";"+ ""+ ";"+"Badajoz y Caceres"+"\n"))
            if x == len(lista_hoja1)-1:
                mirar ="mirar subvencion"
                archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Badajoz y Caceres"+"\n"))
        ###################################################################
        ############# andalucia ###########################################
        ###################################################################

        array_andalucia =["420","520","100","200"]
        ccc_andalucia= ["04","11","14","18","21","23","29","41"]
        ctp_andalucia = float(0.5)

        if Contrato in array_andalucia and ccc[0:2] in ccc_andalucia and ctp >= ctp_andalucia and FechaBaja =="0000-00-00":
            if x != len(lista_hoja1)-1:
                naf_empleado = lista_hoja1[x][1]
                autorizado_1 = lista_hoja1[x][16]
                naf_2 = lista_hoja1[x+1][1]
                autorizado_2 =lista_hoja1[x+1][16]
                if str(naf_empleado + autorizado_1) == str(naf_2 + autorizado_2):
                    fechas =lista_hoja1[x+1][4]# obtengo la fecha de baja de entrada anterior
                    if fechas == "0000-00-00":
                        mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Andalucia"+"\n"))
                    if fechas != "0000-00-00":
                        delta = lista_hoja1[x][3] - lista_hoja1[x+1][4]
                        if delta.days >=180:
                            mirar ="mirar subvencion"
                        else:
                            mirar = ""
                            archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Andalucia"+"\n"))                   
                if str(naf_empleado + autorizado_1) != str(naf_2 + autorizado_2):
                    mirar ="mirar subvencion"
                    archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Andalucia"+"\n"))
            if x == len(lista_hoja1)-1:
                mirar ="mirar subvencion"
                archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Andalucia"+"\n"))
        ########################################################
        ############# Murcia ###################################
        ########################################################

        array_murcia =["420"]
        ccc_murcia= ["30"]
        ctp_murcia = float(0.5)

        if Contrato in array_murcia and ccc[0:2] in ccc_murcia and ctp >= ctp_murcia and FechaBaja =="0000-00-00":
            if x != len(lista_hoja1)-1:
                naf_empleado = lista_hoja1[x][1]
                autorizado_1 = lista_hoja1[x][16]
                naf_2 = lista_hoja1[x+1][1]
                autorizado_2 =lista_hoja1[x+1][16]
                if str(naf_empleado + autorizado_1) == str(naf_2 + autorizado_2):
                    fechas =lista_hoja1[x+1][4]# obtengo la fecha de baja de entrada anterior
                    if fechas == "0000-00-00":
                        mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Murcia"+"\n"))
                    if fechas != "0000-00-00":
                        delta = lista_hoja1[x][3] - lista_hoja1[x+1][4]
                        if delta.days >=180:
                            mirar ="mirar subvencion"
                        else:
                            mirar = ""
                            archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Murcia"+"\n"))                   
                if str(naf_empleado + autorizado_1) != str(naf_2 + autorizado_2):
                    mirar ="mirar subvencion"
                    archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" + str(mirar) +";"+ ""+ ";"+"Murcia"+"\n"))
            if x == len(lista_hoja1)-1:
                mirar ="mirar subvencion"
                archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" + str(mirar) +";"+ ""+ ";"+"Murcia"+"\n"))

        ###################################################################
        ############# valencia castellon alicante  ########################
        ###################################################################

        array_valencia =["420","100"]
        ccc_valencia= ["46","12","03"]
        ctp_valencia = float(1)

        if Contrato in array_valencia and ccc[0:2] in ccc_valencia and ctp >= ctp_valencia and FechaBaja =="0000-00-00":
            if x != len(lista_hoja1)-1:
                naf_empleado = lista_hoja1[x][1]
                autorizado_1 = lista_hoja1[x][16]
                naf_2 = lista_hoja1[x+1][1]
                autorizado_2 =lista_hoja1[x+1][16]
                if str(naf_empleado + autorizado_1) == str(naf_2 + autorizado_2):
                    fechas =lista_hoja1[x+1][4]# obtengo la fecha de baja de entrada anterior
                    if fechas == "0000-00-00":
                        mirar = ""
                        archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Comunidad Valenciana"+"\n"))
                    if fechas != "0000-00-00":
                        delta = lista_hoja1[x][3] - lista_hoja1[x+1][4]
                        if delta.days >=180:
                            mirar ="mirar subvencion"
                        else:
                            mirar = ""
                            archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1]) +";"+str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Comunidad Valenciana"+"\n"))                   
                if str(naf_empleado + autorizado_1) != str(naf_2 + autorizado_2):
                    mirar ="mirar subvencion"
                    archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Comunidad Valenciana"+"\n"))
            if x == len(lista_hoja1)-1:
                mirar ="mirar subvencion"
                archivo_salida.write(str(str(lista_hoja1[x][0]) +";"+str(lista_hoja1[x][1])+";"+ str(lista_hoja1[x][2])+";"+str(lista_hoja1[x][3])+";"+str(lista_hoja1[x][4])+";"+str(lista_hoja1[x][5])+";"+str(lista_hoja1[x][6])+";"+str(lista_hoja1[x][7])+";"+str(lista_hoja1[x][8])+";"+str(lista_hoja1[x][9])+";"+str(lista_hoja1[x][10])+";"+str(lista_hoja1[x][11])+";"+str(lista_hoja1[x][12])+";"+str(lista_hoja1[x][13])+";"+str(lista_hoja1[x][14])+";"+str(lista_hoja1[x][15])+";"+str(lista_hoja1[x][16])+ ";" +str(mirar) +";"+ ""+ ";"+"Comunidad Valenciana"+"\n"))
   
print ("Consulta Procesada correctamente")
