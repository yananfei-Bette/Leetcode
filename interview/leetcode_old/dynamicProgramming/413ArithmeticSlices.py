#413 Arithmetic Slices
# dp list idea comes from https://leetcode.com/problems/arithmetic-slices/solution/
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # dp table time limit exceed
        '''
        if not A:
            return 0
        n = len(A)
        dp = [[False for i in range(n)] for j in range(n)]
        count = 0
        
        for i in range(n-3+1):
            #print i
            if A[i+2]-A[i+1] == A[i+1]-A[i]:
                dp[i][i+3-1] = True
                count += 1
        
        for k in range(4, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if dp[i][j-1] and A[j-1]-A[j-2] == A[j]-A[j-1]:
                    dp[i][j] = True
                    count += 1
        return count
        '''
        '''
        #recursive
        def numberOfAS(A, lasti, diff):
            if lasti+1 == len(A):
                return 1
            if A[lasti]-A[lasti+1] == diff:
                return 1+numberOfAS(A, lasti+1, diff)
            return 1
        
        count = 0
        for i in range(len(A)-2):
            if A[i]-A[i+1] == A[i+1]-A[i+2]:
                diff = A[i]-A[i+1]
                count += numberOfAS(A, i+2, diff)
        return count
        '''
        #dp list 
        if not A:
            return 0
        count = 0
        dp = [0 for i in range(len(A))]
        for i in range(len(A)-2):
            if A[i]-A[i+1] == A[i+1]-A[i+2]:
                dp[i+2] = 1+dp[i+1]
                count += dp[i+2]
        return count