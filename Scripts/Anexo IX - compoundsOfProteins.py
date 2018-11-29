import MySQLdb
import time
import csv
import config
import directoryStructure

def connection ():
    db = MySQLdb.connect(host=config.host,
                         user=config.user,
                         passwd=config.password,
                         db=config.databaseChembl)
    cur = db.cursor()
    return cur;

def getProteins(proteinsA, cur):
    proteinsA = tuple(proteinsA)
    params = {'proteinsList':proteinsA}
    
    s= ('Select * from chembl_simplified.protein where accession in %(proteinsList)s')

    cur.execute(s,params)
    resultado = cur.fetchall()
    return resultado

def getCompounds(idProtein, cur):
    
    s= ('select canonical_smiles from compound where molregno in ('
        'select molregno from data_experimental where tid = %(tid)s)')

    cur.execute(s, { 'tid': idProtein })
    resultado = cur.fetchall()
        #print (resultado)
    return resultado

if __name__ == '__main__':
    
    start_time = time.time()
    proteinsIds = []
    proteinsInfo = []
    fileProteinsGenes = directoryStructure.uniprot
    dirProteinsSmiles = directoryStructure.proteinsSmiles
    with open (fileProteinsGenes + '/proteinas-genesKegg.csv', 'r') as proteins:
        spamreader = proteins.read().split('\n')
        for protein in spamreader:
            if protein != '':
                prot = protein.split (';')
                proteinsInfo.append(prot)
                proteinsIds.append(prot[1])
                
                
    cur = connection()
    proteinsChembl = getProteins(proteinsIds, cur)
    
    print (len(proteinsChembl))
    total= len(proteinsChembl)
    i = 0
    for protein in proteinsChembl:
        
        tid = protein[0]
        targetType = protein [1]
        prefName= protein[2]
        accesion = protein[9]
        gene = list (filter(lambda gene: gene[1] == accesion, proteinsInfo))
        
        gene =gene[0][2]
        nameFile = str(tid)
        firstLine = str(tid)+'_'+gene+'_'+targetType+'_'+ prefName+'_'+accesion
        name= dirProteinsSmiles +'/'+ nameFile+ '.csv'
        compounds = getCompounds(tid, cur)

        if len(compounds) != 0:
            f = open(name, 'w')
            f.write(firstLine+'\n')    
            for compound in compounds:
                #print(compound[0])
                f.write(compound[0]+'\n')
        i = i+1
        print ('Avance: '+ str(i) + '/' +str(total))
    print (time.time() - start_time)
    	
