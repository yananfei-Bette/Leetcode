# Highest Five
# lintcode 613 Highest Five

# https://yeqiuquan.blogspot.com/2017/03/lintcode-613-high-five.html

import heapq

class Solution(object):
	def highestFive(self, rederTimeOfPages):
		hashmap = {}
		k = 5

		for record in rederTimeOfPages:
			if record[0] not in hashmap:
				minheap = []
				hashmap[record[0]] = minheap
			heapq.heappush(hashmap[record[0]], record[1])
			if len(hashmap[record[0]]) > k:
				hashmap[record[0]] = heapq.heappop(hashmap[record[0]])


		res = []
		for key, vals in hashmap.items():
			res.append([key, float(sum(vals)) / len(vals)])
		return res

if __name__ == "__main__":
	records = [[1,91],[1,92],
				[2,93],[2,99],[2,98],[2,97],
				[1,60],[1,58],[2,100],[1,61]]
	sol = Solution()
	print(sol.highestFive(records))