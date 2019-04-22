# LRU Cache Count Miss
class Solution(object):
	def CacheMiss(self, arr, size):
		if not arr:
			return 0
		cache = []
		count = 0
		for i in range(len(arr)):
			if arr[i] in cache:
				cache.remove(arr[i])
			else:
				count += 1
				if count == size:
					cache.pop(0)
				cache.append(arr[i])
		return count