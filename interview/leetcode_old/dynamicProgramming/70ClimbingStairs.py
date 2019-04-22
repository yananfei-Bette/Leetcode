#70 Climbing Stairs
#######
#idea is from:https://leetcode.com/problems/climbing-stairs/solution/
'''
Algorithm

In this brute force approach we take all possible step combinations i.e. 1 and 2, at every step. At every step we are calling the function climbStairsclimbStairs for step 11 and 22, and return the sum of returned values of both functions.

climbStairs(i,n)=(i + 1, n) + climbStairs(i + 2, n) climbStairs(i,n)=(i+1,n)+climbStairs(i+2,n)

where ii defines the current step and nn defines the destination step.

Complexity Analysis

Time complexity : O(2^n)O(2
​n
​​ ). Size of recursion tree will be 2^n2
​n
​​ .

Recursion tree

One can reach i^{th}i
​th
​​  step in one of the two ways:

Taking a single step from (i-1)^{th}(i−1)
​th
​​  step.

Taking a step of 22 from (i-2)^{th}(i−2)
​th
​​  step.

So, the total number of ways to reach i^{th}i
​th
​​  is equal to sum of ways of reaching (i-1)^{th}(i−1)
​th
​​  step and ways of reaching (i-2)^{th}(i−2)
​th
​​  step.

Let dp[i]dp[i] denotes the number of ways to reach on i^{th}i
​th
​​  step:

dp[i]=dp[i-1]+dp[i-2] dp[i]=dp[i−1]+dp[i−2]

Complexity Analysis

Time complexity : O(n)O(n). Single loop upto nn.

Space complexity : O(n)O(n). dpdp array of size nn is used. 

Algorithm

In the above approach we have used dpdp array where dp[i]=dp[i-1]+dp[i-2]dp[i]=dp[i−1]+dp[i−2]. It can be easily analysed that dp[i]dp[i] is nothing but i^{th}i
​th
​​  fibonacci number.

Fib(n)=Fib(n-1)+Fib(n-2) Fib(n)=Fib(n−1)+Fib(n−2)

Now we just have to find n^{th}n
​th
​​  number of the fibonacci series having 11 and 22 their first and second term respectively, i.e. Fib(1)=1Fib(1)=1 and Fib(2)=2Fib(2)=2.

Complexity Analysis

Time complexity : O(n)O(n). Single loop upto nn is required to calculate n^{th}n
​th
​​  fibonacci number.

Space complexity : O(1)O(1). Constant space is used. 
'''
#######
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Brute Force
        #Time Limit Exceeded
        '''
        def climb(i,n):
            if i > n:
                return 0
            if i == n:
                return 1
            return climb(i+1,n)+climb(i+2,n)
        return climb(0,n)
        '''
        #Dynamic Programming
        '''
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0]*(n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
        '''
        #Fibnacci Number
        #Reduce space complexity
        if n == 1: return 1
        if n == 2: return 2
        f1, f2 = 1, 2
        for i in range(3, n+1):
            f1, f2 = f2, f1+f2
        return f2
