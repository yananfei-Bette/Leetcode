# 740 Delete and Earn
# https://www.youtube.com/watch?v=YzZd-bsMthk
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # House rob
        # time: O(r + n)
        # space : O(r)
        def houseRobber(count):
            dp1, dp2 = 0, 0
            for i in range(len(count)):
                dp1, dp2 = dp2, max(dp1 + count[i], dp2)
            return dp2
            
        if not nums:
            return 0
        r = max(nums)
        count = [0] * (r + 1)
        for num in nums:
            count[num] += num

        return houseRobber(count)
