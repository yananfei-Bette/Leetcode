#308 Range Sum Query
# idea comes from : https://leetcode.com/problems/range-sum-query-2d-mutable/discuss/75870/Java-2D-Binary-Indexed-Tree-Solution-clean-and-short-17ms
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        #self.matrix = matrix
        
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        self.max_x = len(matrix)
        self.max_y = len(matrix[0])
                
        self.tree = [[0 for _ in range(self.max_y+1)] for _ in range(self.max_x+1)]
        self.nums = [[0 for _ in range(self.max_y)] for _ in range(self.max_x)]
        
        #initial the tree
        for i in range(self.max_x):
            for j in range(self.max_y):
                self.update(i, j, matrix[i][j])
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        #self.matrix[row][col] = val
        
        delta = val - self.nums[row][col]
        self.nums[row][col] = val
        
        i, j = row+1, col+1
        while i <= self.max_x:
            while j <= self.max_y:
                self.tree[i][j] += delta
                j += (j & -j)
            i += (i & -i)
            j = col+1
        
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #res = 0
        #for i in range(row1, row2+1):
        #    for j in range(col1, col2+1):
        #        res += self.matrix[i][j]
        #return res
        
        # bit calculate
        def accumulate_sum(row, col):
            res = 0
            i, j = row, col
            while i > 0:
                while j > 0:
                    res += self.tree[i][j]
                    j -= (j & -j)
                i -= (i & -i)
                j = col
            return res
        
        return accumulate_sum(row2+1, col2+1)+accumulate_sum(row1, col1)-accumulate_sum(row1, col2+1)-accumulate_sum(row2+1,col1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
