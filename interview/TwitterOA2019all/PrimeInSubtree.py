#PrimesInSubtree
def isPrime(value):
   if value == 1: return False
   if value == 2 or value == 3: return True
   if value%2 == 0: return False
   i = 2
   while i*i<=value:
       if value%i == 0: return False
       i+=1
   return True


def primeQuery(number, starts, ends, values, queries):
    countDict = [None]*number
    indexDict = [None]*number

    for i in range(number):
        countDict[i] = 1 if isPrime(values[i]) else 0
    for i in range(number):
        indexDict[i] = i
    for i in range(len(starts)):
        ind = ends[i]-1
        ptr = starts[i]-1
        indexDict[ind] = ptr

    for i in range(number):
        temp = i
        while indexDict[temp] != temp:
            temp = indexDict[temp]
            countDict[temp] += countDict[i]
    res = [None]*len(queries)
    for i in range(len(queries)):
        res[i] = countDict[queries[i]-1]
    return res

def printList(resList):
    for i in resList:
        print(str(i) + " ")


if __name__ == '__main__':
    # testcase 1
    n = 6;
    startNodes = [1, 2, 2, 1, 3] # 5 edges
    endNodes = [2, 4, 5, 3, 6] # size: 5
    values = [2, 2, 6, 5, 4, 3] # size: 6
    queries = [1, 4, 5, 6, 2] # size: 5
    printList(primeQuery(n, startNodes, endNodes, values, queries))
    # 4 1 0 1 2
