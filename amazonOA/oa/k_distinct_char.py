# count number of substring with exactly k distinct characters
# https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/


class Solution(object):
	def countDist(self, str, k):
		n = len(str)
		res = []
		
		for i in range(n):
			dist_count = 0
			count = [0] * 26
			for j in range(i, n):
				if count[ord(str[j]) - ord("a")] == 0:
					dist_count += 1
				count[ord(str[j]) - ord("a")] += 1

				if dist_count == k:
					res.append(str[i: j + 1])
				if dist_count > k:
					break
		return res

if __name__ == "__main__":
	str = "abcbaa"
	k = 3
	sol = Solution()
	print(sol.countDist(str, k))












