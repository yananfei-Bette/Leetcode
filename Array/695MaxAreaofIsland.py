#695 Max Area of Island

#idea comes from https://leetcode.com/problems/max-area-of-island/solution/

'''
Intuition and Algorithm

We want to know the area of each connected shape in the grid, then take the maximum of these.

If we are on a land square and explore every square connected to it 4-directionally (and recursively squares connected to those squares, and so on), then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, let's use seen to keep track of squares we haven't visited before. It will also prevent us from counting the same shape more than once.
'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        check = set()
        def area(r,c):
            if not (0<=r<len(grid) and 0<=c<len(grid[0]) and (r, c) not in check and grid[r][c]):
                return 0
            check.add((r, c))
            return 1+area(r+1,c)+area(r-1,c)+area(r,c+1)+area(r,c-1)
        return max(area(r,c) for r in range(len(grid)) for c in range(len(grid[0])))
