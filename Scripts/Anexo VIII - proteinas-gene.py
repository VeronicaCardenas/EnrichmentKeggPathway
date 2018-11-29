import MySQLdb
import time, csv
import config
import directoryStructure


def connection ():
    db = MySQLdb.connect( host= config.host,
                          user= config.user,
                          passwd = config.password,
                          db=config.databaseChembl)
    cur = db.cursor()
    return cur;

def getProteins (geneL, cur):
    geneL = tuple(geneL)
    print (len(geneL))
    params = {'geneList': geneL}
    s= ('SELECT * FROM evoluniprot.uniprotdb where GENEID in  %(geneList)s')
    
    cur.execute(s, params)
    resultado = cur.fetchall()
    return resultado
    
if __name__ == '__main__':
    start_time = time.time()
    fileProtsGenes = directoryStructure.uniprot
    fileGenesId = directoryStructure.cleanInfoKegg+'/listGenesID.csv'
    fileToWriteG = open(fileProtsGenes+'/proteinas-genesKegg.csv', 'w')
    genesList = []
    with open (fileGenesId, 'r') as genes:
        spamreader = genes.read().split('\n')
        for gene in spamreader:
            if gene != '':
                gen = gene.split (':')[1]
                genesList.append(gen)
    
    cur = connection()
    proteinas = getProteins(genesList, cur)
    resultado = []
    for protein in proteinas:
        fileToWriteG.write(protein[0]+ ';'+protein[1]+ ';'+ protein[2]+ '\n')
    
    fileToWriteG.close()
    print (len(proteinas))
