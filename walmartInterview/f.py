#time : O(2^(n))
# 1 + 2 + 2*2 + ...
def f(num):
	if num == 1:
		return 1
	if num == 2:
		return 2
	res = f(num - 1) + f(num - 2)
	return res

# time : O(n)
def f(num):
	if num == 1:
		return 1
	if num == 2:
		return 2
	dp1, dp2 = 1, 2
	for i in range(2, num - 1):
		dp1, dp2 = dp2, dp1 + dp2
	return dp2