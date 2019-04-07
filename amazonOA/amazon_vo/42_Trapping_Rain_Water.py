# 42 Trapping Rain Water
class Solution(object):
    def trap(self, height):
        # dp
        # edge casexs
        if not height:
            return 0

        numHeight = len(height)
        maxL = [None] * numHeight
        maxR = [None] * numHeight

        maxL[0] = height[0]
        maxR[-1] = height[-1]

        for i in range(1, numHeight):
            maxL[i] = max(maxL[i - 1], height[i])

        for i in range(numHeight - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])

        res = 0
        for i in range(numHeight):
            res += min(maxL[i], maxR[i]) - height[i]

        return res
