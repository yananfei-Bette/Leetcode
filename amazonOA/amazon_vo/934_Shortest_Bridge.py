# 934 Shortest Bridge

class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # dfs to find the islands and bfs to grow one of them

        # corner case
        if not A or not A[0]:
            return 0

        R, C = len(A), len(A[0])

        #############
        def get_neighbors(r, c):
            neighbors = []
            dirr = [-1, 1, 0, 0]
            dirc = [0, 0, -1, 1]

            for dr, dc in zip(dirr, dirc):
                cr, cc = r + dr, c + dc
                if 0 <= cr < R and 0 <= cc < C:
                    neighbors.append((cr, cc))

            return neighbors


        def get_components():
            seen = set()
            components = []

            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val == 1 and (r, c) not in seen:
                        # find island
                        # dfs
                        stack = [(r, c)]
                        visited = {(r, c)}

                        while stack:
                            curr_r, curr_c = stack.pop()
                            neighbors = get_neighbors(curr_r, curr_c)
                            for cr, cc in neighbors:
                                if A[cr][cc] == 1 and (cr, cc) not in visited:
                                    stack.append((cr, cc))
                                    visited.add((cr, cc))

                        # find one island
                        seen |= visited
                        components.append(visited)

            return components

        #############

        # dfs, get all components
        source, target = get_components()


        # bfs find bridge
        queue = []
        for node in source:
            queue.append((node, 0))

        seen = set()

        while queue:
            node, depth = queue.pop(0)
            if node in target:
                return depth - 1

            neighbors = get_neighbors(node[0], node[1])
            for n in neighbors:
                if n not in seen:
                    queue.append((n, depth + 1))
                    seen.add(n)

        return -1




