# reorder log files
# leetcode 937

class Solution(object):
	def reorderLogFiles(self, logs):
		"""
		:type logs: List[str]
		:rtype: List[str]
		"""
		def f(log):
			ind, res = log.split(" ", 1)
			return (0, res, ind) if res[0].isalpha() else (1,)
		return sorted(logs, key = f)