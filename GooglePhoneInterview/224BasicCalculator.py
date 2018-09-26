# 224 Basic Calculator 

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack
        # time: O(n)
        stack = []
        res = 0
        sign = 1
        i = 0
        while i < len(s):
            if 0 <= ord(s[i]) - ord('0') <= 9:
                num = ord(s[i]) - ord('0')
                #print num
                while i + 1 < len(s) and 0 <= ord(s[i + 1]) - ord('0') <= 9:
                    num = num * 10 + ord(s[i + 1]) - ord('0')
                    #print num
                    i += 1                    
                res += num * sign
                
            elif s[i] == '+':
                sign = 1
                
            elif s[i] == '-':
                sign = -1
                
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res = res * stack.pop() + stack.pop()
            i += 1
        return res
