import numpy as np

def ColtoInt(datas, index):
    for row in datas:
        if len(row[index]) != 0:
            row[index] = int(row[index])
        else:
            row[index] = 0

def ColtoFloat(datas, index):
    for row in datas:
        row[index] = float(row[index])

def Ordinal(datas, dict, index):
    for row in datas:
        row[index] = dict[row[index]]

def OneHot(datas, head, index):
    names = set()
    for row in datas:
        names.add(row[index])
    names = list(names)
    head[index:index + 1] = names
    for row in datas:
        temp = row[index]
        x = [0 for i in range(len(names))]
        for i in range(len(names)):
            if temp == names[i]:
                x[i] = 1
                break
        row[index:index + 1] = x

def CutYear(datas, index):
    for row in datas:
        row[index] = int(row[index][0:4])

def SwapTxt(datas, old, new, index):
    for row in datas:
        if row[index] == old:
            row[index] = new

def DelCol(datas, head, index):
    del head[index]
    for row in datas:
        del row[index]

def Norm(datas, index):
    cols = list(zip(*datas))
    maximo = max(cols[index])
    minimo = min(cols[index])
    for row in datas:
        row[index] = round(5 * (row[index] - minimo) / (maximo - minimo), 2)

def Esta(datas, index):
    cols = list(zip(*datas))
    xPrima = np.average(cols[index])
    sigma = np.std(cols[index])
    for row in datas:
        row[index] = round((row[index] - xPrima) / sigma, 2)

def read_data(file_path):
    datas = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip().split(",")
            if i == 0:  # Header line, leave as is
                datas.append(line)
            else:
                datas.append([int(value) if value.isdigit() else value for value in line])
    return datas

if __name__ == '__main__':
    file = open("survey lung cancer.csv", "r")
    datas = []
    for line in file:
        line = line.strip().split(",")
        datas.append(line)
    file.close()
    head = datas.pop(0)

    # Realiza las transformaciones necesarias para tu conjunto de datos
    # Por ejemplo, para convertir la columna 'AGE' a entero:
    ColtoInt(datas, 1)

    # Convierte 'GENDER' a valores numéricos (M -> 0, F -> 1)
    for row in datas:
        if row[0] == 'M':
            row[0] = 0
        elif row[0] == 'F':
            row[0] = 1

    # Convierte 'LUNG_CANCER' a valores numéricos (NO -> 0, YES -> 1)
    for row in datas:
        if row[-1] == 'NO':
            row[-1] = 0
        elif row[-1] == 'YES':
            row[-1] = 1

    # Continúa con las transformaciones necesarias para tu conjunto de datos

    # Guarda los datos procesados en un nuevo archivo CSV
    with open('doria_data.csv', 'w') as archivo:
        archivo.write(','.join(head))
        archivo.write("\n")
        for row in datas:
            for r in range(len(row)):
                row[r] = str(row[r])
            archivo.write(','.join(row))
            archivo.write('\n')
    
    # Imprime los datos tratados
    print("Datos tratados:")
    print(','.join(head))
    for row in datas:
        print(','.join(map(str, row)))
