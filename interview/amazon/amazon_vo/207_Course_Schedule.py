# 207 Course Schedule

# BFS topology
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # BFS with topology
        # Build graph with in-degree

        # corner case
        if not prerequisites:
            return True

        # build graph with in-dgree
        degree = [0] * numCourses
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            degree[prerequisites[i][0]] += 1

        # bfs
        queue = []
        count = 0

        # initialize queue
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
                count += 1

        while queue:
            course = queue.pop(0)
            neighbors = graph[course]
            for n in neighbors:
                degree[n] -= 1
                if degree[n] == 0:
                    queue.append(n)
                    count += 1

        if count == numCourses:
            return True
        return False


# DFS
# dfs to detect cycle
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(graph, seen, course):
            if course in seen:
                # has cycle
                return False

            seen.add(course)
            neighbors = graph[course]
            for n in neighbors:
                if not dfs(graph, seen, n):
                    return False

            seen.discard(course)
            return True


        if not prerequisites:
            return True

        # create a graph
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])

        seen = set()

        # dfs
        for i in range(numCourses):
            if not dfs(graph,seen, i):
                # has cycle
                return False
        return True



#######
# Follow up
# 269 Alien Dictionary
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # bfs with topology sort

        # edge case
        if not words:
            return ""

        # get all nodes
        nodes = set()
        for word in words:
            for char in word:
                nodes.add(char)

        # build a graph
        graph = {}
        degree = {}
        for i in range(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            for j in range(minLen):
                ch1 = words[i][j]
                ch2 = words[i + 1][j]
                if ch1 != ch2:
                    if ch1 not in graph or ch2 not in graph[ch1]:
                        degree[ch2] = degree.get(ch2, 0) + 1
                        graph[ch1] = graph.get(ch1, []) + [ch2]
                    break

        # bfs
        res = ""
        queue = []
        for node in nodes:
            if node not in degree:
                queue.append(node)

        while queue:
            node = queue.pop()
            res += node
            if node in graph:
                neighbors = graph[node]
                for n in neighbors:
                    degree[n] -= 1
                    if degree[n] == 0:
                        queue.append(n)

        # check if there is any cycle
        # if yes, return ""
        return res if len(res) == len(nodes) else ""

