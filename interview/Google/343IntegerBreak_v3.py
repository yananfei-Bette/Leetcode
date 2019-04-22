#343 Integer Break version 3

def getBalance(n, x, y):
    maxDiff = max(x)
    #initial dp
    dp = [[0]*(maxDiff+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(maxDiff+1):
            aScore, bScore = 0, 0
            if j-x[i-1] >= 0: #a picks
                aPick = dp[i-1][j-x[i-1]]+y[i-1]
            if j+x[i-1] <= maxDiff: #b picks
                bPick = dp[i-1][j+x[i-1]]+y[i-1]
            dp[i][j] = max(dp[i-1][j], aPick, bPick)
            if i == 1 and j == 0: # only one card and none of them picks.
                dp[i][j] = 0
    return dp[n][0]
    
    ################
def getBalance(loads):
    dp = [None for i in range(len(loads))]
    for ind, load in enumerate(loads):
        dp[ind] = min(dp[ind-1]

loads = [1,2,3,4,5]
print(getBalance(loads))
