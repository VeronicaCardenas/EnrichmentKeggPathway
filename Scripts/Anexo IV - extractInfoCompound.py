import csv, os 
import directoryStructure

dirCompounds = directoryStructure.keggCompounds
filesCompound = os.listdir(dirCompounds)
fileInformation = open(directoryStructure.cleanInfoKegg + '/compoundIDdataBases.csv', 'w')

for file in filesCompound:
    name = ""
    chembl = ""
    chebi = ""
    comment = ""
    with open(dirCompounds + '/'+file, 'r') as csvfile:
        lines = csvfile.readlines()
        for linea in lines:
            for lineaS in linea.split():
                if 'NAME' == lineaS:
                    nameLine = linea.split()
                    name = nameLine[1]
                    if name[-1] == ';':
                        otherName = lines[2].lstrip()[:-1]
                        name = name[:-1] + '_'+otherName
                        if otherName[-1] == ';':
                            name = name[:-1]
                if 'ChEMBL:' == lineaS:
                    chemblLine = linea.split()
                    chembl = chemblLine[1]
                if 'ChEBI:' == lineaS:
                    chebiLine = linea.split()
                    chebi = chebiLine[1]
                if 'COMMENT' == lineaS:
                    commentLine = linea.split()
                    comment = 'comment: ' + commentLine[1]
        
        resultados = file[:6]+";"+ name +";"+ chembl  + ";"+ chebi+ ";"+ comment
        fileInformation.write(resultados+'\n')

fileInformation.close()
