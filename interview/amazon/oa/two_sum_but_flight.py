# two Sum but flight
def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
	if not forwardRouteList or not returnRouteList:
		return []

	f = forwardRouteList #sorted(forwardRouteList, key = lambda x: x[1])
	r = returnRouteList #sorted(returnRouteList, key = lambda x: x[1])

	res = []
	minDiff = float("inf")
	res = []

	for i in range(len(f)):
		if maxTravelDist < f[i][1]:
			continue
		for j in range(len(r)):
			if maxTravelDist < r[j][1]:
				continue

			curr = f[i][1] + r[j][1]
			diff = maxTravelDist - curr

			if 0 <= diff < minDiff:
				res = [[f[i][0], r[j][0]]]
				minDiff = diff
			elif diff == minDiff:
				res.append([f[i][0], r[j][0]])

	return res


if __name__ == "__main__":
	maxTravelDist1 = 7000
	forwardRouteList1 = [[1, 2000], [2, 4000], [3, 6000]]
	returnRouteList1 = [[1, 2000]]

	maxTravelDist = 10000
	forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
	returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
	
	print(optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList))



