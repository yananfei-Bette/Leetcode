# 277 Find the Celebrity

# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [i for i in range(n)]
        while len(stack) > 1:
            p1 = stack.pop()
            p2 = stack.pop()
            if knows(p1, p2):
                stack.append(p2)
            else:
                stack.append(p1)

        c = stack.pop()
        for i in range(n):
            if i != c and (knows(c, i) or not knows(i, c)):
                return -1
        return c

########## interivew question #############
class Solution_interivew(object):
    def findCelebrity(self, relationships):
        """
        :type repaltionships: List[[int]]
        :rtype: int
        """
        people = set()
        graph = {}

        for r in repaltionships:
            p1, p2 = r[0], r[1]
            people.add(p1)
            people.add(p2)

            graph[p1] = graph.get(p1, set()) | {p2}

        # check
        stack = [p for p in people]
        while len(stack) > 1:
            p1 = stack.pop()
            p2 = stack.pop()
            if p1 in graph:
                if p2 in graph[p1]:
                    stack.append(p2)
            else:
                stack.append(p1)

        c = stack.pop()
        for p in people:
            if p != c and (c in graph or (p in graph and c not in graph[p])):
                return -1

        return c

if __name__ == "__main__":
    repaltionships = [[1,2],[1,3],[2,3]]
    sol = Solution_interivew()
    print(sol.findCelebrity(repaltionships))