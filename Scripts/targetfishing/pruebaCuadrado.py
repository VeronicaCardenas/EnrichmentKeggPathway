import time
import math


def calculateLines(lines,partialArea,x,nucleo,total):
    
    x1= partialArea
    x1 = math.ceil(x1)

    if int(x) == int(nucleo):
        x1 = total
    return x1
    

def calcularAreas(compoundLen, nucleos):

    resultados = []
    resultadosC = []
    compoundLen = int(compoundLen)

    partialArea =int(compoundLen/nucleos)
    firstLines = math.ceil(partialArea)
    #print(math.ceil(firstLines))
    resultados.append(math.ceil(firstLines))
    lines = int(firstLines)
    y= 0
    resultado = 0


    for x in range (2, nucleos+1):
        nucleo = nucleos
        y= resultado+y
        resultado = calculateLines(lines+y,partialArea,x,nucleo,compoundLen)
        #print("Archivo len : "+ str(x))
        x = x+1
        resultados.append(resultado)
        resultados = sorted(resultados)

    inicial = 0
    for i in range(0,len(resultados)):
        inicial = resultados[i] + inicial
        if inicial > compoundLen:
            inicial = compoundLen
        resultadosC.append(inicial)
    return resultadosC



