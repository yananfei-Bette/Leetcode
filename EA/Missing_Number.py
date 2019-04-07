# Missing Number
#leetcode 268

class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sort
        # Time: O(nlogn)
        # space: O(1)
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            expected_num = nums[i - 1] + 1
            if expected_num != nums[i]:
                return expected_num


class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # hashset
        # Time: O(n)
        # space: O(n)
        num_set = set(nums)
        n = len(nums) + 1
        for i in range(n):
            if i not in num_set:
                return i


class Solution3(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Bit Manipulation
        # find the single num
        # Time: O(n)
        # space: O(1)
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


class Solution4(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Gauss Formula
        # Time: O(n)
        # space: O(1)
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
        