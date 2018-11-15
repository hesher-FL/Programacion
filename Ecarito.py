from lxml import etree
import time
Date= time.strftime("%x")
import sys
import os
import argparse
from os import listdir
import shutil

m= 0 
l = 0 
k = 5
CompanyID = " "
INSS = " "
RequestDate = " "
DeductionType = " "
Reference = " "
DeductionCode = " "
StartingDate = " "
EndingDate = " "
CardDeliveryDate = " "


z = 1
count = 0

for ficheros in listdir("./files/"):
    doc = etree.parse("./files/" + ficheros)
    # print (ficheros)
    tree = doc.getroot()
    tipodocu = tree[0].tag
    # print tipodocu
    die = tipodocu.find("http://www.smals-mvm.be/xml/ns/systemFlux")
    # print (die)
    if die == 1:
            
            # archivo_salida = open("./imports/"+ficheros+".csv","w")
            # archivo_salida.write(str("CompanyID" + ";" + "INSS" + ";" + "RequestDate" + ";" + "DeductionType" + ";" + "Reference" + ";" + "DeductionCode" + ";" + "StartingDate"  + ";" + "EndingDate" + ";" + "CardDeliveryDate" + ";" + "Fecha" + ";"+ "Ficheros" + "\n")) 
            
        Form= tree[0]
        Identificacion = Form[0].text
        FromCreationDate = Form[1].text
        FormCreationHou =Form[2].text
        AttestationStatus =Form[3].text
        TypeForm  = Form[4].text

        Nreference = len(Form)
        while k  < len(Form):
        # Aqui te metes en Reference 
            parse = Form[k].tag
            if parse == "{http://www.smals-mvm.be/xml/ns/systemFlux}Reference":
                Reference = Form[k]
                ReferenceType = Reference[0].text
                ReferenceOrigin = Reference[1].text
                ReferenceNbr = Reference[2].text
            if parse == "{http://www.smals-mvm.be/xml/ns/systemFlux}HandledOriginalFile":
                HandledOriginalFile = Form[k]
                SenderId =  HandledOriginalFile[0].text
                FileReference =HandledOriginalFile[1]
                FileName = HandledOriginalFile[0].text
                ReferenceOrigin = HandledOriginalFile[1].text
                ReferenceNbr = HandledOriginalFile[2].text
                FileReceptionInformation = HandledOriginalFile[2]
                ReceptionDate =FileReceptionInformation[0].text
                ReceptionHour=FileReceptionInformation[1].text
                Channel=FileReceptionInformation[2].text
            if parse == "{http://www.smals-mvm.be/xml/ns/systemFlux}ReferenceData":
                ReferenceData = Form[k]
                Quarter = ReferenceData[0].text
                EmployerId = ReferenceData[1]
                NOSSRegistrationNbr = EmployerId[0].text
                CompanyID = EmployerId[1].text

            if parse == "{http://www.smals-mvm.be/xml/ns/systemFlux}Data":
                Data = Form[k]
                DocumentDescription = Data[0]
                TechnicalDescription = DocumentDescription[0]
                MimeType = TechnicalDescription[0].text
                CharacterFormat = TechnicalDescription[1].text
                DocumentXML = Data[1]
                ecaroanswer = DocumentXML[0]
                Necaroanswer = len(ecaroanswer)

                while l < Necaroanswer:
                    WorkerEmploymentMeasuresRecord = ecaroanswer[l].tag
                    if WorkerEmploymentMeasuresRecord =="{http://socialsecurity.be/xml/ns/ecaroanswer}WorkerEmploymentMeasuresRecord":
                        parse1 = ecaroanswer[l]
                        INSS = parse1[0].text
                        RequestDate= parse1[1].text
                        LastUpdateDate = parse1[2].text
                        ReceptionDate = parse1[3].text
                        SectorCode = parse1[4].text
                        DocumentReference = parse1[5].text
                        WorkCardDeliveryDate = parse1[6].text
                        NOSSRegistrationNbr = parse1[7].text
                        CompanyID = parse1[8].text

                        MostAdvantageousDeductions = parse1[9]
                        DeductionCode_1 = parse1[0].text
                        DeductionCode_2 = parse1[1].text
                        DeductionCode_3 = parse1[2].text
                        DeductionCode_4 = parse1[3].text

                        AlternativeDeductions = parse1[11]
                        while m < len(AlternativeDeductions):
                            DeductionCode = AlternativeDeductions[m].tag
                        #     if DeductionCode == "{http://socialsecurity.be/xml/ns/ecaroanswer}DeductionCode":
                        #         Codigo = AlternativeDeductions[m]
                        #         Codigos = Codigo[9].txt


                            m+=1
                        m = 0 
                    l +=1
                # WorkerEmploymentMeasuresRecord
            k  += 1