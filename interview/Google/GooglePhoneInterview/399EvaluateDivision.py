#399 Evaluate Division
#idea comes from: https://leetcode.com/problems/evaluate-division/discuss/88196/Simple'n'Clean-DFS-solution-in-Python

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs(start, end, path, paths):
            #print path, paths
            if start == end and start in G:
                paths[0] = path
                return
            if start in vis:
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path*W[start, node], paths)
        
        #greate graph
        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            # set compute
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0/V
        '''
        print G
        print '********'
        print W
        defaultdict(<type 'set'>, {u'a': set([u'b']), u'c': set([u'b']), u'b': set([u'a', u'c'])})
        ********
        defaultdict(<type 'float'>, {(u'b', u'a'): 0.5, (u'a', u'b'): 2.0, (u'c', u'b'): 0.3333333333333333, (u'b', u'c'): 3.0})
        '''
        res = []
        for X, Y in queries:
            paths, vis = [-1.0], set()
            dfs(X,Y,1.0,paths)
            res += paths
        return res
