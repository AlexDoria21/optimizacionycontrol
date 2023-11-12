import MarketingCampain
def convertToInt(dataset,index):
    for row in dataset:
        if len(row[index]) != 0:
            row[index] = int(row[index])
        else:
            row[index] = 0

def OrdinalEncoding(dataset: object, dictionary: object, index: object) -> object:
    for row in dataset:
        row[index] = dictionary[row[index]]

def OneHotEncoding(dataset, cabecera, index):
    nombres = set()
    for row in dataset:
        nombres.add(row[index])
    nombres = list(nombres)
    cabecera[index:index+1] = nombres

    for row in dataset:
        temp = row[index]
        x = [0 for i in range(len(nombres))]
        for i in range(len(nombres)):
            if temp == nombres[i]:
                x[i] = 1
                break
        row[index: index+1] = x

def CutYear(dataset, index):
    for row in dataset:
        row[index] = int(row[index][-4:])


def ChangeText(dataset, OriginalText, NewText, index):
    for row in dataset:
        if row[index] == OriginalText:
            row[index] = NewText


def Normalizar(dataset,index):
    cols = list(zip(*dataset))
    maximo = max(cols[index])
    minimo = min(cols[index])
    for row in dataset:
        row[index] = round(5*(row[index]-minimo)/(maximo-minimo),2)

def Estandarizar(dataser,index):
    cols = list(zip(*dataset))
    xPrima = MarketingCampain.average(cols[index])
    sigma = MarketingCampain.std(cols[index])
    for row in dataset:
        row[index] = round((row[index] - xPrima)/sigma, 2)

def DelColumn(dataset, cabecera, index):
    del(cabecera[index])
    for row in dataset:
        row.pop(index)

if __name__ == "__main__":
    cabecera = []
    dataset = []
    archivo = open("marketing_campaign.csv", "r")
    for linea in archivo:
        linea = linea.strip().split(",")
        dataset.append(linea)
    archivo.close()
    cabecera = dataset.pop(0)

    dicccionario = {"Basic": 1, "PhD": 5, "Graduation": 3, "Master": 4, "2n Cycle": 2}
    OrdinalEncoding(dataset, dicccionario, 2)

    ChangeText(dataset, "Alone", "Single", 3)
    ChangeText(dataset, "Together", "Married", 3)


    enteros = [0, 1, 4, 5, 6]
    enteros.extend(list(range(8, 21)))
    for i in enteros:
        convertToInt(dataset, i)

    CutYear(dataset, 7)

    OneHotEncoding(dataset, cabecera, 3)

    DelColumn(dataset, cabecera, 0)

    #Normalizar la columna 1 (índice 1)
    Normalizar(dataset, 7)
    Normalizar(dataset, 8)
    Normalizar(dataset, 12)
    Normalizar(dataset, 13)
    Normalizar(dataset, 14)
    Normalizar(dataset, 15)
    Normalizar(dataset, 16)
    Normalizar(dataset, 18)

    #Estandarizar la columna 2 (índice 2)
    Estandarizar(dataset, 2)

    #     Supongamos que deseas contar elementos en la columna "Marital_Status" (cambia el nombre según tus datos)
    #    columna_marital_status = [fila[cabecera.index("Marital_Status")] for fila in dataset]

    #     Utiliza un conjunto (set) para obtener elementos únicos
    #    elementos_unicos = set(columna_marital_status)

    #    print(f"Elementos únicos en la columna 'Marital_Status': {elementos_unicos}")

    print(cabecera)
    for row in dataset:
        print(row)
    archivo = open("out.csv", "w")
    archivo.write(",".join(cabecera))
    archivo.write("\n")
    for row in dataset:
        for i in range(len(row)):
            row[i] = str(row[i])
        archivo.write(",".join(row))
        archivo.write("\n")
    archivo.close()