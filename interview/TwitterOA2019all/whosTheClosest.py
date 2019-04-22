# who's the closest
def closest(s, indexes):
    unionS = set(s)
    dic = {}
    for char in unionS:
        charInd = [i for i in range(len(s)) if s.startswith(char, i)]
        dic[char] = charInd
    res = []
    for ind in indexes:
        checkChar = s[ind]
        #print(checkChar)
        checkList = dic[checkChar]
        if len(checkList) > 1:
            indInd = checkList.index(ind)
            beforeDiff, afterDiff = float('inf'), float('inf')
            if indInd-1 >=0:
                beforeDiff = ind - checkList[indInd-1]
            if indInd+1 < len(checkList):
                afterDiff = checkList[indInd+1]-ind
            if afterDiff < beforeDiff:
                res.append(str(checkList[indInd+1]))
            else:
                res.append(str(checkList[indInd-1]))
        else:
            res.append('-1')
    return res

def printArray(array):
    for i in array:
        print(i)

if __name__ == '__main__':
    '''
    # testcase 1
    test1 = "babab"
    index1 = [2]
    printArray(closest(test1, index1))
    # 0
    '''
    # testcase 2
    test2 = "hackerrank"
    index2 = [4, 1, 6, 8]
    printArray(closest(test2, index2))
    # -1 7 5 -1
