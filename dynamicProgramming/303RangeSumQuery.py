#303 Range Sum Query
#######
# idea is from :https://leetcode.com/problems/range-sum-query-immutable/solution/
'''
Let us define sum[k]sum[k] as the cumulative sum for nums[0: k-1]inclusive):

Now, we can calculate sumRange as following:

sumRange(i, j) = sum[j + 1] - sum[i] sumRange(i,j)=sum[j+1]−sum[i]

'''
#######

#Brute Force
'''
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # Brute Force
        return sum(self.nums[i:j+1])
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # Brute Force
        # pre-compute with hash table
        #self.nums = nums
        
        # DP
        self.sum = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.sum[i+1] = self.sum[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """       
        #DP
        return self.sum[j+1]-self.sum[i]


