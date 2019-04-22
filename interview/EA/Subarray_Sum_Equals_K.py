# Subarray Sum Equals K
# leetcode 560

class Solution1(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # cumulative sum
        # TLE

        count = 0
        sumArr = [0] * len(nums)
        sumArr[0] = nums[0]
        
        for i in range(1, len(nums)):
            sumArr[i] = sumArr[i - 1] + nums[i]
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sumArr[j] - sumArr[i] + nums[i] == k:
                    count += 1
        
        return count



class Solution2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # space: O(1)
        # TLE

        count = 0
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                if currSum == k:
                    count += 1
        return count


class Solution3(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hashmap with two sum idea
        count = 0
        summ = 0
        hashmap = {0: 1}
        for i in range(len(nums)):
            summ += nums[i]
            x = summ - k
            if x in hashmap:
                count += hashmap[x]
            hashmap[summ] = hashmap.get(summ, 0) + 1
        return count