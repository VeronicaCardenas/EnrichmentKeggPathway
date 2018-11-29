import MySQLdb
import config

#   PROCESSING UNIPROT DATA FILES AND CREATING DATABASE

def ExtractAllWords(Line):
    TempWords = str(Line).split(' ')
    WordAll = []
    for word in TempWords:
        if word != '': WordAll.append(word)
    return (WordAll)
def ExtractSEQ(ListLines):
    Out = []
    for Lines in ListLines:
        Temp = ExtractAllWords(Lines)
        Temp = [item.split('\n')[0] for item in Temp]
        Out = Out+ Temp
    Out = ''.join(Out)
    return (Out)

def filterData(cur, temp0, temp1, temp2,temp3,temp4,temp5,temp6,temp7,temp8):
    add_register = ("INSERT INTO evoluniprotv1.UNIPROTDB "
               "(UNIPROTID, UNIPROTAC, GENEID, GO) "
               "VALUES (%s, %s, %s, %s)")

    if temp6 == 'Homo sapiens (Human).\n':
        temp2 = temp2.split(';')[0]
        data_register = (temp0, temp2, temp3,temp8)
        cur.execute(add_register, data_register)
        
    
def UniprotDataBaseHS_Create():
    global DatabaseName
    
    
    TABLES= (
        "CREATE TABLE `UNIPROTDB` ("
        "  `UNIPROTID` varchar(50),"
        "  `UNIPROTAC` TEXT,"        
        "  `GENEID` TEXT,"
        "  `GO` TEXT"        
        ")")
    db= MySQLdb.connect(host=config.host,passwd=config.password,user=config.user,db=DatabaseName) 
    cur = db.cursor()
    print("Creating table : UNIPROTDB_FILTERED")
    cur.execute(TABLES)
    print ('UNIPROTDB_FILTERED was created')


def UniprotDataBaseHS_ADD(UFile):

    global DatabaseName
    
    
    db= MySQLdb.connect(host=config.host,passwd=config.password,user=config.user,db="")  
    print("Adding records to table : UNIPROTDB_ALL")
    f = open(UFile,'r')

    Continue = False
    for Line in f:
        
        Line = str(Line)
        TempList = ExtractAllWords(Line)
       
        if TempList[0]=='ID':
            Continue = False
            Record_ID = []
            Record_AC = []
            Record_ST = []
            Record_GID = []
            Record_GO = []
            Record_OX = []
            Record_OC = []
            Record_OS = []
            Record_SEQ = []
            Record_ID.append(TempList[1])
            T = str(TempList[2]).split(';')[0]
            Record_ST.append(T)
        if TempList[0]=='AC':
            T = TempList[1:len(TempList)]
            T = ''.join(T)
            T = str(T).split('\n')[0]
            if T[len(T)-1] == ';': T = T[0:len(T)-1]
            Record_AC.append(T)
        if TempList[0]=='GeneID':
            T = str(str(TempList[1]).split(';')[0]).split('=')[1]
            Record_OX.append(T)
        if TempList[0]=='OS':
            
            T = TempList[1:len(TempList)]
            T = ' '.join(T)
            Record_OS.append(T)
        if TempList[0]=='OC':
           
            T = TempList[1:len(TempList)]
            T = ' '.join(T)
            Record_OC.append(T)
        if TempList[0]=='DR' and TempList[1]=='GeneID;':
            T= str(TempList[2]).split(';')[0]
            Record_GID.append(T)
        if TempList[0]=='SQ': Continue = True
        if Continue == True and TempList[0]!='SQ' and (Line[0]+Line[1])!='//': Record_SEQ.append(Line)      
        if TempList[0]=='DR' and TempList[1]=='GO;':
            T= str(TempList[2]).split(';')[0]
            Record_GO.append(T)
        if (Line[0]+Line[1])=='//':
            Continue = False
            Temp = []
            Temp.append(Record_ID[0])
            Temp.append(Record_ST[0])
            if len(Record_AC)>0:
                Temp.append(Record_AC[0])
            else:
                Temp.append('')
            if len(Record_GID)>0:
                Temp.append(Record_GID[0])
            else:
                Temp.append('')
            if len(Record_OX)>0:
                Temp.append(Record_OX[0])
            else:
                Temp.append('')
            if len(Record_OC)>0:
                Temp.append(''.join(Record_OC))
            else:
                Temp.append('')
            if len(Record_OS)>0:
                Temp.append(''.join(Record_OS))
            else:
                Temp.append('')
            if len(Record_SEQ)>0:
                T = ExtractSEQ(Record_SEQ)
                Temp.append(T)
            else:
                Temp.append('')
            if len(Record_GO)>0:
                Temp.append(';'.join(Record_GO))
            else:
                Temp.append('')
            cur = db.cursor()
            filterData(cur, Temp[0], Temp[1], Temp[2],Temp[3],Temp[4],Temp[5],Temp[6],Temp[7],Temp[8])
            db.commit()
            
    f.close
    print ('File Processed')
        
#   Main program UniprotDB_ALL.py       

if __name__ == '__main__':
    
    dirSprotDat = config.basedir + 'resources/uniprot_sprot.dat'
    DatabaseName = 'evoluniprot'
    SprotFile = dirSprotDat
    UniprotDataBaseHS_Create()
    UniprotDataBaseHS_ADD (SprotFile)
    print ('SWI Processed')
                
               
