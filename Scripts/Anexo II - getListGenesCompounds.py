import csv, os, xml.etree.cElementTree as ET
import config
import directoryStructure

dirPathways = directoryStructure.keggpKgml
cleanInfoKegg = directoryStructure.cleanInfoKegg

files = os.listdir(dirPathways)
fileGenes = open(cleanInfoKegg + '/listGenesPathway.csv', 'w')
fileCompounds = open( cleanInfoKegg + '/listCompoundsPathway.csv', 'w')

fileGeneID = open(cleanInfoKegg + '/listGenesID.csv', 'w')
fileCompoundID = open(cleanInfoKegg + '/listCompoundsID.csv', 'w')


resultados = []
resultadosUnicos = []
resultadosUnicosC = []
setGenes = set()
setCompounds = set()

def writeFiles (list, type):
    if type == 'gene':
        for listItem in list:
            fileGeneID.write(listItem+'\n')
    else:
        for listItem in list:
            fileCompoundID.write(listItem+'\n')

for file in files:
         
    tree = ET.ElementTree(file=dirPathways +'/'+file)
    root = tree.getroot()
                    
    for entry in root.findall('entry'):
        type = entry.get("type")
        nameEntry = entry.get("name")        
        if (nameEntry == None):
            nameEntry=''
        
        if type == "compound" or type == "gene":
            for graphics in entry.findall("graphics"):
                name = graphics.get("name")
                nameCorrect =name.find('...')
                nameTotal = nameEntry
                namesEntry = nameEntry.split(" ")

                if nameCorrect != -1:
                    name = name[:nameCorrect] 
                if type == "gene":
                    reaction = ''
                    if entry.get("reaction") != None:
                        reaction = entry.get("reaction")
                    genes = nameTotal +';'+name + ';' +file[:-4]+'\n' 
                    fileGenes.write(genes)
                else:
                    compounds = name + ';' +file[:-4]+'\n'
                    fileCompounds.write(compounds)

                for nameEntry in namesEntry:
                    resultados = [nameEntry]
                    for resultados in resultados:
                        
                        if type == 'gene':
                            setGenes.add(resultados)
                           
                        else:
                            setCompounds.add(name)    
writeFiles(setGenes,'gene')
writeFiles(setCompounds,'compound')

fileGenes.close()
fileCompounds.close()
fileGeneID.close()
fileCompoundID.close()
