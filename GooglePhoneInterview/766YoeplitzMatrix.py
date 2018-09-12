#766 toeplitz matrix
# idea comes form https://leetcode.com/problems/toeplitz-matrix/solution/
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        '''
        # dfs
        def dfs(x, y, matrix):
            if x == 0 or y == len(matrix[0])-1: return True
            #if x == 0:
            #    return dfs(x, y+1, matrix)
            #if y == len(matrix[0])-1:
            #    return dfs(x-1, y, matrix)
            if matrix[x-1][y] != matrix[x][y+1]: return False
            return dfs(x-1,y,matrix)&dfs(x,y+1,matrix)
            
        max_x = len(matrix)
        max_y = len(matrix[0])
        return dfs(max_x-1, 0, matrix)
        '''
        '''
        # group by category
        # r1-c1 == r2-c2 means two points in the same diagonal
        group = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in group:
                    group[r-c] = val
                elif group[r-c] != val:
                    return False
        return True
        '''
        #Compare with top-left neighbor
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val for r, row in enumerate(matrix) for c, val in enumerate(row))

