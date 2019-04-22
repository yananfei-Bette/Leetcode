#Simple Text Queries
def textQueries(sentences, phrases):
    sentenceList = []
    for sentence in sentences:
        words = sentence.split(' ')
        dic = {}
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        sentenceList.append(dic)
    #print(sentenceList)
    #print('******************')
    
    res = []
    for phrase in phrases:
        words = phrase.split(' ')
        stenceInd = ''
        for ind, sentenceDic in enumerate(sentenceList):
            minCount = float('inf')
            for word in words:
                #print(word)
                if word in sentenceDic:
                    minCount = min(minCount, sentenceDic[word])
                else:
                    minCount = float('inf')
                    break
                #print(minCount)
            while minCount != float('inf') and minCount > 0:
                stenceInd += (str(ind) + ' ')
                minCount -= 1
            #print(stenceInd)
        if not stenceInd:
            stenceInd += '-1'
        #print(stenceInd)
        res.append(stenceInd)
    return res

def printList(resList):
    for res in resList:
        print(res)
        #pass
    

if __name__ == "__main__":
    #testcase 1
    sentences1 = ["bob and alice like to text each other", "bob does not like to ski", "alice likes to ski"]
    phrases1 = ["bob alice", "alice", "like"]
    printList(textQueries(sentences1, phrases1))
    # 0, 0 2, 0 1
    
    #testcase 2
    sentences2 = ["jim likes mary", "kate likes tom", "tom does not like jim"]
    phrases2 = ["jim tom", "likes"]
    printList(textQueries(sentences2, phrases2))
    # 2, 0 1

    #testcase 3
    sentences3 = ["how it was done", "are you how", "it goes to", "goes done are it"]
    phrases3 = ["done it", "it"]
    printList(textQueries(sentences3, phrases3))
    # 0 3, 0 2 3

    #testcase 4
    sentences4 = ["it go will away", "go do it", "what to will east"]
    phrases4 = ["it will", "go east will", "will"]
    printList(textQueries(sentences4, phrases4))
    # 0, -1, 0 2

    #testcase 5
    sentences5 = ["bob alice bob alice bob alice"]
    phrases5 = ["bob alice"]
    printList(textQueries(sentences5, phrases5))
    # 0 0 0
    '''
    #testcase 6
    sentences6 = ["bob alice bob alice bob alice"]
    phrases6 = ["bob alice bob alice"]
    print(textQueries(sentences6, phrases6))
    # 
    '''
