def convertToInt(dataset,index):
    for row in dataset:
        if len(row[index]) != 0:
            row[index] = int(row[index])
        else:
            row[index] = 0

def convertToFloat(dataset,index):
    for row in dataset:
        if len(row[index]) !=0:
            row[index] = float(row[index])
        else:
            row[index]  = 0

dataset = []
#cabecera = []

archivo = open("survey lung cancer.csv", "r")
for linea in archivo:
    linea = linea.strip().split(",")
    print(linea)
