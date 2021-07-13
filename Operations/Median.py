from Operations import Addition


def sortlistofnum(listofnum):
    list.sort(listofnum)
    return listofnum

def median(listofnumbers):
    listofsortednum = sortlistofnum(listofnumbers)
    n = len(listofsortednum)
    novertwo = n // 2
    if(n%2 == 0):
        m = novertwo - 1
        middle = Addition.addition(listofsortednum[m], listofsortednum[novertwo])
        return middle/2
    else:
        return listofsortednum[n // 2]
