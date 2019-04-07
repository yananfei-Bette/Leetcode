# 136 Single Number

# Bit manipulation
class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        # Time: O(n)
        # Space: O(1)
        if not nums:
            return None

        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

# Math
# 2 * (a + b + c) - (a + a + b + b + c) = c
class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n) two sum function
        # Spce: O(n) set space
        return 2 * sum(set(nums)) - sum(nums)


# List operation
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n * n)
        # Space: O(n)
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

# Hash Table
class Solution4(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        hash_table = {}
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table.pop(i)
        return hash_table.popitem()[0]



# Follow up
# Find the element that appears once in a sorted array
# in O(logn) complexity
# https://www.geeksforgeeks.org/find-the-element-that-appears-once-in-a-sorted-array/

# arr = [1, 1, 3, 3, 4, 5 ,5, 7, 7, 8, 8]
# binary search
# all elements before the required have first occurrance at even index 0, 2, 4, 6
# and next occurrence at odd index
# all elements after requied element have first occurrance at odd index
# and next occurrence at even index

# Find the middle index, say 'mid'

# if 'mid' is even, check arr[mid], arrr[mid + 1]
# if they are same, required element located after mid
# else before mid

# if 'mid' is odd, check arr[mid - 1], arr[mid]
# if they are same, reuired element located after mid
# else before

class Solution_sortedArr(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # corner case
        if not nums:
            return None

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                return nums[l]

            mid = (l + r) // 2

            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 2
                else:
                    r = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

if __name__ == "__main__":
    sol = Solution_sortedArr()
    arr = [1, 1, 3, 3, 4, 5 ,5, 7, 7, 8, 8]
    print(sol.singleNumber(arr))


