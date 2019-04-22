# 280 Wiggle Sort

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        # sorted and swap
        # time : O(nlogn)
        nums.sort()
        i = 1
        while i < len(nums) and i + 1 < len(nums):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        '''
        # one pass swap
        # time: O(n)
        leftLess = True
        for i in range(len(nums) - 1):
            if leftLess:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            leftLess = not leftLess
        