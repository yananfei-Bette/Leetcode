# 694 Number of Distinct Islands
# Time: O(R * C)
# Spce: O(R * C)


# hash by local coordinates
class Solution1(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        def dfs(r, c, r0, c0):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c] == 1):
                return

            seen.add((r, c))
            shape.add((r - r0, c - c0))

            dfs(r - 1, c, r0, c0)
            dfs(r + 1, c, r0, c0)
            dfs(r, c - 1, r0, c0)
            dfs(r, c + 1, r0, c0)

            return

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                dfs(r, c, r, c)
                if shape:
                    shapes.add(forzenset(shape))
        return len(shapes)



# hash by path signature
class Solution2(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set()
        def dfs(r, c, di = 0):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c) not in seen and grid[r][c] == 1):
                return

            seen.add((r, c))
            shape.append(di)

            dfs(r - 1, c, 1)
            dfs(r + 1, c, 2)
            dfs(r, c - 1, 3)
            dfs(r, c + 1, 4)

            # important
            shape.append(0)
            return

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = []
                dfs(r, c)
                if shape:
                    shapes.add(tuple(shape))
        return len(shapes)