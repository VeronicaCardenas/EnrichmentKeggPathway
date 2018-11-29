from Protein import Protein
from heapq import nlargest
import csv, os
import time
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.DataStructs import FingerprintSimilarity
import directoryStructure

def getValuesSimilitudes (fingerPrint , fingerPrints):
    similitudes = []
    
    for fp in fingerPrints:
        similitude = getSimilitude (fingerPrint, fp)
        similitudes.append(similitude)
	
    return similitudes
    

def getSimilitude (a, b):
	resultado = 0
	if a != None and b !=None:
		resultado = FingerprintSimilarity(a,b,metric=DataStructs.TanimotoSimilarity)	
	return resultado
        
    
def writeProteins(compound, proteins):
    values = []
    dirResultadosTF = directoryStructure.resultadosTargetfishing 
    fileP = open(dirResultadosTF +'/'+compound.nameCompoundKegg+'.csv', 'w')
    maxValue = 0.9
    c3Value= 0.55
    firstLine = compound.nameCompoundKegg + ';' + compound.chemblid + ';'+compound.smile + ';'+compound.name
    fileP.write(firstLine)
    for protein in proteins:
        values = getValuesSimilitudes(compound.fingerPrint, protein.fingerPrints)
	tid = protein.tid
	gene = protein.gene
	targetType = protein.targetType
	prefName = protein.prefName
	accession = protein.accession
	infoProtein = str(tid) + ';'+str(gene)+';'+targetType+';'+prefName+';'+accession
        if len(values) >0:
            maxV = max(values)
            if len(values) >= 3:
                c3List= nlargest(3, values)
                c3 =  sum(c3List)/3
                if c3 >= c3Value or  maxV >=  maxValue:
                    fileP.write(infoProtein+";"+str(maxV)+";"+str(c3)+"\n")
