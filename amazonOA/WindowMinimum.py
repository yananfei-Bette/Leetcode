# Window Minimum
# Input: [4, 2, 12, 11, -5]
# Window size: 2
# Output: [4, 12, 12, 11]
# Dequeue

class Solution(object):
	def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # https://leetcode.com/problems/sliding-window-maximum/discuss/111560/Python-O(n)-solution-using-deque-with-comments
        if not nums or k <= 0:
        	return []

        deque = collections.deque()
        res = []

        for i in range(k):
        	while deque:
        		if nums[i] > nums[deque[-1]]:
        			deque.pop()
        		else:
        			break
        	deque.append(i)

        for i in range(k, len(nums)):
        	res.append(nums[deque[0]])
        	if deque[0] < i - k + 1:
        		deque.popleft()
        	while deque:
        		if nums[i] > nums[deque[-1]]:
        			deque.pop()
        		else:
        			break
        	deque.append(i)

        res.append(nums[deque[0]])
        return res