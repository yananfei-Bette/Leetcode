# 695 Max Area of Island

# recursion
# Time: O(r * c)
# Space: O(1)
class Solution1(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # edge case
        if not grid or not grid[0]:
            return 0

        seen = set()

        def dfs(r, c):
            if (
                0 <= r < len(grid) \
                and 0 <= c < len(grid[0]) \
                and (r, c) not in seen \
                and grid[r][c] == 1
                ):
                seen.add((r, c))
                return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            else:
                return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i, j))
        return res


# Iteration
# Time: O(r * c)
# Space: O(1)
class Solution2(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # edge case
        if not grid or not grid[0]:
            return 0

        seen = set()
        dirr = [-1, 1, 0, 0]
        dirc = [0, 0, -1, 1]

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    stack = [(i, j)]
                    seen.add((i, j))
                    area = 0

                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for dr, dc in zip(dirr, dirc):
                            cr, cc = r + dr, c + dc
                            if (
                                0 <= cr < len(grid) \
                                and 0 <= cc < len(grid[0]) \
                                and (cr, cc) not in seen \
                                and grid[cr][cc] == 1
                                ):
                                stack.append((cr, cc))
                                seen.add((cr, cc))

                    res = max(res, area)

        return res


###########
# Follow up
# find k largest

class Solution3(object):
    def maxAreaOfIsland(self, grid, k):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # edge case
        if not grid or not grid[0]:
            return 0

        minheap = []
        def addToMinheap(num):
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)

        seen = set()
        dirr = [-1, 1, 0, 0]
        dirc = [0, 0, -1, 1]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    stack = [(i, j)]
                    seen.add((i, j))
                    area = 0

                    while stack:
                        r, c = stack.pop()
                        area += 1
                        for dr, dc in zip(dirr, dirc):
                            cr, cc = r + dr, c + dc
                            if (
                                0 <= cr < len(grid) \
                                and 0 <= cc < len(grid[0]) \
                                and (cr, cc) not in seen \
                                and grid[cr][cc] == 1
                                ):
                                stack.append((cr, cc))
                                seen.add((cr, cc))

                    addToMinheap(area)

        return minheap[0] if minheap else 0

