# 6 ZigZag Conversion

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # rearrange according to rows and range by directions
        # time: O(n)
        # space: O(n)
        '''
        if numRows == 1:
            return s
        rows = [''] * min(numRows, len(s))
        r = 0
        goingDown = True
        for ch in s:
            rows[r] += ch
            if goingDown:
                r += 1
                if r == numRows:
                    goingDown = False
                    r -= 2
            else:
                r -= 1
                if r < 0:
                    goingDown = True
                    r += 2
        res = ''
        for row in rows:
            res += row
        return res
        '''
        ##############################
        # visit by rows and indexes
        # indexes: for row ith, k(2*numRows-2) + i and (k+1)*(2*numRows-2) - i
        # time: O(n)
        # space: O(n)
        if numRows == 1:
            return s
        res = ''
        n = len(s)
        delta = 2 * numRows - 2
        for i in xrange(numRows):
            for j in xrange(0, n - i, delta):
                res += s[j + i]
                if i != 0 and i != numRows - 1 and j + delta - i < n:
                    res += s[j + delta - i]
        return res