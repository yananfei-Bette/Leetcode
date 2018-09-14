# walmart phone interview
'''
def Pow(x, n):

	def multiply(res, n, x):
		for i in range(1, n+1):
			res *= x
	return res

	res = 1
	return multiply(res, n, x) if n >=0 else 1.0/multiply(res, -n, x)
'''
def Pow(x, n):
	def recursion(x, n):
		if n == 0:
			return 1
		res = recursion(x, n/2)
		if n%2 == 1:
			return res * res * x
		else:
			return res * res

	mark = False
	if n < 0:
		n = -n
		mark = True
	if mark:
		return 1.0/recursion(x, n)
	else:
		return recursion(x, n)
'''
def Pow(x, n):
	if n == 0:
		return 1
	elif x == 0:
		return 0
	mark = False
	if n < 0:
		mark = True
		n = -n

	res = 1
	while n > 0:
		if n % 2 == 1:
			res *= x
			n -= 1
		else:
			x *= x
			n /= 2

	if mark:
		return 1.0/res
	return res
'''