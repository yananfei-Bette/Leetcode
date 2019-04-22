# 17 Letter Combinations of a Phone Number

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # leetcode 46 Permutations
        if not digits:
            return []
        dic = {'2': 'abc', 
               '3': 'def', 
               '4':'ghi', 
               '5':'jkl', 
               '6':'mno', 
               '7':'pqrs', 
               '8': 'tuv', 
               '9': 'wxyz'
              }
        def helper(currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for char in dic[digits[len(currStr)]]:
                currStr += char
                helper(currStr)
                currStr = currStr[:len(currStr) - 1]
        
        res = []
        helper('')
        return res
        