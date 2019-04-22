# EA

# Brute force method
# Time: O(m * (n - m + 1))
class Solution1(object):
	def patternSearch(self, text, pattern):
		m = len(pattern)
		n = len(text)
		res = []

		if n < m:
			return res

		for i in range(n - m + 1):
			for j in range(m):
				if pattern[j] == "x":
					continue
				if text[i + j] != pattern[j]:
					break

			if j == m - 1:
				res.append(text[i: i + m])
		return res


# A better way to solve this problem is use KMP (one of pattern search methods)
# To reduce time complexity to O(n)

# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
# https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

# In KMP, the key is construct an auxiliary lps[] of size m
# which is used to skip characters while matching
# lps[]: indicates longest proper perfix (not consider word itself) which is also suffix
# lps[i] = the longest proper prefix of pat[0..i] 
#              which is also a suffix of pat[0..i].

# It is not easy that use KMP to solve. Cuz, "x" is not a fix character.
# Fail
class Solution2(object):
	def patternSearch(self, text, pattern, pattern_):
		m = len(pattern)
		n = len(text)
		res = []

		if m > n:
			return res

		lps = [0] * m
		##########
		def computeLPSArray(pattern_, m, lps):
			l = 0
			i = 1
			while i < m:
				if pattern[i] == pattern[l] or pattern[l] == "x":
					l += 1
					lps[i] = l
					i += 1
				else:
					if l != 0:
						l = lps[l - 1]
					else:
						lps[i] = 0
						i += 1
			return lps
		##########
		lps = computeLPSArray(pattern_, m, lps)
		print("************", lps)

		i = 0
		j = 0
		while i < n:
			if pattern[j] in {text[i], "x"}:
				i += 1
				j += 1
			if j == m:
				res.append(text[i - j: i])
				j = lps[j - 1]
			elif i < n and pattern[j] not in {text[i], "x"}:
				if j != 0:
					j = lps[j - 1]
				else:
					i += 1
		return res


if __name__ == "__main__":
	text1 = "a123b22, a&&^bbb,a5b2abb"
	pattern1 = "axxxbxx"
	pattern1_ = "aaaabbb"

	text2 = "a123a22, a&&^abb,a5b2abb"
	pattern2 = "axxxaxx"
	pattern2_ = "aaaaaaa"

	text3 = text1 = "aaaaabbabbbbaaababa"
	pattern3 = "xxaxxbx"
	pattern3_ = "xxaaabb"

	sol1 = Solution1()
	print(sol1.patternSearch(text3, pattern3))

	sol2 = Solution2()
	print(sol2.patternSearch(text3, pattern3, pattern3_))

