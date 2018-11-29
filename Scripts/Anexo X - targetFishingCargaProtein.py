import time, csv, os
from Protein import Protein
from Compound import Compound
from getNumberCompounds import calcularAreas
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.DataStructs import FingerprintSimilarity
from targetFishingRdkitFiles import writeProteins
from multiprocessing import Pool
import multiprocessing
from rdkit.Chem import AllChem
import directoryStructure

def printS(compounds, proteins, rangoi, rangof):
    for i in range(rangoi, rangof):
        fingerPrint = compounds[i]
	if fingerPrint != None:
		compoundName = compounds[i].nameCompoundKegg
		writeProteins(compounds[i], proteins)


def cargarCompounds(line):
    print(line)
    comp = line.split(";")
    fingerPrint = getFingerPrint(comp[2])
    compound = Compound(comp[0], comp[1], comp[2], fingerPrint, comp[3])
    return compound

def getFingerPrint (smile):
    sanit = Chem.MolFromSmiles(smile,False)
    a = None
    try:
        Chem.SanitizeMol(sanit)
        m = Chem.MolFromSmiles(smile)
        a = AllChem.GetMorganFingerprintAsBitVect(m,2)
    except ValueError:
        a= None
    return a

def getFingerPrints (smiles):
    fingerPrints = []
    
    for i in range(1, len(smiles)) :
        fingerPrint = getFingerPrint(smiles[i])
        fingerPrints.append(fingerPrint)
    return fingerPrints

if __name__ == '__main__':
    start_time = time.time()
    dirProteinSmiles = directoryStructure.proteinsSmiles
    archivos = os.listdir(dirProteinSmiles)
    fileCanonicalSmiles = open (directoryStructure.chembl + '/canonicalSmiles.csv', 'r')
    canonicalSmiles = fileCanonicalSmiles.read()
    fileGenericSmiles = open (directoryStructure.chebi + '/compoundGenericSmiles.csv', 'r')
    genericSmiles = fileGenericSmiles.read()[:-1]
    smiles = canonicalSmiles + genericSmiles
    smiles = smiles.split('\n')
    proteins =[]
    i = 0
    
    pool = Pool(processes=4)
    compounds = pool.map(cargarCompounds, smiles, 4)
    print ("compoundsTotales")
    print (len(compounds))
    for archivo in archivos:
        compoundsOfSmile = open(dirProteinSmiles+'/'+ archivo, 'r')
        readCompoundsOfSmile = compoundsOfSmile.read()
	smiles = readCompoundsOfSmile.split ('\n')
	proteinInfo = smiles[0].split('_')
        tid = proteinInfo[0]
	gene = proteinInfo [1]
	targetType = proteinInfo[2]
	prefName = proteinInfo[3]
	accession = proteinInfo[4][:-1]
	fingerPrints = getFingerPrints (smiles)
	protein = Protein(tid, gene, targetType, prefName, accession, fingerPrints)
	proteins.append(protein)

    print ("Carga completa de proteinas y fingerPrints")
    print ("Empieza calculo similitud tanimoto max = 0.9, c3 = 0.55")

    cores = 4;
    totalArchivos = len(compounds)
    print (totalArchivos)
    limitesFinal = calcularAreas(totalArchivos,cores)
    print(limitesFinal)
    limiteInicial = limitesFinal

    for core in range(1,cores+1):
        if core == 1:
            process = multiprocessing.Process ( target=printS, args=( compounds, proteins,int(0),int(limitesFinal[core-1]),))
        else:
            process = multiprocessing.Process ( target=printS, args=( compounds, proteins, int(limiteInicial[core-2]) ,int(limitesFinal[core-1]),))
        process.start()

    print (time.time() -start_time)




        
