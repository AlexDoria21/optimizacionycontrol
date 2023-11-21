import numpy

def ColtoInt(datas,index):
    for row in datas:
        if len(row[index])!=0:
            row[index] = int(row[index])
        else:
            row[index] = 0


def ColtoFloat(datas,index):
    for row in datas:
        row[index] = float(row[index])

def Ordinal(datas,dict,index):
    for row in datas:
        row[index] = dict[row[index]]

def OneHot(datas,head,index):
    names = set()
    for row in datas:
        names.add(row[index])
    names = list(names)
    head[index:index+1] = names
    for row in datas:
        temp = row[index]
        x = [0 for i in range(len(names))]
        for i in range(len(names)):
            if temp == names[i]:
                x[i] = 1
                break
        row[index:index+1] = x

def CutYear(datas,index):
    for row in datas:
        row[index] = int(row[index][0:4])

def SwapTxt(datas,old,new,index):
    for row in datas:
        if row[index] == old:
            row[index] = new

def DelCol(datas,head,index):
    del(head[index])
    for row in datas:
        del(row[index])

def Norm(datas,index):
    cols = list(zip(*datas))
    maximo = max(cols[index])
    minimo = min(cols[index])
    for row in datas:
        row[index] = round(5*(row[index]-minimo)/(maximo-minimo), 2)

def Esta(datas,index):
    cols = list(zip(*datas))
    xPrima = numpy.average(cols[index])
    sigma = numpy.std(cols[index])
    for row in datas:
        row[index] = round((row[index]-xPrima)/sigma, 2)

if __name__ == '__main__':
    file = open("marketing_campaign.csv", "r")
    datas = []
    for line in file:
        line = line.strip().split(";")
        datas.append((line))
    file.close()
    head = datas.pop(0)
    CutYear(datas,7)
    e = [0,1,4,5,6]
    e.extend(list(range(8,29)))
    for i in e:
        ColtoInt(datas,i)
    dicc = {"Basic":1,"PhD":5,"Graduation":3,"Master":4,"2n Cycle":2}
    Ordinal(datas,dicc,2)
    SwapTxt(datas,"Alone","Single",3)
    SwapTxt(datas,"Together","Married",3)
    N = [1, 4, 5]
    N.extend(list(range(7, 19)))
    for i in N:
        Norm(datas, i)
    OneHot(datas,head,3)
    DelCol(datas,head,0)
    print(head)
    for row in datas:
        print(row)
    archivo = open('out.csv', 'w')
    archivo.write(','.join(head))
    archivo.write("\n")
    for row in datas:
        for r in range(len(row)):
            row[r] = str(row[r])
        archivo.write(','.join(row))
        archivo.write('\n')
    archivo.close()