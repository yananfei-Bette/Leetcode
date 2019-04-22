#647 Palindromic Substrings
##########
'''
idea is from: https://leetcode.com/problems/palindromic-substrings/discuss/128581/Easy-to-understand-Python-DP-solution

A DP solution to this problem is to build a table with all possible string[start:end] combinations, storing which are palindromes and which are not (True or False). At any given moment, when you're checking if string[i:j] is a palindrome, you only need to know two things:

Is string[i] equal to string[j]?
Is string[i+1:j-1] a palindrome?
For condition (1), a simple check might do, for condition (2), you use the table. If both conditions are met, mark table[i][j] as True and increase your count
'''
##########
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = 0
        
        #kernel size = 1
        for i in range(n):
            dp[i][i] = True
            res += 1
            
        #kernel size = 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res += 1
        
        #kernel size >= 3
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
        return res