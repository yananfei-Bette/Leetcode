#746 minCostClimbingStairs
##############
#idea is from https://leetcode.com/problems/min-cost-climbing-stairs/solution/
'''
Intuition

There is a clear recursion available: the final cost f[i] to climb the staircase from some step i is f[i] = cost[i] + min(f[i+1], f[i+2]). This motivates dynamic programming.

Algorithm

Let's evaluate f backwards in order. That way, when we are deciding what f[i] will be, we've already figured out f[i+1] and f[i+2].

We can do even better than that. At the i-th step, let f1, f2 be the old value of f[i+1], f[i+2], and update them to be the new values f[i], f[i+1]. We keep these updated as we iterate through i backwards. At the end, we want min(f1, f2).

Complexity Analysis

Time Complexity: O(N)O(N) where NN is the length of cost.

Space Complexity: O(1)O(1), the space used by f1, f2.
'''
##############
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1, f2 = 0, 0
        for i in range(len(cost)-1,-1,-1):
            f1, f2 = cost[i]+min(f1,f2), f1
        return min(f1,f2)