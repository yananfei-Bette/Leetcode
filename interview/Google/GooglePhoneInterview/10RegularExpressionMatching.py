class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        # recursive 
        # for '*' we may igore the '*' in pattern or delete the matching character in text aka s.
        # 'a*' can be '', 'a', 'aaaaa....'
        # time consume in copy str into recursive funtion
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:])) or (first_match and self.isMatch(s[1:], p))
        return first_match and self.isMatch(s[1:], p[1:])
        '''
        ########################################
        # dp(i, j) means isMatch(s[i:], p[j:])
        # time: O(t*p)
        # top-down
        '''
        memo = {}
        
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    res = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        res = dp(i, j + 2) or (first_match and dp(i + 1, j))
                    else:
                        res = first_match and dp(i + 1, j + 1)
                memo[(i, j)] = res
                
            return memo[(i, j)]
        
        return dp(0, 0)
        '''
        # buttom-up
        # start from s = '' for each p
        dp = [[False] * (len(p) + 1) for _ in xrange(len(s) + 1)]
        dp[-1][-1] = True
        
        for i in xrange(len(s), -1, -1):
            for j in xrange(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]
        