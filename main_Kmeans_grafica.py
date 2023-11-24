import matplotlib.pyplot as plt
import random

def centInic(dsT, k):
    c = [[0 for i in range(len(dsT))] for j in range(k)]
    for e in range(k):
        c[e] = [round(random.uniform(min(dsT[0]), max(dsT[0])), 2),
                round(random.uniform(min(dsT[1]), max(dsT[1])), 2)]
    return c


def graph(dsT, grupos, cent):
    gColor = [e * 50 for e in grupos]
    fig, ax = plt.subplots()
    ax.scatter(dsT[0], dsT[1], c=gColor)
    cT = list(zip(*cent))
    ax.scatter(cT[0], cT[1], c='red')
    plt.show()
    plt.close()


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
    for i in range(len(point)):
        total += (point[i] - cent[i]) ** 2
    return total


def calcGrupos(datas, cent, grupos):
    c = False
    for ip in range(len(datas)):
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
    file = open("doria_data.csv", "r")
    datas = []
    origG = []
    k = 3
    for line in file:
        e = line.strip().split('\t')
        for i in range(len(e)):
            e[i] = float(e[i])
        origG.append(int(e.pop(2)))
        datas.append(e)
    dsT = list(zip(*datas))
    cent = centInic(dsT, k)

    cont = [0 for i in range(k)]
    grupos = [0 for i in datas]

    graph(dsT,origG,cent)

    c = True
    while c:
        c = False
        c = calcGrupos(datas, cent, grupos)
        updtCent(datas, grupos, cent)
        graph(dsT, grupos, cent)




