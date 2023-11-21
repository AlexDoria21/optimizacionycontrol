import numpy
import random as rand

if __name__ == '__main__':
    n = 7 #tam de recorrido
    pop_size = 200 #tam de poblacion

    #region Pop vacia todos muertos
    p = [[i for i in range(n)] for j in range(int(pop_size/2))] #poblacion 0 a 99
    vo = [0 for i in range(pop_size)] #valor objetivo
    vivos = [False for i in range (pop_size)] #muertos de 0 a 199
    #endregion

    #region Randomizar mitad de pop a vivos
    for i in range(len(p)): #i de 0 a 99
        vivos[i] = True
        for j in range(n-1):
            it = rand.randint(j,n-1)
            temp = p[i][it]
            p[i][it] = p[i][j]
            p[i][j] = temp
    #endregion

    #region Cruzamiento
    p.extend([[0 for i in range(n)] for j in range(int(pop_size/2))])
    #llenar de 100 a 199 con -1
    for i in range(pop_size):
        if vivos[i] == False: #de 100 a 199
            #region Encontrar padres vivos
            p1 = rand.randint(0,int(pop_size/2)) #indice padre 1
            while(vivos[p1] == False):
                p1 = rand.randint(0, int(pop_size/2))
            p2 = rand.randint(0,int(pop_size/2))  #indice padre 2
            while(vivos[p2] == False or p2 == p1):
                p2 = rand.randint(0,int(pop_size/2))
            """
            for j in range(pop_size): #de 0 a 199
                if j == p1:
                    p1 = p[j] #valor padre 1
                if j == p2:
                    p2 = p[j] #valor padre 2
            """
            #endregion

            #region Encontrar rasgos padre 1
            rani = rand.randint(0, n) #inicio rango
            ranf = rand.randint(0, n) #fin rango
            while rani > ranf or rani == ranf:
                if ranf == 0:
                    ranf = rand.randint(0,n-1)
                rani = rand.randint(0,n-1)

            x = [0 for j in range(n)]
            """
            for j in list(range(rani,ranf)):
                p[i][j] = p1[j]
                for k in range(n):
                    if p1[j] == k:
                        x[k] = 1
            """
            for j in range(n):
                p[i][j] = -1
            for j in range(rani,ranf):
                p[i][j] = p[p1][j]
                x[p[p1][j]] = 1
            #endregion

            #region Rellenar resto rasgos padre 2
            """
            for j in range(n):
                if p[i][j] == -1:
                    for k in range(n):
                        if x[p[p2][k]] == 0:
                            p[i][j] = p[p2][k]
                            x[p[p2][k]] = 1
                            break
            """
            k = 0
            for j in range(n):
                while k < n and p[i][k] != -1:
                    k += 1
                if x[p[p2][j]] == 0:
                    p[i][k] = p[p2][j]
                    k += 1
            #endregion
            vivos[i] = True
    #endregion

    for e in enumerate(zip(p,vo,vivos)):
        print(e)