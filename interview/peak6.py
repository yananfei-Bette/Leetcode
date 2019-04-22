# Best Rooftop
def beHappy(R, evensGrids):
	xMin = float("inf")
	yMin = float("inf")
	xMax = float("-inf")
	yMax = float("-inf")

	maxHappiness = 0
	numEvent = 0
	xRes = 0
	yRes = 0

	for point in evensGrids:
		xMin = min(xMin, point[0])
		yMin = min(yMin, point[1])
		xMax = max(xMax, point[0])
		yMax = max(yMax, point[1])

	for x in range(xMin, xMax + 1):
		for y in range(yMin, yMax + 1):
			currHappiness = 0
			currNumEvents = 0
			for point in evensGrids:
				D = 1 + math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
				if D <= R:
					currHappiness += point[2] / D
					currNumEvents += 1
			if currHappiness > maxHappiness:
				maxHappiness = currHappiness
				numEvent = currNumEvents
				xRes = x
				yRes = y
			elif currHappiness == maxHappiness:
				if currNumEvents > numEvent:
					numEvent = currHappiness
					xRes = x
					yRes = y
				elif currNumEvents == numEvent:
					if math.sqrt(x**2 + y**2) < math.sqrt(xRes**2 + yRes**2):
						xRes = x
						yRes = y
	return [xRes, yRes]

# Centennial Wheel
def closing_time(Queue, admission, runningCost):
	if not Queue:
		return 0

	maxProfit = 0
	currProfit = 0
	time = -1
	left = 0

	for i in range(len(Queue)):
		currPeople = Queue[i] + left
		if currPeople <= 4:
			left = 0
			currProfit += admission * currPeople - runningCost
		else:
			left = currPeople - 4
			currProfit += admission * 4 - runningCost

		if currProfit > maxProfit:
			maxProfit = currProfit
			time = i
	return time if maxProfit > 0 else -1
