class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        # recursive solution
        # time: O(r*c)
        seen = set()
        def dfs(r, c):
            if not(
                0 <= r < len(grid) \
                and 0 <= c < len(grid[0]) \
                and grid[r][c] \
                and (r, c) not in seen
            ):
                return 0
            seen.add((r, c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            
        return max(
            dfs(r, c) \
            for r in range(len(grid)) \
            for c in range(len(grid[0]))
        )
        '''
        # iterative
        # time: O(r*c)
        # stack save the candidates and have not been counted squares
        seen = set()
        res = 0
        
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                
                if val and (r0, c0) not in seen:
                    stack = [(r0, c0)]
                    area = 0
                    seen.add((r0, c0))
                    
                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for r_, c_ in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (
                                0 <= r_ < len(grid) \
                                and 0 <= c_ < len(grid[0]) \
                                and grid[r_][c_] \
                                and (r_, c_) not in seen
                            ):
                                stack.append((r_, c_))
                                seen.add((r_, c_))
                                
                    res = max(res, area)
        return res
        
        