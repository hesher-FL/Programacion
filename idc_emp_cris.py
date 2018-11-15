# IMPORT  PYMYSQL
import pymysql
from os import listdir
import time
from datetime import datetime,timedelta
fecha= time.strftime("%x")
archivo_salida = open("C:\\Users\\jflores\\Desktop\\Programacion\\import\\idcempleado.csv","w")
n = 1
archivo_salida.write(str( "AUTORIZADO"+";"+"REGIMEN" + ";" + "EMPRESA" + ";" + "CCC" +  ";" + "CIF" + ";" + "CNAE" + ";" + "EMPLEADO" + ";" + "NAF" + ";" +" DNI" + ";" + "FECHA_NACIMIENTO "+ ";" + "GRADO_DISCAPACIDAD" + ";" + "PENSIONISTA" + ";" + "PERIODO_idc_desde" + ";"+ "PERIDO_IDC_HASTA" + ";" + "FECHA_ALTA" + ";" + "FECHA_BAJA" + ";" + "FECHA_EFECTOS_BAJA" + ";" + "CONTRATO" + ";" + "COEFICIENTE_TIEMPO_PARCIAL" + ";" + "GRUPO" + ";" + "CLAVE" + ";" + "FECHA_ANTIGUEDAD" + ";" + "FIN_CONTRATO" + ";" + "TRABAJADOR_SUSTITUTO" + ";" + "SITUACIONES" + ";" + "SITUACION_DESDE" + ";" + "SITUACION_HASTA" + ";" + "IT" + ";" + "IMS" + ";" + "TOTAL" + ";" + "DESEMPLEO" + ";" + "PECULIARIDAD" + ";" + "PECULIARIDAD_TEXT"+";"+ "PORCENTAJE" + ";" + "CUANTIA" + ";" + "PECULIARIDAD_DESDE" + ";" + "PECULIARIDAD_HASTA" + ";" + "MOTIVO_GUARDA" + ";" + "red_GUARDA" + ";" + "PERDIDA_BENEFICIO" + ";"+ "SEXO" +";"+ "EXCLUSION_COTIZACION" + ";" + "RLCE" + ";" + "CONDICION_DESEMPLEADO" + ";" + "fin_contrato"+";"+ "fecha_conversion"+";"+"fecha" + ";" + "ficheros" + "\n"))
count = 0
for ficheros in listdir ("C:\\Users\\jflores\\Desktop\\Programacion\\files/"):
    pagina = open("C:\\Users\\jflores\\Desktop\\Programacion\\files/" + ficheros, "r")

    # Iniciamos Variables
    MOTI =""
    flag = 0
    EM=""
    TEXT =""
    TOTAL = ""
    DESEMPLEO =""
    IT = ""
    IMS =""
    REDU=""
    PERDIDA =""
    RLCE =""
    PECU =""
    PORCE =""
    CONDICION_DESEMPLEADO =""
    CUANTIA =""
    PECUD =""
    PECUH =""
    fecha_conversion =""
    fin_contrato =""
    EMPLEADO =""
    FECHAANTI =""
    FINCON=""
    TRABA =""
    SITU =""
    SITUD = ""
    SITUH =""

    #Recorremos el fichero linea a linea

    for line in pagina:
        valor = line[0:3]
        if valor == "DID":
            AUTORIZADO = (line[16:24])
        if valor == "DEM":
            RE = (line[3:7])
            #print RE
            a = (line[7:9])
            b = (line[9:18])
            CCC = a + " " + b
            CIF = (line[24:33])
            CNAE = (line[42:46])
            EXCLUSION = (line[39:42])
            if EXCLUSION =="000":
                EXCLUSION = ""
            if EXCLUSION == "064":
                EXCLUSION = "064-Contrato a tiempo parcial reducido"
            if EXCLUSION == "087":
                EXCLUSION = "087-Contrato de aprendizaje"
            if EXCLUSION == "300":
                EXCLUSION = "300-Asistencia Sanitaria Concertada "
            if EXCLUSION == "301":
                EXCLUSION = "301-Asistencia Sanitaria Concertada menos farmacia"
            if EXCLUSION == "302":
                EXCLUSION = "302-Asistencia Sanitaria Medicina General, Pediatria, Puericultura, Servicio de Urgencia Ambulatoria"
            if EXCLUSION == "303":
                EXCLUSION = "303-Asistencia Sanitaria Servicio de Urgencia"
            if EXCLUSION == "304":
                EXCLUSION = "304-Asistencia Sanitaria Ambulatoria"
            if EXCLUSION == "305":
                EXCLUSION = "305-Asistencia Sanitaria Concertada con AT y EP, menos farmacia"
            if EXCLUSION == "306":
                EXCLUSION = "306-Asistencia Sanitaria Emigrantes"
            if EXCLUSION == "307":
                EXCLUSION = "307-Asistencia Sanitaria Concertada mas AT y EP"
            if EXCLUSION == "308":
                EXCLUSION = "308-Asistencia Sanitaria Pensionistas clases pasivas"
            if EXCLUSION == "309":
                EXCLUSION = "309-Asistencia Sanitaria Concertada MUNPAL"
            if EXCLUSION == "751":
                EXCLUSION = "751-Prestacion Desempleo. Extincion"
            if EXCLUSION == "752":
                EXCLUSION = "752-Prestacion Desempleo. Suspension"
            if EXCLUSION == "753":
                EXCLUSION = "753-Subsidio desempleo mayor 52a55 anhos o fijos discontinuos. Etincion"
            if EXCLUSION == "754":
                EXCLUSION = "754-Subsidio desempleo >52/55 anhos o fijos discontinuos. Suspension"
            if EXCLUSION == "755":
                EXCLUSION = "755-Subsidio desempleo. Extincion"
            if EXCLUSION == "756":
                EXCLUSION = "756-Subsidio desempleo. Suspension"
            if EXCLUSION == "900":
                EXCLUSION = "900-Funcionarios Interinos Administracion Central de Estado"
            if EXCLUSION == "901":
                EXCLUSION = "901-Funcionarios y Personal Estatutario"
            if EXCLUSION == "902":
                EXCLUSION = "902-Funcionarios Interinos"
            if EXCLUSION == "903":
                EXCLUSION = "903-Altos cargos, alcaldes. Excluidos de FOGASA"
            if EXCLUSION == "904":
                EXCLUSION = "904-Altos cargos, alcaldes. Excluidos de FOGASA y desempleo"
            if EXCLUSION == "905":
                EXCLUSION = "905-Trabajadores en Colaboracion Social"
            if EXCLUSION == "906":
                EXCLUSION = "906-Alumnos Escuelas Formacion Profesional"
            if EXCLUSION == "907":
                EXCLUSION = "907-Trabajadores extranjeros de paises sin convenio bilateral"
            if EXCLUSION == "909":
                EXCLUSION = "909-Reclusos que realizan trabajos de aprendizaje o formacion profesional"
            if EXCLUSION == "910":
                EXCLUSION = "910-Funcionario procedente de MUNPAL - no SNS -"
            if EXCLUSION == "911":
                EXCLUSION = "911-Interino procedente de MUNPAL - no SNS -"
            if EXCLUSION == "912":
                EXCLUSION = "912-Funcionario Interino Regimen General situaciones especiales, cumplimiento del servicio militar o prestacion del servicio social"
            if EXCLUSION == "914":
                EXCLUSION = "914-Agentes Auxiliares Union Europea, Funcionarios espanholes excluidos de desempleo"
            if EXCLUSION == "915":
                EXCLUSION = "915-Parlamentarios de Comunidades Autonomas procedentes de Regimen Especial de Trabajadores Autonomos"
            if EXCLUSION == "916":
                EXCLUSION = "916-Parlamentarios Cortes espanholas, europeas y comunidades autonomas"
            if EXCLUSION == "917":
                EXCLUSION = "917-Ministerio de Defensa. Patronato Militar"
            if EXCLUSION == "918":
                EXCLUSION = "918-SMinisterio de Interior. Patronato Militar-Mexc"
            if EXCLUSION == "919":
                EXCLUSION = "919-Mutualidad Prevision Sanitaria Nacional"
            if EXCLUSION == "920":
                EXCLUSION = "920-Funcionarios procedentes de la extinguida Administracion del Movimiento"
            if EXCLUSION == "922":
                EXCLUSION = "922-Ministerio de Interior. Patronato Militar excluido de IT"
            if EXCLUSION == "923":
                EXCLUSION = "923-Convenio de amistad hispano-USA"
            if EXCLUSION == "924":
                EXCLUSION = "924-Trabajador trasladado al extranjero sin beneficiarios en Espanha"
            if EXCLUSION == "925":
                EXCLUSION = "925-Trabajador en extranjero con beneficiarios en Espanha"
            if EXCLUSION == "927":
                EXCLUSION = "927-Maestranza aerea de Sevilla"
            if EXCLUSION == "928":
                EXCLUSION = "928-Hospital Universitario Valladolid. Estatutarios"
            if EXCLUSION == "929":
                EXCLUSION = "929-Hospital Universitario Valladolid. Interinos"
            if EXCLUSION == "930":
                EXCLUSION = "930-Socios Trabajadores Cooperativas (trabajo asociado y explotacion de la tierra)"
            if EXCLUSION == "931":
                EXCLUSION = "931-Reclusos con actividad laboral"
            if EXCLUSION == "932":
                EXCLUSION = "932-Personal estatutario temporal org. salud"
            if EXCLUSION == "933":
                EXCLUSION = "933-Becarios de investigacion"
            if EXCLUSION == "934":
                EXCLUSION = "934-Funcionarios procedentes de MUNPAL -SNS-"
            if EXCLUSION == "935":
                EXCLUSION = "935-Interinos procedentes de MUNPAL -SNS-"
            if EXCLUSION == "936":
                EXCLUSION = "936-Penados en beneficio de la Comunidad"
            if EXCLUSION == "937":
                EXCLUSION = "937-Funcionarios nuevo ingreso  RDL 13/2010"
            if EXCLUSION == "938":
                EXCLUSION = "938-Alumno nuevo ingreso Ministerio de Defensa  RDL 13/2010"
            if EXCLUSION == "939":
                EXCLUSION = "939-Clero diocesano de la iglesia catolica"
            if EXCLUSION == "941":
                EXCLUSION = "941-Ministros culto de la iglesia adventista y ferede"
            if EXCLUSION == "942":
                EXCLUSION = "942-Religiosos comunidades israelitas de Espanha"
            if EXCLUSION == "950":
                EXCLUSION = "950-Armadores asimilados a trabajadores cuenta ajena Regimen Especial del Mar"
            if EXCLUSION == "951":
                EXCLUSION = "951-Consejero administrador SMC  Situacion laboral asimilada a cuenta ajena"
            if EXCLUSION == "952":
                EXCLUSION = "952-Trabajadores espanholes de la Administracion espanhola en el extranjero"
            if EXCLUSION == "953":
                EXCLUSION = "953-Interinos de la Administracion de Justicia"
            if EXCLUSION == "954":
                EXCLUSION = "954-Practicos de puerto asimilados a cuenta ajena Regimen Especial de Trabajadores del Mar"
            if EXCLUSION == "960":
                EXCLUSION = "960-Trabajadores Extranjeros. Exclusion Cotizacion por Desempleo"
            if EXCLUSION == "961":
                EXCLUSION = "961-Convenio Japon AT/EP"
            if EXCLUSION == "962":
                EXCLUSION = "962-Convenio Corea AT/EP"
            if EXCLUSION == "970":
                EXCLUSION = "970-Reconversion industrial cotizacion adicional al desempleo"
            if EXCLUSION == "971":
                EXCLUSION = "971-Reconversion industrial ayu equi jubilacion anticipada"
            if EXCLUSION == "972":
                EXCLUSION = "972-Promocion ind cotiz adicional al desempleo"
            if EXCLUSION == "983":
                EXCLUSION = "983-Cotizacion Desempleo Regimen Especial Agrario Cuenta Ajena Fijos IT/Maternidad"
            if EXCLUSION == "984":
                EXCLUSION = "984-Mesas electorales"
            if EXCLUSION == "985":
                EXCLUSION = "985-Trabajadores cuota obrera IT/Maternidad"
            if EXCLUSION == "986":
                EXCLUSION = "986-Programas de formacion"
        if valor == "RZS":
            EM = (line[3:43])
            EM = EM.rstrip()
        if valor == "NAN" :
            EMPLEADO = (line[3:53])
            EMPLEADO = EMPLEADO.rstrip()
            # print EMPLEADO
        if valor == "DAF" :
            a = (line[3:5])
            b= (line[5:15])
            NAF = a + " " + b
            SEXO = (line[52:53])
            if  SEXO == "1":
                SEXO = "1-Hombre"
            if SEXO == "2":
                SEXO = "2-Mujer"
            if SEXO =="3":
                SEXO = "3-Binario"
            DNI = (line[21:30])
            a = (line[30:34])
            b = (line[34:36])
            c = (line[36:38])
            FECHAN = c + "/" + b + "/" + a
            GRADO = (line[38:40])
            PEN = (line[44:45])
            if PEN == "N":
                PEN = "NO"
            elif PEN == "S":
                PEN = "SI"
        if valor == "DFE":



            a = (line[3:7])
            b = (line[7:9])
            c = (line[9:11])

            PERD= c + "/" + b + "/" + a

            a = (line[11:15])
            b = (line[15:17])
            c = (line[17:19])
            if a == "9999":
                a = "0000"
            if b == "99":
                b = "00"
            if c == "99":
                c = "00"

            PERH = c + "/" + b + "/" + a

            a = (line[25:29])
            b = (line[29:31])
            c = (line[31:33])

            FECHAA = c + "/" + b + "/" + a


            a = (line[33:37])
            b = (line[37:39])
            c = (line[39:41])

            FECHAB = c + "/" + b + "/" + a

            a = (line[41:45])
            b = (line[45:47])
            c = (line[47:49])

            FECHAE= c + "/" + b + "/" + a


        if valor == "DCT":
            CONTRATO = (line[3:6])
            CLAVE = (line[26:27])
            GRUPO = (line[24:26])
            MOTI = (line [63:64])
            RLCE = (line[9:13])
            CONDICION_DESEMPLEADO = (line[13:14])
            # print CONDICION_DESEMPLEADO
        if MOTI == "1":
            MOTI = "Cuidado de menor"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "2":
            MOTI = "Cuidado de discapacitado"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "3":
            MOTI = "Cuidado de familiar"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "4":
            MOTI = "Lactancia"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "5":
            MOTI = "Violencia de genero"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "6":
            MOTI = "Nacimiento de hijo prematuro"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "7":
            MOTI = "Cuidado de menor con enfermedad grave"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "8":
            MOTI = "Cuidado menor enfermedad grave y  otra reduccion de jornada"
            a = (line[6:9])
            REDU = str (int (a) / float (1000))
            REDU = REDU.replace(".",",")
            COE = "0"
            #print REDU
        elif MOTI == "0":
            MOTI = "Sin reduccion"
            a = (line [6:9])
            #print a
            COE = str(int (a) / float (1000))
            COE = COE.replace(".", ",")
            CLAVE = (line[26:27])
        if RLCE =="0100":
            RLCE = "0100-Personal de Alta Direccion"
        elif RLCE == "0301":
            RLCE = "0301-Penados en Instituciones Penitenciarias. Aprendizaje/Formacion"
        elif RLCE == "0302":
            RLCE = "0302-Penados en Instituciones Penitenciarias. Actividad Laboral"
        elif RLCE == "0303":
            RLCE = "0303-Penados en Instituciones Penitenciarias. Beneficio Comunidad"
        elif RLCE == "0304":
            RLCE = "0304-Penados en Instituciones Penitenciarias. Menores"
        elif RLCE == "0409":
            RLCE = "0409-Deportistas profesionales"
        elif RLCE == "0500":
            RLCE = "0500-Representantes de comercio"
        elif RLCE == "0501":
            RLCE = "0501-Representantes de comercio -vendedores del cupon de la ONCE-"
        elif RLCE == "0600":
            RLCE = "0600-Minusvalidos en Centros Especiales de Empleo"
        elif RLCE == "0601":
            RLCE = "0601-Minusvalido procedente enclave laboral"
        elif RLCE == "0602":
            RLCE = "0602-Discapacitado Organizacion Nacional de Ciegos"
        elif RLCE == "0700":
            RLCE = "0700-Estibadores portuarios"
        elif RLCE == "0800":
            RLCE = "0800-Artistas en espectaculos publicos"
        elif RLCE == "0900":
            RLCE = "0900-Abogados en despachos de abogados"
        elif RLCE == "9901":
            RLCE = "9901-Investigadores del Sistema Espanhol de Ciencia y Tecnologia-contratos practicas-"
        elif RLCE == "9902":
            RLCE = "9902-Medicos Interinos Residentes"
        elif RLCE == "9903":
            RLCE = "9903-Universidad Publica -Profesor Ayudante"
        elif RLCE == "9904":
            RLCE = "9904-Universidad Publica -Profesor Ayudante Doctor"
        elif RLCE == "9905":
            RLCE = "9905-Universidad Publica -Profesor Colaborador"
        elif RLCE == "9906":
            RLCE = "9906-Universidad Publica -Profesor Contratado Doctor"
        elif RLCE == "9907":
            RLCE = "9907-Universidad Publica -Profesor Asociado"
        elif RLCE == "9908":
            RLCE = "9908-Universidad Publica -Profesor Visitante"
        elif RLCE == "9909":
            RLCE = "9909-Personal investigador en formacion - Beca"
        elif RLCE == "9910":
            RLCE = "9910-Personal investigador en formacion - Contrato practicas"
        elif RLCE == "9911":
            RLCE = "9911-Alumnos - Trabajadores en programas de escuela taller"
        elif RLCE == "9912":
            RLCE = "9912-Alumnos - Trabajadores en programas de casas de oficios"
        elif RLCE == "9913":
            RLCE = "9913-Alumnos Trabajadores en programas de talleres de empleo"
        elif RLCE == "9914":
            RLCE = "9914-Pensionista de incapacidad S.S."
        elif RLCE == "9915":
            RLCE = "9915-Pensionista de incapacidad clases pasivas"
        elif RLCE == "9916":
            RLCE = "9916-UPersonal investigador I+D+I"
        elif RLCE == "9918":
            RLCE = "9918-Contratos de Formacion - Prorroga posterior 18-06-2010"
        elif RLCE == "9920":
            RLCE = "9920-Contrato de formacion no bonificados. posterior 18.06.2011"
        elif RLCE == "9921":
            RLCE = "9921-Contrato predoctoral. Incentivado"
        elif RLCE == "9922":
            RLCE = "9922-Participantes en programas para la formacion"
        elif RLCE == "9923":
            RLCE = "9923-Practicas no laborales en empresas"
        elif RLCE == "9924":
            RLCE = "9924-Socio Sociedad Laboral"
        elif RLCE == "9925":
            RLCE = "9925-No socio Sociedad Laboral"
        elif RLCE == "9926":
            RLCE = "9926-Alumno participante en Proyecto de Empleo-Formacion"
        elif RLCE == "9927":
            RLCE = "9927-Practicas Academicas Externas"
        elif RLCE == "9928":
            RLCE = "9928-Practicas curriculares externas Real Decreto-Ley 8/2014"
        elif RLCE == "9929":
            RLCE = "9929-Contrato predoctoral. No incentivado."
        elif RLCE =="0000":
            RLCE = ""

        if CONDICION_DESEMPLEADO =="1":
            CONDICION_DESEMPLEADO ="1-Desempleado inscrito en la oficina de empleo"
        elif CONDICION_DESEMPLEADO == "2":
            CONDICION_DESEMPLEADO = "2-Desempleado inscrito en la oficina de empleo durante mas de 12 meses"
        elif CONDICION_DESEMPLEADO == "3":
            CONDICION_DESEMPLEADO = "3-Desempleado subsidio REA"
        elif CONDICION_DESEMPLEADO == "4":
            CONDICION_DESEMPLEADO = "4-DBeneficiario prestacion desempleo -contributiva o asistencial- durante mas de un anho"
        elif CONDICION_DESEMPLEADO == "5":
            CONDICION_DESEMPLEADO = "5-Desempleado inscrito en la oficina de empleo durante mas de 6 meses"
        elif CONDICION_DESEMPLEADO == "6":
            CONDICION_DESEMPLEADO = "6-Beneficiario prestacion desempleo -contributiva o asistencial- al que falta un anho o mas de percepcion de la prestacion"
        elif CONDICION_DESEMPLEADO == "7":
            CONDICION_DESEMPLEADO = "7-Beneficiario subsidio desempleo. Mayor de 52 anhos"
        elif CONDICION_DESEMPLEADO == "U":
            CONDICION_DESEMPLEADO = "U-Desempleado + 6 meses excedente sector textil"
        elif CONDICION_DESEMPLEADO == "F":
            CONDICION_DESEMPLEADO = "F-Desempleado inscrito en la oficina de empleo. Carga familiar"
        elif CONDICION_DESEMPLEADO == "G":
            CONDICION_DESEMPLEADO = "G-esempleado inscrito en la oficina de empleo + 6 meses. Carga familiar"
        elif CONDICION_DESEMPLEADO == "A":
            CONDICION_DESEMPLEADO = "A-Beneficiario Prestacion Desempleo"
        elif CONDICION_DESEMPLEADO == "M":
            CONDICION_DESEMPLEADO = "M-Desempleado contrato de trabajo CTP <333"
        elif CONDICION_DESEMPLEADO == "B":
            CONDICION_DESEMPLEADO = "B-Desempleado con problemas de empleabilidad"
        elif CONDICION_DESEMPLEADO == "C":
            CONDICION_DESEMPLEADO = "C-Desempleado 01.01.2011"
        elif CONDICION_DESEMPLEADO == "D":
            CONDICION_DESEMPLEADO = "D-Desempleado 01.01.2011 12 meses en 18 meses "
        elif CONDICION_DESEMPLEADO == "E":
            CONDICION_DESEMPLEADO = "E-Desempleado 16.08.2011"
        elif CONDICION_DESEMPLEADO == "H":
            CONDICION_DESEMPLEADO = "H-Desempleado sin experiencia laboral o inferior a 3 meses"
        elif CONDICION_DESEMPLEADO == "I":
            CONDICION_DESEMPLEADO = "I-Desempleado procedente de otro sector de actividad"
        elif CONDICION_DESEMPLEADO == "D":
            CONDICION_DESEMPLEADO = "D-aempleado sin experiencia laboral o inferior a 3 meses. Empleo joven"
        elif CONDICION_DESEMPLEADO == "K":
            CONDICION_DESEMPLEADO = "K-esempleado sin titulo oficial ensenhanza "
        elif CONDICION_DESEMPLEADO == "P":
            CONDICION_DESEMPLEADO = "P-Tarifa Plana"
        elif CONDICION_DESEMPLEADO == "R":
            CONDICION_DESEMPLEADO = "R-Tarifa reducida"

        if valor == "ODC":
            a = (line[11:15])
            b = (line[15:17])
            c = (line[17:19])

            fin_contrato= c + "/" + b + "/" + a


            if fin_contrato != "00/00/0000" or fin_contrato != "99/99/9999":
                # print fin_contrato
                if fin_contrato == "00/00/0000" or fin_contrato == "99/99/9999":
                    fin_contrato =""
                    fecha_conversion =""
                else:
                    fe = datetime.strptime(fin_contrato,'%d/%m/%Y')
                    dia = timedelta(days=1)
                    fecha_conversion =  fe + dia
                    fecha_conversion =str(fecha_conversion)
                    fecha_conversion =fecha_conversion[8:10] +"/"+fecha_conversion[5:7]  +"/"+fecha_conversion[0:4]



            a = (line[3:7])
            b = (line[7:9])
            c = (line[9:11])

            FECHAANTI = c + "/" + b + "/" + a
            a = (line[11:15])
            b = (line[15:17])
            c = (line[17:19])
            if a == "9999":
                a = "0000"
            if b == "99":
                b = "00"
            if c == "99":
                c = "00"

            FINCON = c + "/" + b + "/" + a

            a = (line[36:38])
            b = (line[38:48])

            TRABA = a + " "+ b
        if valor == "DAD":
            PERDIDA  =(line[3:5])

            if PERDIDA == "01":
                PERDIDA  = "01- Falta de concurrencias de requisitos"
            if PERDIDA == "02":
                PERDIDA  = "02- Empresario deudor a la Seguridad Social"
            if PERDIDA == "03":
                PERDIDA  = "03-Alta en la empresa 24 meses previos con contrato indefinido"
            if PERDIDA == "04":
                PERDIDA  = "04- Alta empresa. 6 meses previos"
            if PERDIDA == "05":
                PERDIDA  = "05- Alta 3 meses previos contrato indefinido"
            if PERDIDA == "06":
                PERDIDA  = "06- Administracion Publica"
            if PERDIDA == "07":
                PERDIDA  = "07-Inexistencia contrato temporal previo"
            if PERDIDA == "08":
                PERDIDA  = "08- Extincion contrato bonificado ultimos 12 meses"
            if PERDIDA == "09":
                PERDIDA  = "09- Empresa sin la condicion de insercion"
            if PERDIDA == "11":
                PERDIDA  = "11- Deudora la fecha de inicio del derecho"
            if PERDIDA == "12":
                PERDIDA  = "12- Alta posterior plazo reglamentario ingreso"
            if PERDIDA == "13":
                PERDIDA  = "13- Delito contra Hacienda Publica y Seguridad Social"
            if PERDIDA == "19":
                PERDIDA  = "19-Empresa con deuda ss.mecanizada tras alta"
            if PERDIDA == "20":
                PERDIDA  = "20-Incumplimiento obligaciones tributarias"
            if PERDIDA == "21":
                PERDIDA  = "21- Deudas tributarias"
            if PERDIDA == "22":
                PERDIDA  = "22- Incumplimiento obligaciones tributarias + deudas tributarias"
            if PERDIDA == "23":
                PERDIDA  = "23- Baja censal detectada"
            if PERDIDA == "24":
                PERDIDA  = "24-Delito fiscal"
            if PERDIDA == "25":
                PERDIDA  = "25- Incumplimiento obligaciones tributarias + deuda tributaria + delito fiscal"
            if PERDIDA == "26":
                PERDIDA  = "26- Incumplimiento obligaciones tributarias + delito fiscal"
            if PERDIDA == "27":
                PERDIDA  = "27- Deudas tributarias + delito fiscal"
            if PERDIDA == "28":
                PERDIDA  = "28- Incumplimiento obligaciones tributarias + deuda tributaria + baja censal"
            if PERDIDA == "29":
                PERDIDA  = "29-Deudas tributarias + baja censal"
            if PERDIDA == "30":
                PERDIDA  = "30- Delito fiscal + baja censal"
            if PERDIDA == "31":
                PERDIDA  = "31- Incumplimiento obligaciones tributarias + deuda tributaria + delito fiscal + baja censal"
            if PERDIDA == "32":
                PERDIDA  = "32- Incumplimiento obligaciones tributarias + delito fiscal + baja censal"
            if PERDIDA == "33":
                PERDIDA  = "33-Deuda tributaria + delito fiscal + baja censal"
            if PERDIDA == "34":
                PERDIDA  = "34- Incumplimiento obligaciones tributarias + deuda tributaria + baja censal"
            if PERDIDA == "35":
                PERDIDA  = "35-Incumplimiento obligaciones tributarias durante reduccion"
            if PERDIDA == "40":
                PERDIDA  = "40- No acredita derecho segun SPEE"
            if PERDIDA == "41":
                PERDIDA  = "41- Incumplimiento mantenimiento empleo"
            if PERDIDA == "42":
                PERDIDA  = "42- No aplicacion condiciones C.E.E. - Subrogacion de contrato"
            if PERDIDA == "43":
                PERDIDA  = "43-Plantilla trabajadores excede a la de deduccion"
            if PERDIDA == "44":
                PERDIDA  = "44- No acreditacion exclusion social/victima violencia"
            if PERDIDA == "45":
                PERDIDA  = "45- Incumplimiento mantenimiento nivel empleo"
            if PERDIDA == "46":
                PERDIDA  = "46- Decision extintiva improcedente/6 meses"
            if PERDIDA == "47":
                PERDIDA  = "47-No acreditacion Inscripcion Oficina de Empleo segun SPEE"
            if PERDIDA == "48":
                PERDIDA  = "48- Falta de ingreso obligaciones en plazo"
            if PERDIDA == "49":
                PERDIDA  = "49- Incumplimiento mantenimiento nivel empleo. 1 anho."
            if PERDIDA == "50":
                PERDIDA  = "50-Incumplimiento mantenimiento nivel empleo. 2 anho. R. parcial"
            if PERDIDA == "51":
                PERDIDA  = "51- Incumplimiento mantenimiento nivel empleo. 3 anho. R. parcial"
            if PERDIDA == "52":
                PERDIDA  = "52-No incremento nivel empleo total"
            if PERDIDA == "53":
                PERDIDA  = "53-No incremento nivel empleo fijo"
            if PERDIDA == "54":
                PERDIDA  = "54- No inscripcion Sistema Nacional Garantia Juvenil"
            if PERDIDA == "55":
                PERDIDA  = "55- Incumplimiento mantenimiento nivel de empleo. 2 anho. R. total."
            if PERDIDA == "56":
                PERDIDA  = "56-Incumplimiento mantenimiento nivel de empleo. 3 anho. R. total."
            if PERDIDA == "57":
                PERDIDA  = "57- Deuda Seguridad Social. Trabajador post plazo presentacion"
            if PERDIDA == "58":
                PERDIDA  = "58- Deuda Seguridad Social. Trabajador post presentacion liquidacion"
            if PERDIDA == "59":
                PERDIDA  = "59- Incumplimiento informa motivado vinculante - I+D+i"
            if PERDIDA == "99":
                PERDIDA  = "99- Falta requisitos vigencia incentivo"
            SITU = (line[24:54])
            a = (line[54:58])
            b = (line[58:60])
            c = (line[60:62])
            if c =="  ":
                SITUD = " "
            else:
                SITUD = c +"/" + b +"/"+ a

            a = (line[62:66])
            b = (line[66:68])
            c = (line[68:70])
            if c == "  ":
                SITUH = " "
            else:
                SITUH = c +"/"+ b+"/"+a
            j = (line[24:27])
            if j != "***":
                flag = 1
            if j =="***":
                SITU =""
                SITUD =""
                SITUH=""

        if flag == 1:
            archivo_salida.write(str(AUTORIZADO +";" + RE + ";" + EM + ";" + CCC +  ";" + CIF + ";" + CNAE + ";" + EMPLEADO + ";" + NAF + ";" + DNI + ";" + FECHAN + ";" + GRADO + ";" + PEN + ";" + PERD + ";"+ PERH + ";" + FECHAA + ";" + FECHAB + ";" + FECHAE + ";" + CONTRATO + ";" + COE + ";" + GRUPO + ";" + CLAVE + ";" + FECHAANTI + ";" + FINCON + ";" + TRABA + ";" + SITU + ";" + SITUD + ";" + SITUH + ";" + IT + ";" + IMS + ";" + TOTAL + ";" + DESEMPLEO + ";" + PECU + ";" + TEXT +";" +PORCE + ";" + CUANTIA + ";" + PECUD + ";" + PECUH + ";" + MOTI + ";" + REDU + ";" + PERDIDA + ";"+ SEXO +";"+ EXCLUSION + ";" + RLCE + ";" + CONDICION_DESEMPLEADO + ";" + fin_contrato +";"+ fecha_conversion+";"+ fecha + ";" + ficheros + "\n"))
            count = count + 1
            flag = 0
            SITU = ""
            SITUD =""
            SITUH =""
            IT = ""
            IMS = ""
            TOTAL = ""
            DESEMPLEO = ""
            PECU =""
            TEXT =""
            PORCE =""
            CUANTIA = ""
            PECUD =""
            PECUH=""
            fin_contrato = ""
            fecha_conversion =""

        if valor == "TTH":
            ENTERA = (line[17:18])
            DECIMAL = (line[18:20])
            TOTAL =  ENTERA + "," + DECIMAL
            ENTERA = (line[5:6])
            DECIMAL = (line[6:8])
            IT = ENTERA + "," + DECIMAL
            ENTERA = (line[11:12])
            DECIMAL = (line[12:14])
            IMS = ENTERA + "," + DECIMAL
            a = (line[23:26])
            DESEMPLEO = str(int (a) / float (100))
            DESEMPLEO = DESEMPLEO.replace(".",",")
        if  valor == "PEC":
            PECU = (line[0:7])
            a = (line[7:12])
            PORCE =  str (int (a) / float (100))
            PORCE = PORCE.replace(".",",")
            a = (line[12:16])
            b = (line[16:18])
            c = (line[18:20])
            PECUD =  c + "/" + b + "/" + a
            a = (line[20:24])
            b = (line[24:26])
            c = (line[26:28])
            PECUH =  c + "/" + b + "/" + a
            z = (line[28:33])
            CUANTIA = str (int (z) /  float (100))
            CUANTIA = CUANTIA.replace(".",",")
        if valor =="LPE":
            a = (line[8:11])
            if a != "FIN":
                b = (len(line))
                TEXT = (line[5:b])
                TEXT = TEXT.replace("\n","")
                archivo_salida.write(str(AUTORIZADO +";" + RE + ";" + EM + ";" + CCC +  ";" + CIF + ";" + CNAE + ";" + EMPLEADO + ";" + NAF + ";" + DNI + ";" + FECHAN + ";" + GRADO + ";" + PEN + ";" + PERD + ";"+ PERH + ";" + FECHAA + ";" + FECHAB + ";" + FECHAE + ";" + CONTRATO + ";" + COE + ";" + GRUPO + ";" + CLAVE + ";" + FECHAANTI + ";" + FINCON + ";" + TRABA + ";" + SITU + ";" + SITUD + ";" + SITUH + ";" + IT + ";" + IMS + ";" + TOTAL + ";" + DESEMPLEO + ";" + PECU + ";" + TEXT +";" +PORCE + ";" + CUANTIA + ";" + PECUD + ";" + PECUH + ";" + MOTI + ";" + REDU + ";" + PERDIDA + ";"+ SEXO +";"+ EXCLUSION + ";" + RLCE + ";" + CONDICION_DESEMPLEADO + ";" + fin_contrato +";"+ fecha_conversion+";"+ fecha + ";" + ficheros + "\n"))
                flag = 0
                SITU = ""
                SITUD =""
                SITUH =""
                PECU =""
                TEXT =""
                PORCE =""
                CUANTIA = ""
                PECUD =""
                PECUH=""
                fin_contrato = ""
                fecha_conversion =""



                count = count + 1
            #contador para generar ficheros
        if count == 500000:
            print ("entro")
            n = n + 1
            archivo_salida.close()
            archivo_salida = open("./imports/load" + str (n) + ".csv","w")
            count = 0
#cerramos ficheros
    pagina.close()
archivo_salida.close()
