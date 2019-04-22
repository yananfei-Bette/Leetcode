# 22 Generate Parentheses
# backtrack
# Similary problem lc46 Permutations

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(l, r, res, curr):
            if r == 0:
                res.append(curr)
            if l > 0:
                helper(l - 1, r, res, curr + '(')
            if r > l:
                helper(l, r - 1, res, curr + ')')
        
        res = []
        if n == 0:
            return res.append('')
        helper(n, n, res, '')
        return res