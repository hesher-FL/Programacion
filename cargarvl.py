# IMPORT  PYMYSQL
# -*- coding: iso-8859-15
# print "Comenzamos a trabajar en su solicitud"
import pymysql
import sys
import argparse
import os
import shutil, os#mover archivos de nombre
import os # cambiarlos de nombre
import glob#importar glob
import time #importar tiempo
# basedatos = sys.argv[1]
from os import listdir
basedatos="Aki"


connection = pymysql.Connect(host='localhost',port = 3306 , user = 'root', db = basedatos)
cursor = connection.cursor()

b = "LOAD DATA INFILE" + "'" + "C:\\\\Users\\\\jflores\\\\Desktop\\\\Programacion\\\\import\\\\" + "load1.csv" + "'" + "INTO TABLE vl  FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' (Autorizado ,Ccc , Naf , Nif , FechaAlta , FechaBaja , FinVacaciones , Contrato , Ctp , Gc , Cl , Nombre , Cnae , CnaeTexto ,Tipo ,RazonSocial  , Regimen ,Fecha ,Ficheros );"
print (b)
cursor.execute(b)
connection.commit()
print ("Datos insertados correctamente en mysql")
