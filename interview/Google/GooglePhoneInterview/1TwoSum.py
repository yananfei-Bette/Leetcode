#1 two sum
#idea comes from: https://leetcode.com/problems/two-sum/solution/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        #brute force
        #O(n^2)
        res = []
        for i in range(len(nums)):
            a = nums[i]
            b = target - nums[i]
            if b in nums:
                if a != b:
                    return [i, nums.index(b)]
                else:
                    b_indexes = [ind for ind in range(len(nums)) if nums[ind] == b]
                    if len(b_indexes) > 1:
                        for j in b_indexes:
                            if i != j: return [i, j]
        '''
        '''
        #two passes hash
        #O(n), O(n)
        dic_1 = {}
        for i in range(len(nums)):
            if nums[i] not in dic_1:
                dic_1[nums[i]] = [i]
            else:
                dic_1[nums[i]].append(i)
        
        for i in range(len(nums)):
            b = target - nums[i]
            if b in dic_1:
                indexes = dic_1[b]
                if len(indexes) == 1 and indexes[0] != i:
                    return [i, indexes[0]]
                elif len(indexes) > 1:
                    for ind in indexes:
                        if ind != i:
                            return [i, ind]
        '''
        #one pass hash
	#O(n), O(1)
        dic = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if b in dic:
                return [i, dic[b]]
            dic[nums[i]] = i
            
                    
        
