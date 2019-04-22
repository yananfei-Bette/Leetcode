# 128 Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # time: O(n*logn)
        # space: O(1)
        # sort
        if not nums:
            return 0
        
        nums.sort()
        res = 1
        curr = 1
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 1
        return max(res, curr)
        '''
        ####################################
        # the main idea is: for each num, check its consequence.
        # but we use hashset instead of list, so that the time will reduce to O(1)
        if not nums:
            return 0
        res = 0
        nums_set = set(nums)
        
        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_count = 1
                
                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_count += 1
                    
                res = max(res, curr_count)
        return res
        