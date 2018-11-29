import csv, os, xml.etree.cElementTree as ET
import directoryStructure

dirChebismilies = directoryStructure.genericSmilesChebi
archivos = os.listdir(dirChebismilies)
resultados = []
resultadosUnicos = []

fileGenericSmiles = directoryStructure.chebi + '/compoundGenericSmiles.csv'
csv_file = open( fileGenericSmiles,  'w')
for archivo in archivos:
    with open(dirChebismilies + '/' +archivo, 'r' , encoding='utf-8') as compoundChebi:
        lines = compoundChebi.readlines()
        smilestr = []
        namestr = []
        for linea in lines:
            for lineaS in linea.split(">"):
                if lineaS == '<SMILES':
                    smile = linea.split("<")
                    smilestr = smile[1].split(">")
                if lineaS == '<SYNONYM':
                    name = linea.split('<')
                    namestr.append(name[1].split('>')[1])                                
        if len (smilestr) !=0:
            nameC = ''
            if len(namestr) == 2:
                nameC = namestr[0] + ' ' + namestr[1]
            else:
                if len(namestr) == 1:
                    nameC = namestr[0]
            resultado = archivo[:6]+ ';'+archivo[7:-4]+';'+smilestr[1] + ';' +nameC+'\n'
            csv_file.write(resultado)
                                
                            
                                
                                
            
                                    
