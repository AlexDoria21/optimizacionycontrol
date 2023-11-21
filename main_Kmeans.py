import numpy
import random

def maxMin(dsT):
    maxim = []
    minim = []
    for i in dsT:
        maxim.append((max(i)))
        minim.append((min(i)))
    return maxim,minim

def updtCent(dataset, grupos, cent):
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            cent[i][j] = 0
        cont[i] = 0
    for i in range(len(grupos)):
        for j in range(len(dataset[i])):
            cent[grupos[i]][j] += dataset[i][j]
        cont[grupos[i]] += 1
    for i in range(len(cent)):
        for j in range(len(cent[i])):
            cent[i][j] /= cont[i]

def calcDist(point, cent):
    total = 0
    for i in range(m):
        total += (point[i] - cent[i]) ** 2
    return total

def calcGrupos(datas, cent, grupos):
    c = False
    for ip in range(n):
        distMin = float("+inf")
        indexMin = float("+inf")
        for ic in range(len(cent)):
            dist = calcDist(datas[ip], cent[ic])
            if dist < distMin:
                distMin = dist
                indexMin = ic
        if grupos[ip] != indexMin:
            c = True
            grupos[ip] = indexMin
    return c

if __name__ == '__main__':
    datas = []
    k = 7

    file = open("Absenteeism_out.csv", "r")
    for l in file:
        e = l.strip().split(',')
        datas.append(e)
    head = datas.pop(0)
    n = len(datas)
    m = len(head)
    for i in range(n):
        for j in range(m):
            datas[i][j] = float(datas[i][j])
    dsT = list(zip(*datas))

    cent = [[0 for i in range(n)] for j in range(k)]
    grupos = [0 for i in range(n)]
    cont = [0 for i in range(k)]

    maxim, minim = maxMin(dsT)
    for i in range(k):
        for j in range(m):
            cent[i][j] = random.uniform(minim[j],maxim[j])

    c = True
    while c:
        c = calcGrupos(datas, cent, grupos)
        updtCent(datas, grupos, cent)

    prom = [0 for i in range(k)]

    for i in range(n):
        prom[grupos[i]] += calcDist(datas[i],cent[grupos[i]])
        cont[grupos[i]] += 1

    for i in range(k):
        if cont[i] != 0:
            prom[i] = prom[i]/cont[i]

    promGlobal = numpy.average(prom)

    print(f'Promedio Global a {k} k = ', promGlobal)
    #for i in enumerate(grupos):
        #print(i)
