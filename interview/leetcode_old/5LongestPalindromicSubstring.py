# 5 Longest Palindromic Substring
class Solution(object):
    def __init__(self):
        self.res = ''
        self.maxLen = 0
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp
        # time: O(n*n)
        # space: O(n*n)
        # iterative method
        '''
        if not s:
            return ''
        res = ''
        maxLen = 0
        dp = [[False] * len(s) for _ in xrange(len(s))]
        for j in xrange(len(s)):
            for i in xrange(j + 1):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    res = s[i:j + 1]
        return res
        '''
        ###############################
        # recursive method
        if not s:
            return ''
        
        for i in xrange(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)     
        return self.res
    
    def helper(self, s, i, j):
        while 0 <= i <= j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        # this part is important
        # check the boundary
        i += 1
        j -= 1
        if j - i + 1 > self.maxLen:
            self.maxLen = j - i + 1
            self.res = s[i: j + 1]
