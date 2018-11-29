import requests
import shutil
import os
import config
import directoryStructure

organism = config.organism
urlList = 'http://rest.kegg.jp/list/pathway/'
urlKgml = 'http://rest.kegg.jp/get/'
urlImage = 'https://www.genome.jp/kegg/pathway/'
directory = directoryStructure.keggpathway
dirImage = directoryStructure.keggpImage
dirkgml = directoryStructure.keggpKgml

pathways = requests.get(urlList + organism)
for line in pathways.text.split('\n'):
    pathwayid = line.split('\t')[0].replace('path:','')
    print(pathwayid)
    kgml = requests.get(urlKgml + pathwayid + '/kgml')
    image = requests.get(urlImage + organism + '/'+ pathwayid + '.png', stream=True)
    f = open(dirkgml + '/' + pathwayid + '.xml', 'w')
    f.write(kgml.content.decode("utf-8"))
    if image.status_code == 200:
        with open(dirImage + '/' + pathwayid + '.png', 'wb') as imageSave:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, imageSave)
    f.close
