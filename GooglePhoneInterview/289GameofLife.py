# 289 Game of Life

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # [2nd bit, 1st bit] = [next state, current state]
        # - 00  dead (next) <- dead (current)
        # - 01  dead (next) <- live (current)  
        # - 10  live (next) <- dead (current)  
        # - 11  live (next) <- live (current) 
        # In the beginning, every cell is either 00 or 01
        # board[i][j] & 1
        # board[i][j] >> 1
        if not board or not board[0]:
            return
        
        #######################################
        def liveNeighbor(board, nr, nc, i, j):
            # check 8 cells
            lives = 0
            x_start = max(i - 1, 0)
            y_start = max(j - 1, 0)
            x_end = min(i + 1, nr - 1)
            y_end = min(j + 1, nc - 1)
            
            for x_i in xrange(x_start, x_end + 1):
                for y_j in xrange(y_start, y_end + 1):
                    lives += board[x_i][y_j] & 1
            lives -= board[i][j]
            return lives
        ##########################################
        
        nr = len(board)
        nc = len(board[0])
        for i in xrange(nr):
            for j in xrange(nc):
                lives = liveNeighbor(board, nr, nc, i, j)
                if board[i][j] == 1 and 2 <= lives <= 3:
                    board[i][j] = 3 # 01 -> 11
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2 # 00 -> 10
        # get 2nd state
        for i in xrange(nr):
            for j in xrange(nc):
                board[i][j] >>= 1
        