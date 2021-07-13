import Addition
#
# def addemup(s1, s2, s3=[]):
#     print("s1 ", s1)
#     print("s2 ", s2)
#     s3.append(Addition.addition(s1[0], s2[0]))
#     return s3
#
# def meanCalulation(listofnum):
#     n = len(listofnum)
#     #print("length of list", len(listofnum))
#     if n < 2:
#         return
#     else:
#         mid = n // 2
#         leftlist = listofnum[0:mid]
#         print("left ", leftlist)
#         rightList = listofnum[mid:n]
#         print("right ", rightList)
#         meanCalulation(leftlist)
#         meanCalulation(rightList)
#         #addthemup()
#
#     # if(len(listofnum) == 0):
#     #     return 0
#     # if(len(listofnum) < 2):
#     #     return listofnum[0]
#     # if (len(listofnum) == 2):
#     #     print("len == 2", Addition.addition(listofnum[0], listofnum[1]))
#     #     return Addition.addition(listofnum[0], listofnum[1])
#     # else:
#     #     print(listofnum, " ", len(listofnum), "end ")
#     #     ans= ((meanCalulation(listofnum[low:mid], low, mid) +\
#     #            meanCalulation(listofnum[mid:high], mid, high)))
#     # print(ans)

def meanCalculation(listofnum):
    ans = 0.0
    for elem in listofnum:
        ans += elem
    return ans/len(listofnum)

def mean(listofnumbers):
    return (meanCalculation(listofnumbers))


