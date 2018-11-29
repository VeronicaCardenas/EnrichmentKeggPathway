import json
import csv
import requests
import directoryStructure
from urllib.request import  Request, urlopen, urlretrieve

dirInfoCompounds = directoryStructure.cleanInfoKegg + '/compoundIDdataBases.csv'
dircanSmiles = directoryStructure.chembl + '/canonicalSmiles.csv'
chebiDir = directoryStructure.genericSmilesChebi

file =  open(dirInfoCompounds, 'r')
spamreader = file.read().split('\n')
compoundSmileIdchembl = open(dircanSmiles, "w")
chemblId = ''
cheid = ''
name = ''
smile= ''
for row in spamreader:
    rowArray = row.split(';')
    resultado=[]
    if rowArray[2] != '':
        conection = requests.get('https://www.ebi.ac.uk/chembl/api/data/molecule/' + rowArray[2]+ '.json', timeout=None)
        texto = conection.content.decode("utf-8")
        try:
            compound = json.loads(texto)
            if compound['molecule_structures'] != None:
                smile = compound['molecule_structures']['canonical_smiles']
                chemblId = compound['molecule_chembl_id']
                resultado = rowArray[0]+";"+chemblId+';'+ smile +';'+rowArray[1]
                print (resultado)
                compoundSmileIdchembl.write(resultado + '\n')
        except:
            continue
        
    else:
        if rowArray[3] != '':
            url = "http://www.ebi.ac.uk/chebi/saveStructure.do?xml=true&chebiId="+ rowArray[3]+"&imageId=0"
            savein = chebiDir + '/' +rowArray[0]+"-"+rowArray[3] + ".xml"
            urlretrieve(url, savein)

compoundSmileIdchembl.close()
                
                    
                



            
            
