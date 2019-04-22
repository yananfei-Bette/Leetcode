#343 Integer Break
#idea comes from https://leetcode.com/problems/integer-break/discuss/80707/Easy-Java-DP-solution-with-explanation-typical-knapsack-problem
'''
This is a typical knapsack problem. We can assume that the volume of the knapsack is n. The items we can choose range from 1 to n - 1(because we must divide n into at least two positive parts). The point is that we can choose each item many times.
The first loop means the items we can choose(i means first i items).
And in the second loop, j means the sum of items that we are going to choose.
For each item, we have two choices, pick it up or not. And we should choose the max result.
just as dp[j] = Math.max(dp[j], dp[j - i] * i);
Then, you are able to solve the problem.
By the way, the initialization is also important.
'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dp knapsack problem
        dp = [None for i in range(n+1)]
        dp[0] = 1
        for i in range(1, n):
            for j in range(i, n+1):
                dp[j] = max(dp[j], dp[j-i]*i)
        return dp[-1]