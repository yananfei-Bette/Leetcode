#712 Minimum ASCII Delete Sum
#dp idea comes from https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        
        for i in range(len(s1)-1, -1, -1):
            dp[i][-1] = dp[i+1][-1]+ord(s1[i])
            
        for j in range(len(s2)-1, -1, -1):
            dp[-1][j] = dp[-1][j+1]+ord(s2[j])
            
        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j]+ord(s1[i]), dp[i][j+1]+ord(s2[j]))
        #print dp
        return dp[0][0]