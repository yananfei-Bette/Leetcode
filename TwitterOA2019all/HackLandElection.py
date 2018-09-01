#HackLand Election
def hackerLandElection(votes):
    dic = {}
    for vote in votes:
        if vote not in dic:
            dic[vote] = 1
        else:
            dic[vote] += 1
    sortedResults = sorted(dic.items(), key = lambda item: (item[1], item[0]))[::-1]
    #print(sortedResults)
    maxNum = sortedResults[0][1]
    #print(maxNum)
    candidates = []
    for item in sortedResults:
        if item[1] == maxNum:
            candidates.append(item[0])
        else:
            break
    #print(candidates)
    return sorted(candidates, key=str.lower, reverse=True)[0]


votes = [ "victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica"]
votes2 = ["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"]
print(hackerLandElection(votes2))
