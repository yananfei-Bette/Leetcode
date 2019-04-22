# 214 Shortest Palindrome

'''
Hence, we can find the largest segment from the beginning that is a palindrome, and we can then easily reverse the remaining segment and append to the beginning. This must be the required answer as no shorter palindrome could be found than this by just appending at the beginning.
'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rs = s[::-1]
        for i in xrange(len(s)):
            if s[:len(s)-i] == rs[i:]:
                return rs[:i]+s
        return ''
            
