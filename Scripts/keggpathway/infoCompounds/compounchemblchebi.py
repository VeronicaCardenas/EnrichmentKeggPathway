import csv, os 
archivos = os.listdir('C:/Users/ASUS R454LA/Documents/EPN/Tesis/Compuestoshsa')
with open('C:/Users/ASUS R454LA/Documents/EPN/Tesis/Compuestossmileskegg/compounchemblchebi1Coment.csv', "w", newline = '') as csv_file:
    
    writer = csv.writer(csv_file, delimiter='\n')
    print (len(archivos))
    for archivo in archivos:
        chembl = ""
        chebi = ""
        nikkaji = ""
        dmet = ""
        comment = ""
        with open(archivo, 'r') as csvfile:
            if archivo != 'compounchemblchebi.py':
                lines = csvfile.readlines()
                for linea in lines:
                    for lineaS in linea.split():
                        if 'ChEMBL:' == lineaS:
                            chemblLine = linea.split()
                            chembl = chemblLine[1]
                        if 'ChEBI:' == lineaS:
                            chebiLine = linea.split()
                            chebi = chebiLine[1]
                        if 'NIKKAJI:' == lineaS:
                            nikkajiLine = linea.split()
                            nikkaji = nikkajiLine[1]
                        if '3DMET:' == lineaS:
                            dmetLine = linea.split()
                            dmet = dmetLine[1]
                        if 'COMMENT' == lineaS:
                            commentLine = linea.split()
                            comment = 'comment: ' + commentLine[1]
            
                            
                resultados = csvfile.name[:6]+";"+ chembl+";"+chebi + ";"+ nikkaji+ ";"+dmet + ";"+ comment
                writer.writerow([resultados])
                        
            

      
      
        
                
