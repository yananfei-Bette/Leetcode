# 5 Longest Palindromic Substring

class Solution(object):
    '''
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp
        # time O(n*n)
        # space O(n*n)
        if not s or len(s) == 0:
            return s
        res = ''
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        maxCount = 0
        for j in range(len(s)):
            for i in range(j+1):
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1])
                if dp[i][j]:
                    if j - i + 1 > maxCount:
                        maxCount = j - i + 1
                        res = s[i:j+1]
        return res
    '''
    def __init__(self):
        self.res = ''
        
    def longestPalindrome(self, s):
        # central
        # time : O(n*n)
        # space : O(1)
        
        if not s or len(s) == 0:
            return s
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i+1)
        return self.res
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        currStr = s[left+1:right]
        if len(currStr) > len(self.res):
            self.res = currStr
        