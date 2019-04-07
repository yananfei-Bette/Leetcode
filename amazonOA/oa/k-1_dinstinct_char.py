# k - 1 dinstinct char


class Solution(object):
	def countDist(self, str, k):
		if not str or len(str) < k:
			return []

		strArray = list(str)
		res = []
		lo = 0
		while lo <= len(strArray) - k:
			charSet = set()
			for i in range(k):
				charSet.add(strArray[lo + i])
			if len(charSet) == k - 1:
				res.append("".join(strArray[lo: lo + k]))
			lo += 1
		return res


if __name__ == "__main__":
	str = "abcbaa"
	k = 3
	sol = Solution()
	print(sol.countDist(str, k))