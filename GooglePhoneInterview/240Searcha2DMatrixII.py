# 240 Search a 2D Matrix II
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # my anwser 1
        # binary search
        '''
        if not matrix or not matrix[0]:
            return False
        
        nr, nc = len(matrix), len(matrix[0])
        lr, lc = 0, 0
        rr, rc = nr - 1, nc - 1
        
        def binarySearch(lr, lc, rr, rc):
            if not (0 <= lr < nr and 0 <= lc < nc and 0 <= rr < nr and 0 <= rc < nc and lr <= rr and lc <= rc):
                return False

            midr, midc = (lr + rr) / 2, (lc + rc) / 2
            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] > target:
                r1, c1 = midr - 1, rc
                r2, c2 = rr, midc - 1
                return binarySearch(lr, lc, r1, c1) or binarySearch(lr, lc, r2, c2)
            else:
                r1, c1 = midr + 1, lc
                r2, c2 = lr, midc + 1
                return binarySearch(r1, c1, rr, rc) or binarySearch(r2, c2, rr, rc)
               
        return binarySearch(lr, lc, rr, rc)
        '''
        ########################################
        # my answer 2
        '''
        if not matrix or not matrix[0]:
            return False
        nr, nc = len(matrix), len(matrix[0])
        r, c = nr - 1, nc - 1
        def dfs(r, c):
            if not (0 <= r < nr and 0 <= c < nc):
                return False
            if matrix[r][c] == target:
                return True
            return dfs(r - 1, c) or dfs(r, c - 1)
        return dfs(r, c)
        '''
        #######################################
        # brute force
        # time: O(m * n)
        # space: O(1)
        '''
        for row in matrix:
            for val in row:
                if val == target:
                    return True
        return False
        '''
        #######################################
        # binary search
        # time: O(mlog(n))
        '''
        if not matrix or not matrix[0]:
            return False
        
        def binarySearch(matrix, target, start, vertical):
            lo = start
            hi = len(matrix) - 1 if vertical else len(matrix[0]) - 1
            
            while lo <= hi:
                mid = (lo + hi) / 2
                if vertical:
                    if matrix[mid][start] > target:
                        hi = mid - 1
                    elif matrix[mid][start] < target:
                        lo = mid + 1
                    else:
                        return True
                else:
                    if matrix[start][mid] > target:
                        hi = mid - 1
                    elif matrix[start][mid] < target:
                        lo = mid + 1
                    else:
                        return True
            return False
        
        for i in xrange(min(len(matrix), len(matrix[0]))):
            vertical = binarySearch(matrix, target, i, True)
            horizontal = binarySearch(matrix, target, i, False)
            if vertical or horizontal:
                return True
        return False
        '''
        ###############################################
        # d & c ==> my answer 1
        # pruning by using
        # if matrix[r1][c1] > target or matrix[r2][c2] < target:
        #     return False
        # only mid column and check two matrixs that are
        # --- ---
        #|   | . |
        # --- ---
        #| . |   |
        # --- ---
        # time: O(nlogn)
        '''
        if not matrix or not matrix[0]:
            return False
        
        def searchRec(r1, c1, r2, c2):
            if not (0 <= r1 <= r2 < len(matrix) and 0 <= c1 <= c2 < len(matrix[0])):
                return False
            if matrix[r1][c1] > target or matrix[r2][c2] < target:
                return False
            midc = (c1 + c2) / 2
            r = r1
            while r <= r2 and matrix[r][midc] <= target:
                if matrix[r][midc] == target:
                    return True
                r += 1
            return searchRec(r, c1, r2, midc - 1) or searchRec(r1, midc + 1, r - 1, c2)
            
            
        r1, c1 = 0, 0
        r2, c2 = len(matrix) - 1, len(matrix[0]) - 1
        return searchRec(r1, c1, r2, c2)
        '''
        ############################################
        # I have thought about this kinda idea, the tricky part is the initial position. It's kinda like path, one direction is to increase and the other is decrease. My idea is start from right-down to left-up. It's not right, cz two ways will decrease the value.
        # The idea is either choose left-down cell or right-up cell as start point. Assuming we choose left-down cell as start point, and we can either go up to decrease our value or go right to increase our value.
        if not matrix or not matrix[0]:
            return False
        r, c = len(matrix) - 1, 0
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
        
        
                    
                        
                
        
                
