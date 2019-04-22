#NoPairsAllowed
def minimalOperations(inpList):
    res = []
    for i in range(len(inpList)):
        op = 0
        char = inpList[i][0]
        count = 1
        for j in range(1,len(inpList[i])):
            if inpList[i][j] == char:
                count += 1
            else:
                op += count/2
                count = 1
            char = inpList[i][j]
        if count > 1:
            op += count/2
        res.append(op)
    return res

def printList(resList):
    for i in resList:
        print(i)

if __name__ == '__main__':
    # testcase1
    input1 = ["ab", "aab", "abb", "abab", "abaaaba"]
    printList(minimalOperations(input1));
    # 0 1 1 0 1
    '''
    # testcase2
    input2 = ["add", "boook", "break"]
    printList(minimalOperations(input2));
    # 1 1 0
    '''
