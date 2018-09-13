#46 Permutation

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(res, currList, nums):
            if len(currList) == len(nums):
                res.append([curr for curr in currList])
            else:
                for i in range(len(nums)):
                    if nums[i] not in currList:
                        currList.append(nums[i])
                        helper(res, currList, nums)
                        currList.pop()
        
        res = []
        if not nums or len(nums) == 0:
            return res.append([])
        helper(res, [], nums)
        return res

#47 Permutation II
#Duplicate

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(res, currList, nums, used):
            if len(currList) == len(nums):
                res.append([curr for curr in currList])
            else:
                preNum = None
                for i in range(len(nums)):
                    if used[i] == False and nums[i] != preNum:
                        preNum = nums[i]
                        used[i] = True
                        currList.append(nums[i])
                        helper(res, currList, nums, used)
                        used[i] = False
                        currList.pop()
        
        res = []
        if not nums or len(nums) == 0:
            return res.append([])
        nums.sort()
        helper(res, [], nums, [False]*len(nums))
        return res