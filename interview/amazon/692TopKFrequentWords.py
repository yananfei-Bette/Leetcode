# Top K Frequent Words
# Leetcode 692

class Solution692(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda word: (-count[word], word))
        return candidates[:k]

# Leetcode 347
class Solution347(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key = count.get)