import math
import numpy as np
import random as rand
import os

if __name__ == '__main__':
    pop_size=200
    files = os.listdir("TSP Instances")
    for files in files:
        f = open("TSP Instances/{0}".format(files), "r")
        f.readline()
        f.readline()
        f.readline()
        n = int(f.readline().split(":")[1])
        f.readline()
        f.readline()
        cities = np.zeros((n,2))
        for i in range(n):
            cities[i] = f.readline().strip().split(" ")[1:]
        graph = np.zeros((n,n))
        for i in range (n-1):
            for j in range(i+1,n):
                graph[i][j] = int(math.sqrt((cities[i][0]-cities[j][0])**2+(cities[i][1]-cities[j][1])**2))
                graph[j][i] = graph[i][j]
        
        n = 10
        iSinM = 10
        limM = int(pop_size * .75)
        minVo = float("+inf")

        p = [[i for i in range(n)] for j in range(int(pop_size/2))]
        vo = [0 for i in range(pop_size)]
        vivos = [False for i in range(pop_size)]
        for i in range(len(p)):
            vivos[i] = True
            for j in range(n-1):
                it = rand.randint(j,n-1)
                temp = p[i][it]
                p[i][it] = p[i][j]
                p[i][j] = temp
        while(iSinM > 0):
            iSinM -= 1
            p.extend([[0 for i in range(n)] for j in range(int(pop_size/2))])
            for i in range(pop_size):
                if vivos[i] == False:
                    p1 = rand.randint(0, int(pop_size/2))
                    while (vivos[p1] == False):
                        p1 = rand.randint(0, int(pop_size/2))
                p2 = rand.randint(0, int(pop_size/2))
                while (vivos[p2] == False or p2 == p1):
                    p2 = rand.randint(0, int(pop_size/2))
                rani = rand.randint(0, n)
                ranf = rand.randint(0, n)
                while rani > ranf or rani == ranf:
                    if ranf == 0:
                        ranf = rand.randint(0, n-1)
                    rani = rand.randint(0, n-1)
                x = [0 for j in range(n)]
                for j in range (n):
                    p[i][j] = -1
                for j in range(rani, ranf):
                    p[i][j] = p[p1][j]
                    x[p[p1][j]] = 1
                k = 0
                for j in range(n):
                    while k < n and p[i][k] != -1:
                        k += 1
                    if x[p[p2][j]] == 0:
                        p[i][k] = p[p2][j]
                        k += 1
                vivos[i] = True
        for i in range(pop_size):
            vo[i] = 0
            for j in range(n-1):
                vo += graph[p[i][j]][p[i][j+1]]
            vo[i] += graph[p[i][n-1]][p[i][0]]
        if min(vo) < minVo:
            minVo = min(vo)
            iSinM = 10
        voprom = np.average
        contm = 0
        for i in range(pop_size):
            if vo[i] >= voprom:
                vivos[i] = False
                contm += 1
                if contm == limM:
                    break
    print('Archivo: {0} - Mejor Valor = {1}'.format(files, minVo))
                    