from random import randint, gauss
# generate some integers

def noseedgenerator(a, b):
    for i in range(a,b):
        #valueint = randint(a, b)
        valuedec = gauss(a, b)

    return (int(valuedec), valuedec)


def seedgenerator(a, b, seed):
    seed(seed)
    for i in range(a, b):
        #valueint = randint(a, b)
        valuedec = gauss(a, b)

    return (int(valuedec), valuedec)

def seedgeneratorlist(a, b, seed):
    seed(seed)
    listofstuff=[]
    for i in range(a, b):
        #valueint = randint(a, b)
        valuedec = gauss(a, b)
        listofstuff.append(int(valuedec))
        listofstuff.append((valuedec))


    return (int(valuedec), valuedec)