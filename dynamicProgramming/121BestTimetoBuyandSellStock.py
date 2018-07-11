#121 Best Time to Buy and Sell Stock
#########
#idea is from:https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
'''
We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).

In formal terms, we need to find \max(prices[j] - prices[i])max(prices[j]−prices[i]), for every ii and jj such that j > ij>i.

Approach 1: Brute Force

Complexity Analysis

Time complexity : O(n^2)O(n
​2
​​ ). Loop runs \dfrac{n (n-1)}{2}
​2
​
​n(n−1)
​​  times.

Space complexity : O(1)O(1). Only two variables - \text{maxprofit}maxprofit and \text{profit}profit are used. 

Approach 2: One Pass
Algorithm

Say the given array is:

[7, 1, 5, 3, 6, 4]

If we plot the numbers of the given array on a graph, we get:

Profit Graph

The points of interest are the peaks and valleys in the given graph. We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.

Complexity Analysis

Time complexity : O(n)O(n). Only a single pass is needed.

Space complexity : O(1)O(1). Only two variables are used.
'''
#########
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #Brute Force
        #Time Limit Exceeded
        '''
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j]-prices[i])
        return profit
        '''
        #One pass
        minPrice = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i]-minPrice)
        return maxProfit