#
import sys 
for line in sys.stdin:
    a = line.split()
    n, m = int(a[0]), int(a[1])
    '''
    if n <= m:
        print(n%10007)
    dp = [0]*(n+1)
    for i in range(1, m+1):
        dp[i] = i
    for i in range(m+1, n+1):
        sum_dp = 0
        for j in range(1, m+1):
            sum_dp += dp[i-j]
        dp[i] = sum_dp
    print(dp[-1]%10007)
    '''
    def climb(i,n):
        if i > n:
            return 0
        if i == n:
            return 1
        sum_c = 0
        for j in range(1, m+1):
            sum_c = climb(i+j, n)
        return sum_c
    print(climb(0,n)
