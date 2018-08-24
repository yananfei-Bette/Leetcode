#343 Integer Break (version 2 card)
#a and b play a game that has n cards. Each card has two integers x and y.
#when pick a card, add x to the person and add y to group.
#or neither a or b pick the card.
#let their personal scores are equal and maximize the group score.
#after they pick several cards.

#input
#4
#3 1
#2 2
#1 4
#1 4

#output
#10
#cz, a can pick 2 2 and b can pick 1 4 and 1 4.

#this problem is really like the knapsack problem
#let say personalScore(a)-personalScore(b) = 0
#we have three cases
#1.none of them picks the card
#2.a picks the card
#3.b picks the card
#the problem is going to:
#dp[i][j] = max(dp[i-1][j], a picks, b picks)
# i means ith card
# j means the different between personalScore(a) and personalScore(b)
# a picks = dp[i-1][j-x[i-1]]+y[i-1]
# b picks = dp[i-1][j+x[i-1]]+y[i-1]

# code comes from https://blog.csdn.net/XX_123_1_RJ/article/details/81808305

def getMaxGain(n, x, y):
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

n = 4
x = [3,2,1,1]
y = [1,2,4,4]
print(getMaxGain(n,x,y))
