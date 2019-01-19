# Shorted Job First

class Solution(object):
	def shortedJobFirst(self, req, dur):
		if not req or not dur:
			return 0

		ind = 0
		n = len(req)
		waitTime = 0
		currTime = 0

		pq = []
		