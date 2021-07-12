import Addition
'''

wtf was i thinking, turning binary seach into a mean algorithm on the day its due

'''
def meanCalulation(listofnum, lows, highs):
    #print(listofnum)
    #print("1 ", lows, highs)
    low = lows
    high = highs
    mid = (low + high) // 2
    #print("2 ", low, mid, high)
    #print("length of list", len(listofnum))
    if(len(listofnum) < 2):
        return listofnum[0]
    if (len(listofnum) == 2):
        #print("len == 2", Addition.addition(listofnum[0], listofnum[1]))
        return Addition.addition(listofnum[0], listofnum[1])
    else:
        #print(listofnum, " ", len(listofnum), "end ")
        ans= ((meanCalulation(listofnum[low:mid], low, mid) +\
               meanCalulation(listofnum[mid:high], low, mid)))
    return(ans)

def mean(listofnumbers):
    return meanCalulation(listofnumbers, 0, len(listofnumbers))/len(listofnumbers)


