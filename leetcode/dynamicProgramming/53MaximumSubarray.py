#53 Maximum Subarray
########
'''
#DP
idea is from: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1)+A[i] : 0 + A[i]; 

#DC
idea is from: https://leetcode.com/problems/maximum-subarray/discuss/20452/12ms-DPDC-C++-Solutions

The DC algorithm breaks nums into two halves and find the maximum subarray sum in them recursively. Well, the most tricky part is to handle the case that the maximum subarray may span the two halves. For this case, we use a linear algorithm: starting from the middle element and move to both ends (left and right ends), record the maximum sum we have seen. In this case, the maximum sum is finally equal to the middle element plus the maximum sum of moving leftwards and the maximum sum of moving rightwards.
'''
########
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp
        '''
        dp = [None]*len(nums)
        dp[0] = nums[0]
        max_ = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1] > 0:
                dp[i] = nums[i]+dp[i-1]
            else:
                dp[i] = nums[i]
            max_ = max(dp[i], max_)
        #print dp
        return max_
        '''
        '''
        #reduce space complexity
        dp, max_ = nums[0], nums[0]
        for i in range(1,len(nums)):
            if dp > 0:
                dp += nums[i]
            else:
                dp = nums[i]
            max_ = max(dp, max_)
        return max_
        '''
        #Divide & conquer
        def maxSub(nums, l, r):
            if l > r: return float('-inf')
            mid = l+(r-l)/2
            lMax = maxSub(nums, l, mid-1)
            rMax = maxSub(nums, mid+1, r)
            s1, s2 = 0, 0
            curr = 0
            for i in range(mid-1, l-1, -1):
                curr += nums[i]
                s1 = max(s1, curr)
            curr = 0
            for i in range(mid+1, r+1):
                curr += nums[i]
                s2 = max(s2, curr)
            return max(s1+s2+nums[mid], max(lMax, rMax))
        
        return maxSub(nums, 0, len(nums)-1)