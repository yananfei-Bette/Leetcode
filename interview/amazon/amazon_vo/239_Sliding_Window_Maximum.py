# 239 Sliding Window Maximum
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time: O(n)
        # Space: O(n)
        # edge case
        if not nums or k <= 0:
            return []

        deq = collections.deque()
        res = []

        # initialize dequeue
        for i in range(k):
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        for i in range(k, len(nums)):
            res.append(nums[deq[0]])
            if deq[0] < i - k + 1:
                deq.popleft()
            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

        res.append(nums[deq[0]])
        return res
