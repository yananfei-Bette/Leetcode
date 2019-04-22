# 1 Two Sum

# brute force
# Time: O(n * n)
# Space: O(1)
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Two-pass Hash table
# Time: O(n)
# Space: O(1)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if x in hash_table and i != hash_table[x]:
                return [hash_table[x], i]
        return [-1, -1]


# one pass hash table
# Time: O(n)
# Space: O(n)
class Solution3(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hash_table:
                return [hash_table[x], i]
            hash_table[nums[i]] = i
        return [-1, -1]



# follow up
# 3 sum
# a + b + c = 0
# Time: O(n * n)
# Space: O(1)
class Solution_threeSum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # corner case
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                # find the second and third nums
                # make them satisfied: first + second + thrid == 0
                lo = i + 1
                hi = len(nums) - 1
                twoSumTarget = 0 - nums[i]

                while lo < hi:
                    if nums[lo] + nums[hi] == twoSumTarget:
                        res.append([nums[i], nums[lo], nums[hi]])

                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1

                    elif nums[lo] + nums[hi] < twoSumTarget:
                        lo += 1
                    else:
                        hi -= 1
        return res


# follow up
# n sum
class Solution_nSum(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # corner case
        if len(nums) < 4:
            return []

        def findNSum(nums, target, N, curr):
            if len(nums) < N or N < 2 or nums[0] * N > target or nums[-1] * N < target:
                return

            if N == 2:
                # two sum proble
                lo = 0
                hi = len(nums) - 1
                while lo < hi:
                    currSum = nums[lo] + nums[hi]
                    if currSum == target:
                        res.append(curr + [nums[lo], nums[hi]])

                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1
                    elif currSum < target:
                        lo += 1
                    else:
                        hi -= 1
            else:
                # reduce to N - 1 sum proble
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i] != nums[i - 1]:
                        findNSum(nums[i + 1:], target - nums[i], N - 1, curr + [nums[i]])

        res = []
        nums.sort()

        findNSum(nums, target, 4, [])
        return res



