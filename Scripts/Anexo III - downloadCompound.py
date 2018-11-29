import csv, requests
import directoryStructure

dirCompounds = directoryStructure.keggCompounds
listCompoundID = directoryStructure.cleanInfoKegg + '/listCompoundsID.csv'

with open( listCompoundID, 'r') as csvfile:
  spamreader = csv.reader(csvfile, delimiter='\n')
  for row in spamreader:
        compoundID = row[0][0:6]
        txt = requests.get('http://rest.kegg.jp/get/' + compoundID)
        f = open(dirCompounds + '/' + compoundID[0:6] + '.txt', 'w')
        f.write(txt.content.decode("utf-8"))
        f.close
                
