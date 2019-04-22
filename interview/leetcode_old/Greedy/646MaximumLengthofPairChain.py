# 646 Maximum Length of Pair Chain
# Greedy idea comes from https://leetcode.com/problems/maximum-length-of-pair-chain/solution/
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        ###############Greedy###################
        # We can greedily add to our chain.
        # Choosing the next addition to be the
        # one with the lowest second coordinate
        # is at least better than a choice with
        # a larger second coordinate.
        ########################################
        curr, res = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if curr < x:
                curr = y
                res += 1
        return res