# 287 Find the Duplicate Number

class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort
        # Time: O(nlogn)
        # Space: O(1)

        # edge case
        if not nums:
            return None

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]
        return None


class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set
        # Time: O(n)
        # Space: O(n)
        if not nums:
            return None

        s = set()
        for num in nums:
            if num in s:
                return num
            s.add(num)
        return None


class Solution3(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Cycle detect
        # Find the intersection point of the two runners
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        # Time: O(n)
        # Space: O(1)
        if not nums:
            return None
        
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

            if tortoise == hare:
                break

        # Find the entrance to the cycle
        prt1 = nums[0]
        prt2 = tortoise
        while prt1 != prt2:
            prt1 = nums[prt1]
            prt2 = nums[prt2]
        return prt1











