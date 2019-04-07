# sqrt()
# leetcode 69
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=461849
# https://blog.csdn.net/u012050154/article/details/52554489


class Solution1(object):
	def mySqrt(self, x):
		# Time: O(logx)

		if x == 0:
			return 0

		lo, hi, res = 0, x, None
		while lo <= hi:
			mid = (lo + hi) // 2
			if mid ** 2 <= x:
				lo = mid + 1
				res = mid
			else:
				hi = mid - 1
		return res


class Solution2(object):
	def mySqrt(self, x, delta):
		# if we condiser x, delta is double
		if x < 0:
			return -1
		if x == 0.0:
			return 0.0

		lo, hi = 0.0, x
		mid = float(lo + hi) / 2

		while abs(mid ** 2 - x) > delta:
			if mid ** 2 < x:
				lo = mid
			elif mid ** 2 > x:
				hi = mid
			mid = float(lo + hi) / 2
		return mid


if __name__ == "__main__":
	x = 8
	delta = 0.001
	sol1 = Solution1()
	print(sol1.mySqrt(x))

	sol2 = Solution2()
	print(sol2.mySqrt(x, delta))
