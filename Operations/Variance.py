from Mean import mean

def variance(listofnumbers):
    meanoflist = mean(listofnumbers)
    squaredDiff = []
    for item in listofnumbers:
        sub = (item - meanoflist)
        sub = sub**2
        squaredDiff.append(sub)
    meanofsquaredDiff = mean(squaredDiff) #reusing mean here to calculate the sum of squares
    sumofsquares = meanofsquaredDiff * len(squaredDiff)
    finalans = sumofsquares / ((len(listofnumbers))-1)
    return((finalans))

