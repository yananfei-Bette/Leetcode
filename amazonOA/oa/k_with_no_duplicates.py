# find_array_of_size_k_with_no_duplicates

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
			if len(charSet) == k:
				res.append("".join(strArray[lo: lo + k]))
			lo += 1
		return res


if __name__ == "__main__":
	str = "abcbaa"
	k = 3
	sol = Solution()
	print(sol.countDist(str, k))