#295 Find Median from Data Stream
class MedianFinder(object):
    #A max-heap to store the smaller half of the input numbers
    #A min-heap to store the larger half of the input numbers

    def __init__(self):
        """
        initialize your data structure here.
        """
        '''
        self.minheap = []
        #self.maxheap = []
        '''
        #maxheap
        self.lo = []
        #minheap
        self.hi = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        '''
        heapq.heappush(self.minheap, num)
        #heapq.heappush(self.maxheap, -num)
        '''
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        """
        :rtype: float
        """
        '''
        minheap = [i for i in self.minheap]
        l = len(minheap)
        if l%2 != 0:
            for i in range(1, l/2+1):
                heapq.heappop(minheap)
            return heapq.heappop(minheap)
        for i in range(1,l/2):
            heapq.heappop(minheap)
        return (heapq.heappop(minheap)+heapq.heappop(minheap))*0.5
        '''
        if len(self.lo) > len(self.hi):
            res = heapq.heappop(self.lo)
            heapq.heappush(self.lo, res)
            return float(-res)
        res_1 = heapq.heappop(self.lo)
        heapq.heappush(self.lo, res_1)
        res_2 = heapq.heappop(self.hi)
        heapq.heappush(self.hi, res_2)
        return (-res_1+res_2)*0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()