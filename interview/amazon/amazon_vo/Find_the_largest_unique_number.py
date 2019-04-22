# Find the largest unique number
class Solution(obejct):
    def findTheLargestUnique(self, nums):
        # O(n)
        count = collections.Counter(nums)
        res = None
        # O(n)
        for num in nums:
            if count[num] == 1:
                res = max(res, num) if res != None else num
        return res

