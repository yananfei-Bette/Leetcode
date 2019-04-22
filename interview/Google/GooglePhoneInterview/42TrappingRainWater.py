# 42 Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        # Brute force
        # time: O(n*n)
        # space: O(1)
        if not height:
            return 0
        
        nh = len(height)
        res = 0
        
        for i in xrange(nh):
            maxl, maxr = 0, 0
            for j in xrange(i, -1, -1):
                maxl = max(maxl, height[j])
            for j in xrange(i, nh):
                maxr = max(maxr, height[j])
            #print min(maxl, maxr) - height[i]
            res += min(maxl, maxr) - height[i]
        return res
        '''
        ###############################
        # Dynamic programming
        # time: O(n)
        # space: O(n)
        if not height:
            return 0
        nh = len(height)
        res = 0
        maxl = [None] * nh
        maxr = [None] * nh
        maxl[0] = height[0]
        maxr[-1] = height[-1]
        for i in xrange(1, nh):
            maxl[i] = max(maxl[i - 1], height[i])
        for i in xrange(nh - 2, -1, -1):
            maxr[i] = max(maxr[i + 1], height[i])
        for i in xrange(nh):
            res += min(maxr[i], maxl[i]) - height[i]
        return res