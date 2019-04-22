# 121 Best Time to Buy and Sell Stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Time: O(n)
        minPrice = float("inf")
        maxRes = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            if price - minPrice > maxRes:
                maxRes = price - minPrice
        return maxRes