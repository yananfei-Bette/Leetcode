# string multiply
# leetcode 43
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=444066

class Solution(object):
	def multiply(self, num1, num2):
		"""
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
        if not num1 or not num2:
        	return "0"

        n1 = len(num1)
        n2 = len(num2)

        digits = [0] * (n1 + n2)

        for i in range(n1 - 1, -1, -1):
        	for j in range(n2 - 1, -1, -1):
        		res1 = i + j
        		res2 = i + j + 1
        		curr = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0")) + digits[res2]
        		digits[res1] += curr / 10
        		digits[res2] = curr % 10

        res = ""
        for i in range(n1 + n2):
        	if not (not res and digits[i] == 0):
        		# remove first several 00000
        		res += str(digits[i])
        return res