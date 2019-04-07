# mst
# http://jingyid.me/2018/07/19/Amazon-OA2-Practice/
# https://www.cnblogs.com/biyeymyhjob/archive/2012/07/30/2615542.html

# already defined
class Connections(object):
	def __init__(self, city1, city2, cost):
		self.city1 = city1
		self.city2 = city2
		self.cost = cost


class Solution(object):
	def lowestCost(self, connections):
		"""
		type: list[connections]
		retype: list[connections]
		"""
		# sort the list
		connectionsSort = sorted(connections, 
			key = lambda x: (x.cost, x.city1, x.city2))

		# give each city id
		# save all nodes
		nameId = {}
		ind = 0
		for connect in connectionsSort:
			if connect.city1 not in nameId:
				ind += 1
				nameId[connect.city1] = ind
			if connect.city2 not in nameId:
				ind += 1
				nameId[connect.city2] = ind

		# union find
		# initial father arrry
		father = [None] * (ind + 1)
		for i in range(1, ind + 1):
			father[i] = i

		results = []
		for connect in connectionsSort:
			ind1 = nameId.get(connect.city1)
			ind2 = nameId.get(connect.city2)
			if self.find(father, ind1) != self.find(father, ind2):
				self.union(fatherr, ind1, ind2)
				result.append(connect)

		return results


	def find(self, father, ind):
		if father[ind] == ind:
			return ind
		return self.find(father, father[ind])

	def union(self, father, ind1, ind2):
		father1 = self.find(father, ind1)
		father2 = self.find(father, ind2)
		father[father1] = father2
		return











