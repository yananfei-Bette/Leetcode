# 79 Word Search
# Backtrack
# Generate Parentheses
# Permutations

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, r, c):
            if i == len(word):
                return True
            if 0 <= r < R and 0 <= c < C and not visited[r][c] and board[r][c] == word[i]:
                visited[r][c] = True
                res =  True and (dfs(i+1, r, c-1) or 
                                 dfs(i+1, r, c+1) or 
                                 dfs(i+1, r-1, c) or 
                                 dfs(i+1, r+1, c))
                visited[r][c] = False
                return res
            
            return False
                
            
        if not word or not board or len(word) > len(board)*len(board[0]):
            return False
        R, C = len(board), len(board[0])
        visited = [[False]*C for _ in xrange(R)]
        return any([dfs(0, r, c) for r in xrange(R) for c in xrange(C) if board[r][c] == word[0]])
