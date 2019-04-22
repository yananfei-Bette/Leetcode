def optimalUtilization(maxTravelDist, forwardRouteList, returnRouteList):
    # WRITE YOUR CODE HERE
    f = sorted(forwardRouteList, key = lambda x: (x[1], x[0]), reverse = True)
    r = sorted(returnRouteList, key = lambda x: (x[1], x[0]), reverse = True)
    res = []
    curr = 0.0
    print(f)
    print(r)
    for i in range(len(f)):
        if maxTravelDist < f[i][1]:
            continue
        for j in range(len(r)):
            if maxTravelDist < r[i][1]:
                continue
            
            summ = f[i][1] + r[j][1]
            
            if res and summ < curr:
                break
            
            if summ <= maxTravelDist:
                if not res:
                    curr = summ
                    res.append([f[i][0], r[j][0]])
                elif summ > curr:
                    res.pop()
                    res.append([f[i][0], r[j][0]])
                    curr = summ
                elif summ == curr:
                    res.append([f[i][0], r[j][0]])
    return res

import heapq
def nearestVegetarianRestaurant(totalRestaurants, allLocations, numRestaurants):
    # WRITE YOUR CODE HERE
    H = []
    res = []
    for i in range(len(allLocations)):
        heapq.heappush(H, (- allLocations[i][0]**2 + allLocations[i][1]**2, allLocations[i]))
        if len(H) > numRestaurants:
            heapq.heappop(H)
    
    for e in H:
        res.append(e[1])
    return res


print(nearestVegetarianRestaurant(3, [[1, -3], [1, 2], [3, 4]], 1))

# print(optimalUtilization(20, [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]]))







