#714 Best Time to Buy and Sell Stock with transaction Fee
#Compare to #121
#Idea comes from https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/solution/
'''
To transition from the i-th day to the i+1-th day, we either sell our stock cash = max(cash, hold + prices[i] - fee) or buy a stock hold = max(hold, cash - prices[i]). At the end, we want to return cash. 
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, prices[i]+hold-fee)
            hold = max(hold, cash - prices[i])
        return cash