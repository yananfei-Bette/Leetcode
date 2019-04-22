class UnionFind(object):
    def __init__(self, grid):
        nr, nc = len(grid), len(grid[0])
        
        self.count = 0
        self.parent = [None] * nr * nc
        self.rank = [None] * nr * nc
        
        for r in xrange(nr):
            for c in xrange(nc):
                if grid[r][c] == '1':
                    self.parent[r * nc + c] = r * nc + c
                    self.count += 1
                self.rank[r * nc + c] = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        
        if xRoot == yRoot:
            return
        # merge
        if self.rank[xRoot] < self.rank[yRoot]:
            xRoot, yRoot = yRoot, xRoot
            
        self.parent[yRoot] = xRoot
        
        if self.rank[xRoot] == self.rank[yRoot]:
            self.rank[xRoot] += 1
            
        self.count -= 1
    
    def getCount(self):
        return self.count
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        # recursive method
        seen = set()
        def dfs(r, c):
            if not (
                0 <= r < len(grid) \
                and 0 <= c < len(grid[0]) \
                and grid[r][c] == "1" \
                and (r, c) not in seen
            ):
                return 0
            seen.add((r, c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        
        return len([1 for r in xrange(len(grid)) for c in xrange(len(grid[0])) if dfs(r, c) != 0])
        '''
        #######################################
        '''
        # recursive method with dfs
        # time : O(nr*nc)
        # space : O(nr*nc)
        if not grid or not grid[0]:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        #seen = set()
        numIsland = 0
        
        def dfs(r, c):
            if not (
                0 <= r < nr and 0 <= c < nc and grid[r][c] == '1'
            ):
                return
            
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        
        for r in xrange(nr):
            for c in xrange(nc):
                if grid[r][c] != '0':
                    numIsland += 1
                    dfs(r, c)
        return numIsland
        '''
        #############################################
        '''
        # interative with BFS
        # time: O(nr*nc)
        # space: O(min(nr, nc))
        if not grid or not grid[0]:
            return 0
        
        nr = len(grid)
        nc = len(grid[0])
        numIsland = 0
        
        for r in xrange(nr):
            for c in xrange(nc):
                if grid[r][c] == '1':
                    numIsland += 1
                    grid[r][c] = '0'
                    
                    queue = [(r, c)]
                    while queue:
                        row, col = queue.pop(0)
                        #grid[r][c] = '0'
                        dirr = [-1, 1, 0, 0]
                        dirc = [0, 0, -1, 1]
                        for dr, dc in zip(dirr, dirc):
                            r_nei = row + dr
                            c_nei = col + dc
                            if 0 <= r_nei < nr and 0 <= c_nei < nc and grid[r_nei][c_nei] == '1':
                                queue.append((r_nei, c_nei))
                                grid[r_nei][c_nei] = '0'
        return numIsland
        '''
        ##################################
        # union find
        if not grid or not grid[0]:
            return 0
        nr, nc = len(grid), len(grid[0])
        
        uf = UnionFind(grid)
        
        for r in xrange(nr):
            for c in xrange(nc):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    dirr = [-1, 1, 0, 0]
                    dirc = [0, 0, -1, 1]
                    for dr, dc in zip(dirr, dirc):
                        r_nei = r + dr
                        c_nei = c + dc
                        if 0 <= r_nei < nr and 0 <= c_nei < nc and grid[r_nei][c_nei] == '1':
                            uf.union(r * nc + c, r_nei * nc + c_nei)
                            #grid[r_nei][c_nei] = '0'
        return uf.getCount()
        
        
                        
        