import os
import config

basedir = config.basedir
directories = []
# directories kegg
keggpathway = basedir + '/keggpathway'
directories.append(keggpathway)

keggpKgml = basedir + '/keggpathway/kgml'
directories.append(keggpKgml)

cleanInfoKegg = basedir + '/keggpathway/cleanInfoKegg'
directories.append(cleanInfoKegg)

keggCompounds = basedir + '/keggpathway/infoCompounds'
directories.append(keggCompounds)

# directories chembl
chembl = basedir + '/chembl'
directories.append(chembl)


# directories chebi
chebi = basedir + '/chebi'
directories.append(chebi)

genericSmilesChebi = basedir + '/chebi/genericSmiles'
directories.append(genericSmilesChebi)

# directories uniprot
uniprot = basedir + '/uniprot'
directories.append(uniprot)

proteinsSmiles = basedir + '/uniprot/proteinsSmiles'
directories.append(proteinsSmiles)

#directories targetFishing

targetfishing = basedir + '/targetfishing'
directories.append(targetfishing)

resultadosTargetfishing = basedir + '/targetfishing/resultadosTF'
directories.append(resultadosTargetfishing)

resultadosTFProteins = basedir + '/targetfishing/resultadosTFproteins'
directories.append(resultadosTFProteins)


for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)
