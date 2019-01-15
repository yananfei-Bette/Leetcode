# Grey code
# check if two byte numbers are gray code to each other
# https://www.1point3acres.com/bbs/thread-116704-1-1.html

def grayCheck(term1, term2):
	# XOR
	# Time: O(n)
	x = term1 ^ term2
	count = 0
	while x != 0:
		x = x & (x - 1)
		count += 1
	return True if count == 1 else False

def grayCheck(term1, term2):
	# Time: O(1)
	x = term1 ^ term2
	return x != 0 and (x & (x - 1) == 0)