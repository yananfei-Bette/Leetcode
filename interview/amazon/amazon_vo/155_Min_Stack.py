# 155 Min Stack
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        currMin = self.getMin()
        if currMin == None or currMin > x:
            currMin = x
        self.stack.append((x, currMin))
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()