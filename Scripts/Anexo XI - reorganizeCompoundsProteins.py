import time, csv, os
from multiprocessing import Pool
import directoryStructure
import multiprocessing

dirResultadosTF = directoryStructure.resultadosTargetfishing
dirResultadosTFproteins = directoryStructure.resultadosTFProteins
dirProtein = directoryStructure.proteinsSmiles

if __name__ == '__main__':
    start_time = time.time()
    archivos = os.listdir(dirResultadosTF)
    archivosProtein = os.listdir(dirProtein)
    campounds = []
    proteinas = []
    proteinids = []
    compoundsOfProtein = []
    total= len(archivosProtein)
    i = 0;
    for archivoProtein in archivosProtein:
        proteins = open(dirProtein+'/'+archivoProtein, 'r')
        proteins = proteins.read()
        proteinid = archivoProtein.split(".")[0]
        infoProtein = proteins.split('\n')[0]
        proteinids.append(proteinid)
        file = open( dirResultadosTFproteins +'/'+ proteinid+'.csv', 'w')
        file.write(infoProtein+'\n')
        for archivo in archivos:
            compoundsTargeF = open(dirResultadosTF+'/'+ archivo, 'r')
            nameFile = archivo.split(".")[0]
            compound = nameFile
            campounds.append(compound)
            readcompoundsTargeF = compoundsTargeF.read()
            proteins = readcompoundsTargeF.split("\n")
            infoCompound = proteins[0].split(';')
            for proteinStr in proteins:
                proteinDatos = proteinStr.split(";")
                if proteinDatos[0] == proteinid and len(proteinDatos) >1:
                    resultado = compound+";"+infoCompound[1] + ";"+infoCompound[3]  +";"+proteinDatos[5]+";"+proteinDatos[6]+"\n"
                    file.write(resultado)
        i = i+1
        print("Avance " + str(i)+'/'+str(total))
        
