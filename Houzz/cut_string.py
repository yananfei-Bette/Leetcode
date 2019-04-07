# cut string
# given a string which has n
# now, we want to cut this string into several substrings
# let the product of all substrings be max.

# https://blog.csdn.net/xiangxianghehe/article/details/82427444


# Greedy
# when n >= 5, cur this string into 3 as much as possible
# when n == 4, cut it into two 2 subtrings

class Solution1(object):
	def cutString(self, n):
		if n in {2, 3, 4}:
			return n
		if n < 2:
			return 0
		return 3 * self.curString(n - 3)



# dp
# dp[n] = max(dp[i] * dp[n - i])
# dp[i] means, the max product of string with lenght i.

class Solution2(object):
	def curString(self, n):
		if n < 2:
			return 0
		if n == 2:
			return 1
		if n == 3:
			return 2

		dp = [0] * (n + 1)
		dp[1] = 1
		dp[2] = 2
		dp[3] = 3

		for i in range(4, n + 1):
			max_i = 0
			for j in range(1, i / 2 + 1):
				product = dp[j] * dp[i - j]
				if max_i < product:
					max_i = product
			dp[i] = max_i

		return dp[-1]
