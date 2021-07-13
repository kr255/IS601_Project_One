from Variance import variance

def StandDev(listofnumbers):
    varianceoflist = variance(listofnumbers)
    #print(varianceoflist**(1/2))
    return(varianceoflist**(1/2))