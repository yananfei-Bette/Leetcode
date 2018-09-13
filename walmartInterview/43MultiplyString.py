#43 Multiply String

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ###########################################
        #          num1    1   2   3   index i
        #          num2        4   5   index j
        #                 -------------
        #                      1   5
        #                  1   0
        #              0   5
        #                  1   2
        #              0   8
        #          0   4
        #        -----------------------
        #  index  [0,  1,  2,  3,  4]
        #
        #  indices [i + j, i + j + 1]
        ############################################
        # ord()
        # chr()
        
        # time: O(m*n)
        # space O(m+n)
        if not num1 or not num2:
            return '0'
        digits = [0]*(len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                product = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                p1 = i + j
                p2 = i + j + 1
                sumVal = product + digits[p2]
                digits[p1] += sumVal / 10
                digits[p2] = sumVal % 10
        
        res = ''
        for digit in digits:
            if not (digit == 0 and len(res) == 0):
                res += str(digit)
        return '0' if len(res) == 0 else res
        