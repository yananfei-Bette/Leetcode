class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        #################################################
        # DFS
        # store each node's earliest arrive
        # compare with recent arrtive
        # time: O(n^n + eloge)
        # space: O()
        '''
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        dist = {node: float("inf") for node in xrange(1, N + 1)}
        
        def dfs(currNode, spendTime):
            if spendTime >= dist[currNode]:
                return
            dist[currNode] = spendTime
            for time, nextNode in sorted(graph[currNode]):
                dfs(nextNode, spendTime + time)
        
        dfs(K, 0)
        res = max(dist.values())
        return res if res < float("inf") else -1
        '''
        ####################################################
        
        ####################################################
        # Dijkstra's
        # time: O(n*n)
        '''
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        dist = {node: float("inf") for node in xrange(1, N + 1)}
        seen = [False for _ in xrange(N + 1)]
        dist[K] = 0
        
        while True:
            candNode = -1
            candDist = float("inf")
            for i in xrange(1, N + 1):
                if not seen[i] and dist[i] < candDist:
                    candNode = i
                    candDist = dist[i]
            
            if candNode < 0:
                break
            seen[candNode] = True
            for time, nextNode in graph[candNode]:
                dist[nextNode] = min(dist[nextNode], dist[candNode] + time)
        
        res = max(dist.values())
        return res if res < float("inf") else -1
        '''
        ###############################################################
        ###############################################################
        # Dijkstra's
        # minheap
        # time: O(n*logn)
        '''
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        minheap = [(0, K)]
        dist = {} # use as seen and store the shortest path from source node to every rest nodes
        
        while minheap:
            time, currNode = heapq.heappop(minheap)
            if currNode in dist:
                continue
            dist[currNode] = time
            for w, nextNode in graph[currNode]:
                if nextNode not in dist:
                    heapq.heappush(minheap, (time + w, nextNode))
        return max(dist.values()) if len(dist) == N else -1
        '''
        #################################################################
        #################################################################
        # Bellman- Ford
        # time: O(V*E)
        '''
        dist = {node: float("inf") for node in xrange(1, N + 1)}
        dist[K] = 0
        
        for _ in xrange(1, N):
            for u, v, w in times:
                dist[v] = min(dist[v], dist[u] + w)
        
        # check negtive circle
        # check all edges
        for u, v, w in times:
            if dist[v] > dist[u] + w:
                return -1
        res = max(dist.values())
        return res if res < float("inf") else -1
        '''
        ##################################################################
        ##################################################################
        # Floyd- Warshall
        # time O(n*n*n)
        # Dynamic programming
        dist = [[float("inf")] * (N + 1) for _ in range(N + 1)]
        #print dist
        
        # directed graph
        for u, v, w in times:
            #print(u, v)
            dist[u][v] = w
            
        for i in xrange(1, N + 1):
            dist[i][i] = 0
        
        # for each separate point
        for k in xrange(1, N + 1):
            # start from i to j
            for i in xrange(1, N + 1):
                for j in xrange(1, N + 1):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res = float("-inf")
        for i in xrange(1, N + 1):
            if dist[K][i] == float("inf"):
                return -1
            res = max(res, dist[K][i])
            
        return res
        ##################################################################
                
        
        
        