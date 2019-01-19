# Round Robin
# A processor need to deal with butch of requests. It can only processes one request at a time. The maximum time of each task is q.
# After finishing one task or reaching the maximum time, the processor goes to the next. If the current task haven't finished yet, the processor put it in the end of unfinshed tasks list, and let it wait for the next execution.


class Process(object):
	def __init__(self, arr, exe):
		self.arrTime = arr
		self.exeTime = exe

class Soultion(object):
	def roundRobinScheduling(self, ArrTime, ExeTime, q):
		if not ArrTime or not ExeTime:
			return 0.0
		length = len(ArrTime)
		queue = []
		currTime = 0
		waitTime = 0
		ind = 0

		while queue or ind < length:
			if queue:
				currPorcess = queue.pop(0)
				waitTime += currTime - currPorcess.arrTime
				currTime += min(currPorcess.exeTime, q)
				while ind < length and ArrTime[ind] <= currTime:
					queue.append(Process(ArrTime[ind], ExeTime[ind]))
					ind += 1
				if currPorcess.exeTime > q:
					queue.append(Process(currTime, currPorcess.exeTime - q))
			else:
				queue.append(Process(ArrTime[ind], ExeTime[ind]))
				currTime = ArrTime[ind]
				ind += 1
		return float(waitTime) / length
