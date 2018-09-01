#MissingWords
def missingWords(s, t):
    sList = s.split(' ')
    tList = t.split(' ')
    res = []
    sInd, tInd = 0, 0
    while tInd < len(tList):
        tWord = tList[tInd]
        while sInd < len(sList):
            sWord = sList[sInd]
            if sWord == tWord:
                tInd += 1
                sInd += 1
                break
            else:
                res.append(sWord)
                sInd += 1
    while sInd < len(sList):
        res.append(sList[sInd])
        sInd += 1
    return res

str1 = "I am using HackerRank to improve programming"
str2 = "am HackerRank to improve"
for missStr in missingWords(str1, str2):
    print(missStr)
