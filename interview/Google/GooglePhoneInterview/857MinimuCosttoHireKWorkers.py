#857 Minimum Cost to Hire K Wokers
# idea comes form https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        '''
        #greedy
        #each factor
        ans = float('inf')
        N = len(quality)
        #N
        for caption in range(N):
            factor = float(wage[caption])/quality[caption]
            #SC: O(N)
            prices = []
            #N
            for worker in range(N):
                price = quality[worker]*factor
                if price < wage[worker]:
                    continue
                prices.append(price)
            
            if len(prices) < K:
                continue
            #logN
            prices.sort()
            ans = min(ans, sum(prices[:K]))
        return ans
        '''
        #heap
        #small ratio(factor) and small quality
        workers = sorted((float(w)/q, q, w) for w, q in zip(wage, quality))
        ans = float('inf')
        heapPool = []
        sumQualities = 0
        for ratio, q, w in workers:
            heapq.heappush(heapPool, -q)
            sumQualities += q
            
            if len(heapPool) > K:
                sumQualities += heapq.heappop(heapPool)
            if len(heapPool) == K:
                ans = min(ans, ratio*sumQualities)
        return ans

