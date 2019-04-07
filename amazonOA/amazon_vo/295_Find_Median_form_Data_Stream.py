# 295 Find Median form Data Stream
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # maxheap
        self.lo = []
        
        # minheap
        self.hi = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lo) > len(self.hi):
            return -float(self.lo[0])
        
        res1 = self.lo[0]
        res2 = self.hi[0]
        return float(-res1 + res2) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


##################################
# Find 90th percentile Largest
class Find90thPercentile(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # maxheap
        self.lo = []

        # minheap
        self.hi = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        while len(self.lo) < (len(self.lo) + len(self.hi)) * 0.9:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))
        # print(self.lo, self.hi)
        

    def find90th(self):
        """
        :rtype: float
        """
        return -float(self.lo[0])

if __name__ == "__main__":
    sol = Find90thPercentile()
    sol.addNum(1)
    print(sol.find90th())
    sol.addNum(2)
    print(sol.find90th())
    sol.addNum(3)
    print(sol.find90th())
    sol.addNum(4)
    print(sol.find90th())
    sol.addNum(5)
    print(sol.find90th())
    sol.addNum(6)
    print(sol.find90th())
    sol.addNum(7)
    print(sol.find90th())
    sol.addNum(8)
    print(sol.find90th())
    sol.addNum(9)
    print(sol.find90th())
    sol.addNum(10)
    print(sol.find90th())
    sol.addNum(1)
    print(sol.find90th())
    sol.addNum(1)
    print(sol.find90th())
    sol.addNum(1)
    print(sol.find90th())

