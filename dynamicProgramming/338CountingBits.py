#338 Counting Bits
########
#idea is from: https://leetcode.com/problems/counting-bits/discuss/79539/Three-Line-Java-Solution
#https://leetcode.com/problems/counting-bits/discuss/147451/Simple-java-DP-solution-beats-100
#https://leetcode.com/problems/counting-bits/discuss/147259/Java-O(n)-1-ms-beats-100
'''
For every number, the number of bits = 1 + bits in num - ( previous power of 2).

Example :
12 => 1 + bits in (12-8) = 1 + bits in 4 = 1 + 1 = 2
13 => 1 + bits in (13-8) = 1 + bits in 5 = 1 + 2 = 3
14 => 1 + bits in (14-8) = 1 + bits in 6 = 1 + 2 = 3
'''
########
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]*(num+1)
        #base = 1
        for i in range(1, num+1):
            #dp[i] = 1 + dp[i&(i-1)]
            '''
            dp[i] = 1 + dp[i-base]
            if i == base*2 -1:
                base *= 2
            '''
            dp[i] = dp[i>>1]+(i&1)
        return dp