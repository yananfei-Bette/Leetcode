# 31 Next Permutation

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the first pair of two successive numbers a[i], a[i] and a[i-1]a[i−1], from right to left
        # find the first large than a[i], which is a[j], from right to left
        # swap a[i] and a[j]
        # reverse the rest part start from index i.
        
        def reverse(start):
            i = start
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

            
        if not nums:
            return
        
        firstSmall = -1
        for i in xrange(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstSmall = i
                break
        #print nums[firstSmall]
        # 321
        if firstSmall == -1:
            reverse(0)
            return
        
        firstLarge = -1
        for i in xrange(len(nums) - 1, -1, -1):
            if nums[i] > nums[firstSmall]:
                firstLarge = i
                break
        #print nums[firstLarge]
        nums[firstSmall], nums[firstLarge] = nums[firstLarge], nums[firstSmall]
        #print nums
        reverse(firstSmall + 1)
        return
        