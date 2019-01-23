#198 House Robber
#######
#dp[i] = max(dp[i-1], dp[i-2]+nums[i])
#######
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp
        '''
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [None]*len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        '''
        #reduce space complexity
        # rob1 = dp[i-2]
        #rob2 = dp[i-1]
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        rob1, rob2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            rob1, rob2 = rob2, max(rob2, rob1+nums[i])
        return rob2