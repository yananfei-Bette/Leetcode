# 54 Spiral Matrix

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        '''
        # we need direction and visited map
        # time : O(R*C)
        # space : O(R*C)
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        visited = [[False] * C for _ in range(R)]
        res = []
        dirR = [0, 1, 0, -1]
        dirC = [1, 0, -1, 0]
        r, c, di = 0, 0, 0
        for _ in range(R * C):
            res.append(matrix[r][c])
            visited[r][c] = True
            cr, cc = r + dirR[di], c + dirC[di]
            if 0 <= cr < R and 0 <= cc < C and not visited[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dirR[di], c + dirC[di]
        return res
        '''
        # layer by layer:
        # two coordinates bounding box
        # time : O(R*C)
        # space : O(R*C)
        def helperLayer(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1 - 1 , -1):
                    yield r2, c
                for r in range(r2 - 1, r1, -1):
                    yield r, c1
                    
        if not matrix:
            return []
        res = []
        r1, c1 = 0, 0
        r2, c2 = len(matrix) - 1, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in helperLayer(r1, c1, r2, c2):
                res.append(matrix[r][c])
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res
        