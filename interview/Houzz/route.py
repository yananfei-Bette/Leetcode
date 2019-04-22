# route
# leetcode 332
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=484354
# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=470528&extra=&page=1


class Solution1(object):
	def findItinerary1(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		targets = {}
		for a, b in sorted(tickets):
			targets[a] = targets.get(a, []) + [b]
		
		# print targets
		
		route = []
		
		def visit(airport):
			while airport in targets and targets[airport]:
				visit(targets[airport].pop(0))
			route.append(airport)
			# print route
		
		visit("JFK")
		return route[::-1]


	def findIterinerary2(self, tickets):
		targets = {}
		for a, b in sorted(tickets):
			targets[a] = targets.get(a, []) + [b]

		route = []
		stack = ["JFK"]

		while stack:
			while stack[-1] in targets and targets[stack[-1]]:
				stack.append(targets[stack[-1]].pop(0))
			route.append(stack.pop())

		return route[::-1]


# In this problem
# It is also build a graph, dfs, update res
class Solution2(object):
	def __init__(self):
		self.resTime = []
		self.resPath = []
		self.visited = None


	def compareTime(self, t1, t2):
		"""
		:type: t1: str
		:type: t2: str
		:rtype: bool
		"""
		t1_ = int(t1[:2]) * 60 + int(t1[2:])
		t2_ = int(t2[:2]) * 60 + int(t2[2:])

		# we assume all tickets happend in one day
		t1_ = t1_ if t1_ else 24 * 60 + 60
		t2_ = t2_ if t2_ else 24 * 60 + 60

		return t1_ > t2_

	def compareTimeGeneral(self, timeInterval1, timeInterval2):
		pass
		

	def findOptimalPath(self, tickets, start, end):
		"""
		:type: tickets: List[List[str]]
		:type: start: str
		:type: end: str
		:rtype: List[str]
		"""
		dic = {}
		for t in tickets:
			dic[t[0]] = dic.get(t[0], []) + [(t[1], t[2], t[3])]


		def dfs(dic, airport, end, currPath, currTime):
			if airport == end:
				if not self.resTime:
					self.resTime = currTime
					self.resPath = currPath + [end]
				else:
					if self.compareTime(self.resTime[1], currTime[1]):
						self.resTime = currTime
						self.resPath = currPath + [end]
					elif self.compareTime(currTime[0], self.resTime[1]):
						self.resTime = currTime
						self.resPath = currPath + [end]
				return

			# check
			if airport not in dic:
				return

			# find
			for nextStop, departureTime, arrivalTime in dic[airport]:
				if nextStop in self.visited:
					continue

				# avoid cycle in this graph
				self.visited.add(nextStop)

				if not currTime:
					dfs(dic, nextStop, end, [airport], [departureTime, arrivalTime])
				else:
					if self.compareTime(departureTime, currTime[1]):
						dfs(dic, nextStop, end, currPath + [airport], [currTime[0], arrivalTime])
			return


		self.visited = set(start)
		dfs(dic, start, end, [], [])
		return self.resPath, self.resTime



if __name__ == "__main__":
	tickets1 = [["SAN FRANCISCO", "SANTA MONICA", "1100", "1230"],
				["SANTA MONICA", "LAX", "1240", "1330"],
				["SAN FRANCISCO", "LAX", "1130", "1430"]]
	start1 = "SAN FRANCISCO"
	end1 = "LAX"

	sol1 = Solution2()
	# print(sol1.findOptimalPath(tickets1, start1, end1))

	tickets2 = [["A", "B", "1000", "1100"],
				["B", "C", "1120", "1215"],
				["A", "C", "1015", "1250"]]
	start2 = "A"
	end2 = "C"

	sol2 = Solution2()
	print(sol2.findOptimalPath(tickets2, start2, end2))

















		
