from Median import sortlistofnum

def mode(listofnum):
    listofsortednum = sortlistofnum(listofnum)
    dictofnum = {}
    for index in range(0, len(listofsortednum)):
        if((dictofnum.get(listofsortednum[index])) == None):
            dictofnum.update({listofsortednum[index]: 1})
        else:
            num = dictofnum.get(listofsortednum[index])
            num += 1
            dictofnum.update({listofsortednum[index]:num})
    return keywithmaxval(dictofnum)

def keywithmaxval(d):

    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


'''

from Median import sortlistofnum

def mode(listofnum):
    listofsortednum = sortlistofnum(listofnum)
    dictofnum = {}
    #print(listofsortednum)
    for index in range(0, len(listofsortednum)):
        #print(listofsortednum[index])
        if((dictofnum.get(listofsortednum[index])) == None):
            #print("item is not in dictionary \n",  dictofnum)
            dictofnum.update({listofsortednum[index]: 1})
            #print("dic item ", dictofnum)
        else:
            #print("item in dic ", dictofnum.get(listofsortednum[index]))
            num = dictofnum.get(listofsortednum[index])
            #print(num)
            num += 1
            dictofnum.update({listofsortednum[index]:num})
    print(dictofnum)

    #print(dictofnum)

'''