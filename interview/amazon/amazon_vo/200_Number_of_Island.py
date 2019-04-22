# 200 Number of Island

# recursion
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][r] == '1'):
                return

            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            return

        # corner case
        if not grid or not grid[0]:
            return 0

        numIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numIsland += 1
                    dfs(r, c)


# iteration
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # corner case
        if not grid or not grid[0]:
            return 0

        numIslands = 0
        dirr = [-1, 1, 0, 0]
        dirc = [0, 0, -1, 1]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    numIslands += 1
                    grid[r][c] == '0'

                    # bfs
                    queue = [(r, c)]
                    while queue:
                        r, c = queue.pop(0)
                        for dr, dc in zip(dirr, dirc):
                            cr, cc = r + dr, c + dc
                            if 0 <= cr < len(grid) and 0 <= cc < len(grid) and grid[cr][cc] == '1':
                                queue.append((cr, cc))
                                grid[cr][cc] = '0'

        return numIslands

